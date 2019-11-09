import pymel.core as pymel
import maya.OpenMayaUI as omui
import logging

from maya_game_fbx_exporter.core import exporter_core

reload(exporter_core)
from ui import main_window_ui
reload(main_window_ui)
from vendor.Qt import QtWidgets, QtCompat

log = logging.getLogger('maya_game_fbx_exporter')
gui = None
window_name = 'Maya Game Fbx Exporter'

def get_main_maya_window():
    ptr = omui.MQtUtil.mainWindow()
    return QtCompat.wrapInstance(long(ptr), QtWidgets.QMainWindow)


class GameFbxExporterUi(QtWidgets.QMainWindow):
    """
    Main window of the export tool
    """
    def __init__(self, parent=None):
        super(GameFbxExporterUi, self).__init__()

        self.ui = main_window_ui.Ui_win_maya_game_fbx_exporter()
        self.ui.setupUi(self)

        self.setWindowTitle(window_name)

        # Base state of certain ui element
        self.ui.tbl_subanims.setEnabled(False)

        # Signal connections
        self.ui.action_sel_data_network.triggered.connect(self.trig_action_select_data_network)
        self.ui.rdo_time_slider.toggled.connect(self.toggle_time_range)
        self.ui.chk_use_clip.toggled.connect(self.toggle_use_clip)
        self.ui.btn_add_new_char.pressed.connect(self.press_add_new_char)

        self.core = exporter_core.GameFbxExporterCore()
        self.core.load_all_data_network()
        self.update_ui()

    def update_ui(self, char_index=0):
        """
        Update the ui with the information found in the scene

        :param char_index: Index of the character selected in the list. Will be used to update the info
        """

        # Index of the combo box will match the order of the character
        self.ui.cb_character_list.clear()

        if self.core.character_nodes:
            for char in self.core.character_nodes:
                self.ui.cb_character_list.addItem(char.character_name)
            self.ui.cb_character_list.setCurrentIndex(char_index)
            self.ui.cb_character_list.setEnabled(True)
            self.update_ui_character(True, char_index)
            self.update_ui_animation(True, char_index)
        else:
            self.ui.cb_character_list.addItem('No Character Found')
            self.ui.cb_character_list.setEnabled(False)
            self.update_ui_character(False)
            self.update_ui_animation(False)

    def update_ui_character(self, is_valid, char_index=0):
        """
        Update the character ui element that can be used or not depending of the validity of the scene

        :param is_valid: Do we have a valid character in the scene
        :param char_index: Index of the character selected in the list. Will be used to update the info
        """

        # Clear old ui element value
        update_data = False
        self.ui.le_char_name.setText('')
        self.ui.le_root_name.setText('No Root Set')
        self.ui.lst_sk.clear()

        # If the node is referenced, prevent the user to modified the current character
        cur_char = None
        if is_valid:
            cur_char = self.core.character_nodes[char_index]
            update_data = True
            if cur_char._network.isReferenced():
                is_valid = False

        if is_valid:
            # Enable Ui Element
            self.ui.lbl_edit_char_name.setEnabled(True)
            self.ui.le_char_name.setEnabled(True)
            self.ui.btn_set_name.setEnabled(True)
            self.ui.lbl_root_node.setEnabled(True)
            self.ui.le_root_name.setEnabled(True)
            self.ui.btn_set_root.setEnabled(True)
            self.ui.btn_select_root.setEnabled(True)
            self.ui.btn_add_sk.setEnabled(True)
            self.ui.btn_remove_sk.setEnabled(True)
            self.ui.btn_sel_all_sk.setEnabled(True)
            self.ui.lst_sk.setEnabled(False)
        else:
            # Disable Ui Element
            self.ui.lbl_edit_char_name.setEnabled(False)
            self.ui.le_char_name.setEnabled(False)
            self.ui.btn_set_name.setEnabled(False)
            self.ui.lbl_root_node.setEnabled(False)
            self.ui.le_root_name.setEnabled(False)
            self.ui.btn_set_root.setEnabled(False)
            self.ui.btn_select_root.setEnabled(False)
            self.ui.btn_add_sk.setEnabled(False)
            self.ui.btn_remove_sk.setEnabled(False)
            self.ui.btn_sel_all_sk.setEnabled(False)
            self.ui.lst_sk.setEnabled(False)

        if update_data and cur_char:
            # Now set the good values
            self.ui.le_char_name.setText(cur_char.character_name)
            self.ui.le_root_name.setText(cur_char.root_node.name())
            for sk in cur_char.skeletal_meshes:
                self.ui.lst_sk.addItem(sk.name())

    def update_ui_animation(self, is_valid, char_index=0):
        """
        Update the animation ui element that can be used or not depending of the validity of the scene

        :param is_valid: Do we have a valid character in the scene
        :param char_index: Index of the character selected in the list. Will be used to update the info
        """

        if is_valid:
            self.ui.grp_anim.setEnabled(True)
        else:
            self.ui.grp_anim.setEnabled(False)

    #
    ## Ui connection function
    #

    def press_add_new_char(self):
        """
        Activate when the button add new character is pressed. It will setup a new character data in the scene
        :return:
        """

        error_msg = "You need to select only ONE valid root node (must be a joint type node) " \
                    "before adding a new character"
        # Ensure valid root node is valid before adding the new character
        if len(pymel.selected()) != 1:
            log.error(error_msg)
            return
        if pymel.general.nodeType(pymel.selected()[0]) != 'joint':
            log.error(error_msg)
            return

        root = pymel.selected()[0]

        result = pymel.promptDialog(
            title='Name the new character',
            message='Enter Name:',
            button=['OK', 'Cancel'],
            defaultButton='OK',
            cancelButton='Cancel',
            dismissString='Cancel')

        if result == 'OK':
            new_char_name = pymel.promptDialog(query=True, text=True)
            for char in self.core.character_nodes:
                if char.character_name == new_char_name:
                    log.error('Character named {0} already exist. Please choose another name')
                    return
            new_char = self.core.setup_new_character(new_char_name, root)
            self.update_ui(len(self.core.character_nodes) - 1)


    def trig_action_select_data_network(self):
        """
        Activate when the menu bar tag skeletal mesh is triggered.
        :return:
        """
        pymel.select(self.core.find_data_network())

    def toggle_time_range(self, checked):
        """
        Activate when time type radio button is changed. It will turn on/off start/end field
        :return:
        """

        if not checked:
            self.ui.le_start.setEnabled(False)
            self.ui.le_end.setEnabled(False)
        else:
            self.ui.le_start.setEnabled(True)
            self.ui.le_end.setEnabled(True)

    def toggle_use_clip(self, checked):
        """
        Activate when use clip checkbox is change. It will turn on/of the subanim table and time range field
        :return:
        """

        if checked:
            self.ui.tbl_subanims.setEnabled(True)
            self.ui.grp_anim_time.setEnabled(False)
            self.ui.btn_add_subanim.setEnabled(False)
            self.ui.btn_remove_subanim.setEnabled(False)
        else:
            self.ui.tbl_subanims.setEnabled(False)
            self.ui.grp_anim_time.setEnabled(True)
            self.ui.btn_add_subanim.setEnabled(True)
            self.ui.btn_remove_subanim.setEnabled(True)


def show():
    """
    Show the ui and center it in the middle of the main screen
    :return: None
    """
    # Try to kill latest window if our ui
    try:
        pymel.deleteUI(window_name)
    except:
        pass

    global gui

    gui = GameFbxExporterUi(get_main_maya_window())

    # Create a frame geo to easilly move it from the center
    pFrame = gui.frameGeometry()
    pScreen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
    ptCenter = QtWidgets.QApplication.desktop().screenGeometry(pScreen).center()
    pFrame.moveCenter(ptCenter)
    gui.move(pFrame.topLeft())

    gui.show()