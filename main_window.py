import pymel.core as pymel
import maya.OpenMayaUI as omui
import logging

from core import exporter_core

reload(exporter_core)
from ui import main_window_ui
reload(main_window_ui)
from vendor.Qt import QtWidgets, QtCompat, QtGui

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
        super(GameFbxExporterUi, self).__init__(parent)

        self.cur_char = None # Current selected character information

        self._no_cb_char_update = False # Flag to prevent char combo box index change signal to update ui

        self.ui = main_window_ui.Ui_win_maya_game_fbx_exporter()
        self.ui.setupUi(self)

        self.setWindowTitle(window_name)

        # Base state of certain ui element
        self.ui.tbl_subanims.setEnabled(False)

        # Signal connections
        self.ui.action_sel_data_network.triggered.connect(self.trig_action_select_data_network)
        self.ui.rdo_time_slider.toggled.connect(self.toggle_time_range)
        self.ui.cb_character_list.currentIndexChanged.connect(self.index_change_current_character)
        self.ui.btn_remove_char.clicked.connect(self.clicked_remove_char)

        # Animation Tab
        self.ui.chk_use_clip.toggled.connect(self.toggle_use_clip)

        # Character Tab
        self.ui.btn_add_new_char.clicked.connect(self.clicked_add_new_char)
        self.ui.btn_set_name.clicked.connect(self.clicked_set_name)
        self.ui.btn_set_root.clicked.connect(self.clicked_set_selected_as_root)
        self.ui.btn_select_root.clicked.connect(self.clicked_select_current_root)
        self.ui.btn_add_sk.clicked.connect(self.clicked_add_selected_as_skel_mesh)
        self.ui.btn_remove_sk.clicked.connect(self.clicked_remove_list_selected_as_skel_mesh)
        self.ui.btn_sel_all_sk.clicked.connect(self.clicked_select_all_skel_mesh)

        # Core init
        self._core = exporter_core.GameFbxExporterCore()
        self._core.load_all_data_network()
        self.update_ui()

    def update_ui(self, char_index=0, clear=True):
        """
        Update the ui with the information found in the scene

        :param char_index: Index of the character selected in the list. Will be used to update the info
        :param clear: Do we want to clear and reset the list or just change the index ?
        """

        self._no_cb_char_update = True

        if clear:
            # Index of the combo box will match the order of the character
            self.ui.cb_character_list.clear()

            # If we have data, update the list with it, else, just deactivate it
            if self._core.character_nodes:
                for char in self._core.character_nodes:
                    self.ui.cb_character_list.addItem(char.character_name)
                self.ui.cb_character_list.setCurrentIndex(char_index)
                self.ui.cb_character_list.setEnabled(True)
                self.ui.btn_remove_char.setEnabled(True)
                self.update_ui_character(True, char_index)
                self.update_ui_animation(True, char_index)
            else:
                self.ui.cb_character_list.addItem('No Character Found')
                self.ui.cb_character_list.setEnabled(False)
                self.ui.btn_remove_char.setEnabled(False)
                self.update_ui_character(False, char_index)
                self.update_ui_animation(False, char_index)
        else:
            self.update_ui_character(True, char_index)
            self.update_ui_animation(True, char_index)

        self._no_cb_char_update = False

    def update_ui_character(self, is_valid, char_index=0):
        """
        Update the character ui element that can be used or not depending of the validity of the scene

        :param is_valid: Do we have a valid character in the scene
        :param char_index: Index of the character selected in the list. Will be used to update the info
        """

        #TODO - Improve perf with preventing update when not needed

        # Clear old ui element value
        update_data = False
        self.ui.le_char_name.setText('')
        self.ui.le_root_name.setText('No Root Set')
        self.ui.lst_sk.clear()
        self.cur_char = None

        # If the node is referenced, prevent the user to modified the current character
        if is_valid:
            self.cur_char = self._core.character_nodes[char_index]
            if self.cur_char._network.isReferenced():
                self.ui.btn_remove_char.setEnabled(False)
            update_data = True
            if self.cur_char._network.isReferenced():
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
            if self.cur_char.skeletal_meshes:
                self.ui.lst_sk.setEnabled(True)
                self.ui.btn_remove_sk.setEnabled(True)
                self.ui.btn_sel_all_sk.setEnabled(True)
            else:
                self.ui.lst_sk.setEnabled(False)
                self.ui.btn_remove_sk.setEnabled(False)
                self.ui.btn_sel_all_sk.setEnabled(False)
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

        if update_data and self.cur_char:
            # Now set the good values
            self.ui.le_char_name.setText(self.cur_char.character_name)
            self.ui.le_root_name.setText(self.cur_char.root_node.name())
            for sk in self.cur_char.skeletal_meshes:
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

    def set_char_name(self, new_char=False):
        """
        Ask the user for a character name and do some validation over it

        :param new_char: Is the name set for a new character ?
        :return: The new name or none if invalid
        """
        new_char_name = None
        user_input, clicked = QtWidgets.\
            QInputDialog().getText(self, 'Change Character Name' if not new_char else "Choose Character Name",
                                                                "Name:",
                                                                QtWidgets.QLineEdit.Normal,
                                                                '' if not self.cur_char or new_char else self.cur_char.character_name)
        if user_input and clicked:
            new_char_name = user_input
            for char in self._core.character_nodes:
                if new_char and char.character_name == new_char_name:
                    log.error('Character named {0} already exist. Please choose another name'.format(new_char_name))
                    break
                if not new_char and self.cur_char != char and char.character_name == new_char_name:
                    log.error('Character named {0} already exist. Please choose another name'.format(new_char_name))
                    break

        return new_char_name

    def root_node_selection_validation(self):
        """
        Ensure the current selection in the scene can be use as a root node candidate
        :return: True or False depending of the validation
        """

        error_msg = "You need to select only ONE valid root node (must be a joint type node) " \
                    "before adding a new character"
        # Ensure valid root node is valid before adding the new character
        if len(pymel.selected()) != 1:
            log.error(error_msg)
            return False
        if pymel.general.nodeType(pymel.selected()[0]) != 'joint':
            log.error(error_msg)
            return False

        return True

    #
    ## Ui connection function
    #

    def index_change_current_character(self, new_index):
        """
        Activate when the character drop down list index change. Do the character switch and update the ui

        :param new_index: The new character index changed for
        """
        if not self._no_cb_char_update:
            self.update_ui(new_index, clear=False)

    def clicked_remove_char(self):
        """
        Remove all the current character data from the scene and update the ui
        :return:
        """
        self._core.remove_character(self.cur_char)
        self.update_ui()


    # Character Tab ui elements signal functions

    def clicked_add_new_char(self):
        """
        Activate when the button add new character is clicked. It will setup a new character data in the scene
        :return:
        """

        if not self.root_node_selection_validation():
            return

        root = pymel.selected()[0]

        new_char_name = self.set_char_name(new_char=True)

        if new_char_name:
            new_char = self._core.setup_new_character(new_char_name, root)
            self.update_ui(len(self._core.character_nodes) - 1)

    def clicked_set_name(self):
        """
        Set the name of the current selected character

        :return:
        """
        new_name = self.set_char_name()

        if new_name:
            self.cur_char.character_name = new_name
            self._core.save_data_network(self.cur_char)
            self.update_ui(self.ui.cb_character_list.currentIndex())

    def clicked_set_selected_as_root(self):
        """
        Change the root of the selected character for the selected node. The node need to be single selected and
        pass the validation of the character node
        :return:
        """

        if not self.root_node_selection_validation():
            return

        new_root = pymel.selected()[0]
        if self._core.check_root_node_validation(new_root):
            self.cur_char.set_root_node(new_root)
            self._core.save_data_network(self.cur_char)
            self.update_ui(self.ui.cb_character_list.currentIndex(), clear=False)

    def clicked_select_current_root(self):
        """
        Select, in the scene, the current character root joint
        :return:
        """
        pymel.select(self.cur_char.root_node)

    def clicked_add_selected_as_skel_mesh(self):
        """
        Add the selected scene node as skeletal mesh to export with the character. Those node need to pass
        validation before
        :return:
        """

        # TODO - Add core check with other character to prevent addition of same mesh in multiple character
        if self.cur_char.add_skeletal_mesh(pymel.selected()):
            self._core.save_data_network(self.cur_char)
            self.update_ui(self.ui.cb_character_list.currentIndex(), clear=False)


    def clicked_remove_list_selected_as_skel_mesh(self):
        """
        Remove the selected mesh in the list from the mesh to export with the character
        :return:
        """

        for list_sel in self.ui.lst_sk.selectedItems():
            pass

    def clicked_select_all_skel_mesh(self):
        raise NotImplementedError()

    # Action signal functions
    def trig_action_select_data_network(self):
        """
        Activate when the menu bar tag skeletal mesh is triggered.
        :return:
        """
        pymel.select(self._core.find_data_network())

    # Animation Tab ui elements signal functions
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