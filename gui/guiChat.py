# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/guiChat.ui'
#
# Created: Thu Feb 26 13:56:18 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Chat(object):
    def setupUi(self, Chat):
        Chat.setObjectName(_fromUtf8("Chat"))
        Chat.resize(575, 524)
        self.groupBox = QtGui.QGroupBox(Chat)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 111, 521))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 101, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 145, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 30, 101, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.line = QtGui.QFrame(Chat)
        self.line.setGeometry(QtCore.QRect(90, 0, 21, 521))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.stackedWidget = QtGui.QStackedWidget(Chat)
        self.stackedWidget.setGeometry(QtCore.QRect(100, 0, 471, 521))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.line_2 = QtGui.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(-3, 40, 481, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.page)
        self.graphicsView_2.setGeometry(QtCore.QRect(5, 5, 43, 43))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(70, 10, 251, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 381, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_3 = QtGui.QFrame(self.page)
        self.line_3.setGeometry(QtCore.QRect(0, 440, 481, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.textEdit = QtGui.QTextEdit(self.page)
        self.textEdit.setGeometry(QtCore.QRect(0, 450, 391, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(392, 450, 81, 71))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.scrollArea = QtGui.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(0, 50, 471, 391))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 463, 383))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.listWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 471, 391))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 10, 471, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.widget)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(60, 20, 401, 18))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.widget_2 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setGeometry(QtCore.QRect(0, 80, 471, 61))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.graphicsView_4 = QtGui.QGraphicsView(self.widget_2)
        self.graphicsView_4.setGeometry(QtCore.QRect(420, 10, 41, 41))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 401, 18))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(80, 180, 256, 81))
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 40))
        self.textBrowser.setSizeIncrement(QtCore.QSize(0, 10))
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Chat)
        QtCore.QMetaObject.connectSlotsByName(Chat)

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(_translate("Chat", "聊天", None))
        self.groupBox.setTitle(_translate("Chat", "GroupBox", None))
        self.pushButton.setText(_translate("Chat", "稻草人", None))
        self.pushButton_2.setText(_translate("Chat", "小曾子", None))
        self.label.setText(_translate("Chat", "稻草人(28762822)", None))
        self.label_2.setText(_translate("Chat", "[在线]悄悄是别离的生肖。。。。。", None))
        self.pushButton_3.setText(_translate("Chat", "发送", None))
        self.label_3.setText(_translate("Chat", "你好啊！", None))
        self.label_4.setText(_translate("Chat", "你好啊！", None))
        self.textBrowser.setHtml(_translate("Chat", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'WenQuanYi Micro Hei\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">你好啊,<img src=\"/home/younfor/project/PyLinuxQQ/tmp/head/qq.jpg\" />,嘿嘿</p></body></html>", None))

