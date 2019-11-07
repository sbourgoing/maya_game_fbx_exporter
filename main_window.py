from maya import cmds
import pymel.core as pymel
from maya import OpenMaya
import maya.OpenMayaUI as omui
import logging

import exporter_core
reload(exporter_core)
from ui import main_window_ui
reload(main_window_ui)
from vendor.Qt import QtCore, QtGui, QtWidgets, QtCompat

log = logging.getLogger('maya_game_fbx_exporter')
gui = None
window_name = 'Maya Fbx Animation Exporter'

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
        self.ui.action_tag_root.triggered.connect(self.trig_action_tag_root)
        self.ui.action_tag_sk.triggered.connect(self.trig_action_tag_sk)
        self.ui.action_sel_data_network.triggered.connect(self.trig_action_select_data_network)
        self.ui.rdo_time_slider.toggled.connect(self.toggle_time_range)
        self.ui.chk_use_clip.toggled.connect(self.toggle_use_clip)

    #
    ## Ui connection function
    #

    def trig_action_tag_root(self):
        """
        Activate when the menu bar tag root is triggered.
        :return:
        """
        exporter_core.GameFbxExporterCore.tag_selection_as_root(pymel.selected())

    def trig_action_tag_sk(self):
        """
        Activate when the menu bar tag skeletal mesh is triggered.
        :return:
        """
        exporter_core.GameFbxExporterCore.tag_selection_as_sk(pymel.selected())

    def trig_action_select_data_network(self):
        """
        Activate when the menu bar tag skeletal mesh is triggered.
        :return:
        """
        pymel.select(exporter_core.GameFbxExporterCore.get_data_network())

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