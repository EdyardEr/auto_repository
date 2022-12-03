# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ederm\Desktop\my_projects\repository\qt_designer_files\\main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 420)
        MainWindow.setToolTipDuration(-1)
        self.MainWidget = QtWidgets.QWidget(MainWindow)
        self.MainWidget.setToolTipDuration(-1)
        self.MainWidget.setObjectName("MainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainTab = QtWidgets.QTabWidget(self.MainWidget)
        self.MainTab.setToolTipDuration(-2)
        self.MainTab.setObjectName("MainTab")
        self.Tracker_tab = QtWidgets.QWidget()
        self.Tracker_tab.setObjectName("Tracker_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Tracker_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reps_row = QtWidgets.QHBoxLayout()
        self.reps_row.setObjectName("reps_row")
        self.label_2 = QtWidgets.QLabel(self.Tracker_tab)
        self.label_2.setObjectName("label_2")
        self.reps_row.addWidget(self.label_2)
        self.rep_list = QtWidgets.QComboBox(self.Tracker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rep_list.sizePolicy().hasHeightForWidth())
        self.rep_list.setSizePolicy(sizePolicy)
        self.rep_list.setMinimumSize(QtCore.QSize(310, 0))
        self.rep_list.setMaximumSize(QtCore.QSize(310, 16777215))
        self.rep_list.setObjectName("rep_list")
        self.reps_row.addWidget(self.rep_list)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reps_row.addItem(spacerItem)
        self.create_rep = QtWidgets.QPushButton(self.Tracker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_rep.sizePolicy().hasHeightForWidth())
        self.create_rep.setSizePolicy(sizePolicy)
        self.create_rep.setObjectName("create_rep")
        self.reps_row.addWidget(self.create_rep)
        self.del_rep = QtWidgets.QPushButton(self.Tracker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_rep.sizePolicy().hasHeightForWidth())
        self.del_rep.setSizePolicy(sizePolicy)
        self.del_rep.setObjectName("del_rep")
        self.reps_row.addWidget(self.del_rep)
        self.verticalLayout_2.addLayout(self.reps_row)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.track_indicator = QtWidgets.QPushButton(self.Tracker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.track_indicator.sizePolicy().hasHeightForWidth())
        self.track_indicator.setSizePolicy(sizePolicy)
        self.track_indicator.setMaximumSize(QtCore.QSize(20, 20))
        self.track_indicator.setText("")
        self.track_indicator.setObjectName("track_indicator")
        self.horizontalLayout_2.addWidget(self.track_indicator)
        self.track_dir = QtWidgets.QPushButton(self.Tracker_tab)
        self.track_dir.setObjectName("track_dir")
        self.horizontalLayout_2.addWidget(self.track_dir)
        self.track_settings = QtWidgets.QPushButton(self.Tracker_tab)
        self.track_settings.setObjectName("track_settings")
        self.horizontalLayout_2.addWidget(self.track_settings)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.track_row = QtWidgets.QHBoxLayout()
        self.track_row.setContentsMargins(0, -1, -1, -1)
        self.track_row.setSpacing(7)
        self.track_row.setObjectName("track_row")
        self.label = QtWidgets.QLabel(self.Tracker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.track_row.addWidget(self.label)
        self.repository_path = QtWidgets.QLabel(self.Tracker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repository_path.sizePolicy().hasHeightForWidth())
        self.repository_path.setSizePolicy(sizePolicy)
        self.repository_path.setText("")
        self.repository_path.setObjectName("repository_path")
        self.track_row.addWidget(self.repository_path)
        self.verticalLayout_2.addLayout(self.track_row)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.events_list = QtWidgets.QListWidget(self.Tracker_tab)
        self.events_list.setObjectName("events_list")
        self.horizontalLayout_3.addWidget(self.events_list)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.MainTab.addTab(self.Tracker_tab, "")
        self.Roollback_tab = QtWidgets.QWidget()
        self.Roollback_tab.setObjectName("Roollback_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Roollback_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.choose_file = QtWidgets.QPushButton(self.Roollback_tab)
        self.choose_file.setObjectName("choose_file")
        self.verticalLayout_3.addWidget(self.choose_file)
        self.file_conditions_list = QtWidgets.QListWidget(self.Roollback_tab)
        self.file_conditions_list.setObjectName("file_conditions_list")
        self.verticalLayout_3.addWidget(self.file_conditions_list)
        self.MainTab.addTab(self.Roollback_tab, "")
        self.verticalLayout.addWidget(self.MainTab)
        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)
        self.MainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Repository:"))
        self.create_rep.setText(_translate("MainWindow", "Create"))
        self.del_rep.setText(_translate("MainWindow", "Delete"))
        self.track_dir.setText(_translate("MainWindow", "Track off"))
        self.track_settings.setText(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "Location:"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.Tracker_tab), _translate("MainWindow", "Tracker"))
        self.choose_file.setText(_translate("MainWindow", "Choose File"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.Roollback_tab), _translate("MainWindow", "Roollback"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())