# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Activitat 1 - Apartat 2 - formulari de text I.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(509, 468)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.copiar = QPushButton(Form)
        self.copiar.setObjectName(u"copiar")

        self.horizontalLayout.addWidget(self.copiar)

        self.cortar = QPushButton(Form)
        self.cortar.setObjectName(u"cortar")

        self.horizontalLayout.addWidget(self.cortar)

        self.pegar = QPushButton(Form)
        self.pegar.setObjectName(u"pegar")

        self.horizontalLayout.addWidget(self.pegar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.seleccionar_todo = QPushButton(Form)
        self.seleccionar_todo.setObjectName(u"seleccionar_todo")

        self.horizontalLayout_2.addWidget(self.seleccionar_todo)

        self.eliminar = QPushButton(Form)
        self.eliminar.setObjectName(u"eliminar")

        self.horizontalLayout_2.addWidget(self.eliminar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)
        self.copiar.clicked.connect(self.textEdit.copy)
        self.cortar.clicked.connect(self.textEdit.cut)
        self.pegar.clicked.connect(self.textEdit.paste)
        self.seleccionar_todo.clicked.connect(self.textEdit.selectAll)
        self.eliminar.clicked.connect(self.textEdit.clear)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">TextLabel</span></p></body></html>", None))
        self.copiar.setText(QCoreApplication.translate("Form", u"Copiar", None))
        self.cortar.setText(QCoreApplication.translate("Form", u"Cortar", None))
        self.pegar.setText(QCoreApplication.translate("Form", u"Pegar", None))
        self.seleccionar_todo.setText(QCoreApplication.translate("Form", u"Seleccionar todo", None))
        self.eliminar.setText(QCoreApplication.translate("Form", u"Eliminar texto", None))
    # retranslateUi

