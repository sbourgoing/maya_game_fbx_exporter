# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gsq_sbourgoing\Documents\Git\maya_game_fbx_exporter\resources\ui\main_window_ui.ui'
#
# Created: Thu Nov  7 09:22:50 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_win_maya_game_fbx_exporter(object):
    def setupUi(self, win_maya_game_fbx_exporter):
        win_maya_game_fbx_exporter.setObjectName("win_maya_game_fbx_exporter")
        win_maya_game_fbx_exporter.resize(917, 1104)
        self.centralwidget = QtWidgets.QWidget(win_maya_game_fbx_exporter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_character_root = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_character_root.sizePolicy().hasHeightForWidth())
        self.lbl_character_root.setSizePolicy(sizePolicy)
        self.lbl_character_root.setObjectName("lbl_character_root")
        self.horizontalLayout_5.addWidget(self.lbl_character_root)
        self.cb_character_list = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_character_list.sizePolicy().hasHeightForWidth())
        self.cb_character_list.setSizePolicy(sizePolicy)
        self.cb_character_list.setEditable(False)
        self.cb_character_list.setObjectName("cb_character_list")
        self.horizontalLayout_5.addWidget(self.cb_character_list)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.grp_export = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_export.sizePolicy().hasHeightForWidth())
        self.grp_export.setSizePolicy(sizePolicy)
        self.grp_export.setObjectName("grp_export")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.grp_export)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.chk_root_no_parent = QtWidgets.QCheckBox(self.grp_export)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_root_no_parent.sizePolicy().hasHeightForWidth())
        self.chk_root_no_parent.setSizePolicy(sizePolicy)
        self.chk_root_no_parent.setObjectName("chk_root_no_parent")
        self.verticalLayout_5.addWidget(self.chk_root_no_parent)
        self.verticalLayout_4.addWidget(self.grp_export)
        self.grp_anim = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_anim.setObjectName("grp_anim")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.grp_anim)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_export_path = QtWidgets.QLabel(self.grp_anim)
        self.lbl_export_path.setScaledContents(False)
        self.lbl_export_path.setObjectName("lbl_export_path")
        self.horizontalLayout_6.addWidget(self.lbl_export_path)
        self.le_export_path = QtWidgets.QLineEdit(self.grp_anim)
        self.le_export_path.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_export_path.sizePolicy().hasHeightForWidth())
        self.le_export_path.setSizePolicy(sizePolicy)
        self.le_export_path.setReadOnly(True)
        self.le_export_path.setObjectName("le_export_path")
        self.horizontalLayout_6.addWidget(self.le_export_path)
        self.btn_browse_export_path = QtWidgets.QPushButton(self.grp_anim)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_browse_export_path.sizePolicy().hasHeightForWidth())
        self.btn_browse_export_path.setSizePolicy(sizePolicy)
        self.btn_browse_export_path.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_browse_export_path.setObjectName("btn_browse_export_path")
        self.horizontalLayout_6.addWidget(self.btn_browse_export_path)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chk_use_clip = QtWidgets.QCheckBox(self.grp_anim)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_use_clip.sizePolicy().hasHeightForWidth())
        self.chk_use_clip.setSizePolicy(sizePolicy)
        self.chk_use_clip.setObjectName("chk_use_clip")
        self.verticalLayout_3.addWidget(self.chk_use_clip)
        self.grp_animOptions = QtWidgets.QGroupBox(self.grp_anim)
        self.grp_animOptions.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_animOptions.sizePolicy().hasHeightForWidth())
        self.grp_animOptions.setSizePolicy(sizePolicy)
        self.grp_animOptions.setObjectName("grp_animOptions")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.grp_animOptions)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rdo_time_slider = QtWidgets.QRadioButton(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdo_time_slider.sizePolicy().hasHeightForWidth())
        self.rdo_time_slider.setSizePolicy(sizePolicy)
        self.rdo_time_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rdo_time_slider.setChecked(True)
        self.rdo_time_slider.setObjectName("rdo_time_slider")
        self.horizontalLayout.addWidget(self.rdo_time_slider)
        self.rdo_time_start_end = QtWidgets.QRadioButton(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdo_time_start_end.sizePolicy().hasHeightForWidth())
        self.rdo_time_start_end.setSizePolicy(sizePolicy)
        self.rdo_time_start_end.setChecked(False)
        self.rdo_time_start_end.setObjectName("rdo_time_start_end")
        self.horizontalLayout.addWidget(self.rdo_time_start_end)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_time = QtWidgets.QLabel(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_time.sizePolicy().hasHeightForWidth())
        self.lbl_time.setSizePolicy(sizePolicy)
        self.lbl_time.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_time.setObjectName("lbl_time")
        self.horizontalLayout_2.addWidget(self.lbl_time)
        self.le_start = QtWidgets.QLineEdit(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_start.sizePolicy().hasHeightForWidth())
        self.le_start.setSizePolicy(sizePolicy)
        self.le_start.setObjectName("le_start")
        self.horizontalLayout_2.addWidget(self.le_start)
        self.le_end = QtWidgets.QLineEdit(self.grp_animOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_end.sizePolicy().hasHeightForWidth())
        self.le_end.setSizePolicy(sizePolicy)
        self.le_end.setObjectName("le_end")
        self.horizontalLayout_2.addWidget(self.le_end)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.grp_animOptions)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tbl_subanims = QtWidgets.QTableWidget(self.grp_anim)
        self.tbl_subanims.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_subanims.sizePolicy().hasHeightForWidth())
        self.tbl_subanims.setSizePolicy(sizePolicy)
        self.tbl_subanims.setProperty("showDropIndicator", True)
        self.tbl_subanims.setAlternatingRowColors(True)
        self.tbl_subanims.setColumnCount(3)
        self.tbl_subanims.setObjectName("tbl_subanims")
        self.tbl_subanims.setColumnCount(3)
        self.tbl_subanims.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_subanims.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_subanims.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_subanims.setHorizontalHeaderItem(2, item)
        self.tbl_subanims.horizontalHeader().setVisible(True)
        self.tbl_subanims.horizontalHeader().setHighlightSections(True)
        self.tbl_subanims.horizontalHeader().setSortIndicatorShown(False)
        self.tbl_subanims.horizontalHeader().setStretchLastSection(True)
        self.tbl_subanims.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tbl_subanims)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_add_subanim = QtWidgets.QPushButton(self.grp_anim)
        self.btn_add_subanim.setObjectName("btn_add_subanim")
        self.horizontalLayout_3.addWidget(self.btn_add_subanim)
        self.btn_remove_subanim = QtWidgets.QPushButton(self.grp_anim)
        self.btn_remove_subanim.setObjectName("btn_remove_subanim")
        self.horizontalLayout_3.addWidget(self.btn_remove_subanim)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.grp_anim)
        win_maya_game_fbx_exporter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(win_maya_game_fbx_exporter)
        self.statusbar.setObjectName("statusbar")
        win_maya_game_fbx_exporter.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(win_maya_game_fbx_exporter)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 917, 36))
        self.menuBar.setObjectName("menuBar")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        win_maya_game_fbx_exporter.setMenuBar(self.menuBar)
        self.action_tag_sk = QtWidgets.QAction(win_maya_game_fbx_exporter)
        self.action_tag_sk.setObjectName("action_tag_sk")
        self.action_tag_root = QtWidgets.QAction(win_maya_game_fbx_exporter)
        self.action_tag_root.setObjectName("action_tag_root")
        self.action_sel_data_network = QtWidgets.QAction(win_maya_game_fbx_exporter)
        self.action_sel_data_network.setEnabled(True)
        self.action_sel_data_network.setObjectName("action_sel_data_network")
        self.menuTools.addAction(self.action_sel_data_network)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_tag_root)
        self.menuTools.addAction(self.action_tag_sk)
        self.menuTools.addSeparator()
        self.menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(win_maya_game_fbx_exporter)
        QtCore.QMetaObject.connectSlotsByName(win_maya_game_fbx_exporter)

    def retranslateUi(self, win_maya_game_fbx_exporter):
        win_maya_game_fbx_exporter.setWindowTitle(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Maya Game Fbx Exporter", None, -1))
        self.lbl_character_root.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Character Root:", None, -1))
        self.grp_export.setTitle(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Export Options", None, -1))
        self.chk_root_no_parent.setToolTip(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Will Unparent if needed", None, -1))
        self.chk_root_no_parent.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Ensure Root Joint Have Not Parent", None, -1))
        self.grp_anim.setTitle(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Animation Options", None, -1))
        self.lbl_export_path.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Export Path:", None, -1))
        self.btn_browse_export_path.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "...", None, -1))
        self.chk_use_clip.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Use Animation Clips", None, -1))
        self.grp_animOptions.setTitle(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Time range", None, -1))
        self.rdo_time_slider.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Time Slider", None, -1))
        self.rdo_time_start_end.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Start/End", None, -1))
        self.lbl_time.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Start/End:", None, -1))
        self.tbl_subanims.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "SubAnim Name", None, -1))
        self.tbl_subanims.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Start", None, -1))
        self.tbl_subanims.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "End", None, -1))
        self.btn_add_subanim.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Add SubAnim", None, -1))
        self.btn_remove_subanim.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Remove SubAnim", None, -1))
        self.menuTools.setTitle(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Tools", None, -1))
        self.action_tag_sk.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Tag Selection As Skeletal Mesh", None, -1))
        self.action_tag_sk.setToolTip(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Tag mesh of a character for animation export.", None, -1))
        self.action_tag_sk.setShortcut(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Ctrl+S", None, -1))
        self.action_tag_root.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Tag Selection As Root Joint", None, -1))
        self.action_tag_root.setToolTip(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Tag a joint as the root hierarchy of a character for animation export", None, -1))
        self.action_tag_root.setShortcut(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Ctrl+R", None, -1))
        self.action_sel_data_network.setText(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Select Data Network", None, -1))
        self.action_sel_data_network.setShortcut(QtWidgets.QApplication.translate("win_maya_game_fbx_exporter", "Ctrl+D", None, -1))

