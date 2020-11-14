# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(820, 636)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(70, 340, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(54, 250, 101, 20))
        self.le_step = QLineEdit(Dialog)
        self.le_step.setObjectName(u"le_step")
        self.le_step.setGeometry(QRect(210, 240, 113, 22))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 290, 151, 20))
        self.le_file_type = QLineEdit(Dialog)
        self.le_file_type.setObjectName(u"le_file_type")
        self.le_file_type.setGeometry(QRect(210, 280, 113, 22))
        self.pb_run = QPushButton(Dialog)
        self.pb_run.setObjectName(u"pb_run")
        self.pb_run.setGeometry(QRect(630, 60, 93, 28))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 521, 161))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.le_dir = QLineEdit(self.verticalLayoutWidget)
        self.le_dir.setObjectName(u"le_dir")

        self.horizontalLayout.addWidget(self.le_dir)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pb_dir = QPushButton(self.verticalLayoutWidget)
        self.pb_dir.setObjectName(u"pb_dir")

        self.horizontalLayout.addWidget(self.pb_dir)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.le_first_file = QLineEdit(self.verticalLayoutWidget)
        self.le_first_file.setObjectName(u"le_first_file")

        self.horizontalLayout_2.addWidget(self.le_first_file)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.le_prefix = QLineEdit(self.verticalLayoutWidget)
        self.le_prefix.setObjectName(u"le_prefix")

        self.horizontalLayout_3.addWidget(self.le_prefix)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.le_file_number = QLineEdit(self.verticalLayoutWidget)
        self.le_file_number.setObjectName(u"le_file_number")

        self.horizontalLayout_4.addWidget(self.le_file_number)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Choose step", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Choose file type", None))
        self.pb_run.setText(QCoreApplication.translate("Dialog", u"Power", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select Directory Path", None))
        self.pb_dir.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Choose First File", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Choose File Name", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Choose number to numerate", None))
    # retranslateUi

