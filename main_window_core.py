from maya import cmds
import pymel.core as pymel
from maya import OpenMaya
import maya.OpenMayaUI as omui
import logging

from ui import main_window
reload(main_window)
from vendor.Qt import QtCore, QtGui, QtWidgets, QtCompat

log = logging.getLogger('maya_game_fbx_anim_exporter')
gui = None
window_name = 'Maya Fbx Animation Exporter'


def get_main_maya_window():
    ptr = omui.MQtUtil.mainWindow()
    return QtCompat.wrapInstance(long(ptr), QtWidgets.QMainWindow)


class GameFbxExporter(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(GameFbxExporter, self).__init__()

        self.ui = main_window.Ui_win_mayaGameFbxExporter()
        self.ui.setupUi(self)

        self.setWindowTitle(window_name)


def show():
    # Try to kill latest Autorig ui window
    try:
        pymel.deleteUI(window_name)
    except:
        pass

    global gui

    gui = GameFbxExporter(get_main_maya_window())

    # Create a frame geo to easilly move it from the center
    pFrame = gui.frameGeometry()
    pScreen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
    ptCenter = QtWidgets.QApplication.desktop().screenGeometry(pScreen).center()
    pFrame.moveCenter(ptCenter)
    gui.move(pFrame.topLeft())

    gui.show()