# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from client.images import draw_all
from client.array import Array_Form
from client.sub_array import SubArray_Form
from utils.message_box import *


class Antenna():
    def __init__(self):
        self.arrayWin = Array_Form()
        self.arrayExc = QtWidgets.QWidget()
        self.arrayWin.setupUi(Form=self.arrayExc)
        self.arrayWin.retranslateUi(Form=self.arrayExc)

        self.arrayWin.pushButton1.clicked.connect(self.arrayWin.confirm_input)

    def show(self):
        self.arrayExc.show()


class SubAntenna():
    def __init__(self, xy):
        self.arrayWin = SubArray_Form(xy=xy)
        self.arrayExc = QtWidgets.QWidget()
        self.arrayWin.setupUi(Form=self.arrayExc)
        self.arrayWin.retranslateUi(Form=self.arrayExc)

    def show(self):
        self.arrayExc.show()


class Setting_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(298, 218)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setStyleSheet("font-size:17px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font-size:17px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("font-size:17px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font-size:17px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("font-size:17px;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("font-size:17px;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout_3.addWidget(self.lineEdit_1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 保存阵列
        self.antennas = None
        self.sub_antenna = None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "天线尺寸："))
        self.label_3.setText(_translate("Form", "阵元数目："))
        self.label_4.setText(_translate("Form", "副瓣天平："))
        self.label_5.setText(_translate("Form", "阵元间距："))
        self.label_6.setText(_translate("Form", "阵元波长："))
        self.label_7.setText(_translate("Form", "波束宽度："))
        self.label_2.setText(_translate("Form", "X"))
        self.pushButton_2.setText(_translate("Form", "确定"))
        self.pushButton_3.setText(_translate("Form", "取消"))

    # 确认手动输入的设置
    def confirm_input(self, init):
        # 获取输入字符
        self.text1 = self.lineEdit_1.text()
        self.text2 = self.lineEdit_2.text()
        self.text3 = self.lineEdit_3.text()
        self.text4 = self.lineEdit_4.text()
        self.text5 = self.lineEdit_5.text()
        self.text6 = self.lineEdit_6.text()
        self.text7 = self.lineEdit_7.text()
        # 检查天线尺寸设置是否正确
        if self.text1 != '' and self.text2 != '':
            check_size((self.text1, self.text2))
        # 设置显示字符
        self.lineEdit_1.setText(self.text1)
        self.lineEdit_2.setText(self.text2)
        self.lineEdit_3.setText(self.text3)
        self.lineEdit_4.setText(self.text4)
        self.lineEdit_5.setText(self.text5)
        self.lineEdit_6.setText(self.text6)
        self.lineEdit_7.setText(self.text7)
        # 初始化阵列
        self.initialize_antenna()
        # 弹出提示框
        QtWidgets.QMessageBox.information(None, '操作成功', '参数设置成功')
        init.stat = True
        # 提前画出所有参数有更改的图
        draw_all()

    # 导入文件输入的设置
    def loadSet(self, settings):
        # 获取输入字符
        self.text1 = settings[0]
        self.text2 = settings[1]
        self.text3 = settings[2]
        self.text4 = settings[3]
        self.text5 = settings[4]
        self.text6 = settings[5]
        self.text7 = settings[6]

        # 设置显示字符
        self.lineEdit_1.setText(self.text1)
        self.lineEdit_2.setText(self.text2)
        self.lineEdit_3.setText(self.text3)
        self.lineEdit_4.setText(self.text4)
        self.lineEdit_5.setText(self.text5)
        self.lineEdit_6.setText(self.text6)
        self.lineEdit_7.setText(self.text7)
        # 检查天线尺寸设置是否正确
        if self.text1 != '' and self.text2 != '':
            check_size((self.text1, self.text2))

    def initialize_antenna(self):
        size = (self.text1, self.text2)
        if size == ('8', '8'):
            areas = [(534, 651, 260, 376)]
            antennas = [Antenna() for _ in range(len(areas))]
            self.antennas = (areas, antennas)
            self.sub_antenna = SubAntenna(size)

        if size == ('8', '16'):
            areas = [(384, 500, 327, 444), (684, 802, 327, 444)]
            antennas = [Antenna() for _ in range(len(areas))]
            self.antennas = (areas, antennas)
            self.sub_antenna = SubAntenna(size)

        if size == ('8', '32'):
            areas = [(79, 199, 341, 459), (381, 500, 341, 459), (683, 800, 341, 459), (985, 1100, 341, 459)]
            antennas = [Antenna() for _ in range(len(areas))]
            self.antennas = (areas, antennas)
            self.sub_antenna = SubAntenna(size)

        if size == ('16', '16'):
            areas = [(381, 500, 165, 279), (682, 801, 165, 279), (381, 500, 415, 531), (381, 500, 415, 531)]
            antennas = [Antenna() for _ in range(len(areas))]
            self.antennas = (areas, antennas)
            self.sub_antenna = SubAntenna(size)

        if size == ('16', '32'):
            areas = [(80, 199, 200, 317), (384, 501, 200, 317), (684, 803, 200, 317), (987, 1103, 200, 317)
                , (80, 199, 449, 566), (384, 501, 449, 566), (684, 803, 449, 566), (987, 1103, 449, 566)]
            antennas = [Antenna() for _ in range(len(areas))]
            self.antennas = (areas, antennas)
            self.sub_antenna = SubAntenna(size)

        if size == ('16', '64'):
            areas = [(37, 96, 281, 341), (186, 246, 281, 341), (337, 395, 281, 341), (487, 546, 281, 341),
                     (636, 694, 281, 341), (786, 844, 281, 341), (935, 994, 281, 341), (1086, 1143, 281, 341)
                , (37, 96, 405, 464), (186, 246, 405, 464), (337, 395, 405, 464), (487, 546, 405, 464),
                     (636, 694, 405, 464), (786, 844, 405, 464), (935, 994, 405, 464), (1086, 1143, 405, 464)]
            antennas = [Antenna() for _ in range(len(areas))]
            self.antennas = (areas, antennas)
            self.sub_antenna = SubAntenna(size)

        if size == ('32', '32'):
            areas = [(264, 340, 59, 133), (458, 533, 59, 133), (650, 726, 59, 133), (843, 919, 59, 133)
                , (264, 340, 218, 296), (458, 533, 218, 296), (650, 726, 218, 296), (843, 919, 218, 296)
                , (264, 340, 377, 452), (458, 533, 377, 452), (650, 726, 377, 452), (843, 919, 377, 452)
                , (264, 340, 537, 610), (458, 533, 537, 610), (650, 726, 537, 610), (843, 919, 537, 610)]
            antennas = [Antenna() for _ in range(len(areas))]
            self.antennas = (areas, antennas)
            self.sub_antenna = SubAntenna(size)

        if size == ('32', '64'):
            areas = [(77, 131, 153, 209), (217, 271, 153, 209), (357, 410, 153, 209), (494, 549, 153, 209),
                     (634, 689, 153, 209), (772, 826, 153, 209), (912, 966, 153, 209), (1051, 1105, 153, 209)
                , (77, 131, 270, 323), (217, 271, 270, 323), (357, 410, 270, 323), (494, 549, 270, 323),
                     (634, 689, 270, 323), (772, 826, 270, 323), (912, 966, 270, 323), (1051, 1105, 270, 323)
                , (77, 131, 382, 436), (217, 271, 382, 436), (357, 410, 382, 436), (494, 549, 382, 436),
                     (634, 689, 382, 436), (772, 826, 382, 436), (912, 966, 382, 436), (1051, 1105, 382, 436)
                , (77, 131, 487, 551), (217, 271, 487, 551), (357, 410, 487, 551), (494, 549, 487, 551),
                     (634, 689, 487, 551), (772, 826, 487, 551), (912, 966, 487, 551), (1051, 1105, 487, 551)]
            antennas = [Antenna() for _ in range(len(areas))]
            self.antennas = (areas, antennas)
            self.sub_antenna = SubAntenna(size)

        if size == ('64', '64'):
            areas = [(249, 285, 38, 74), (341, 378, 38, 74), (433, 470, 38, 74), (527, 564, 38, 74), (620, 655, 38, 74),
                     (713, 748, 38, 74), (806, 841, 38, 74), (898, 934, 38, 74)
                , (249, 285, 115, 151), (341, 378, 115, 151), (433, 470, 115, 151), (527, 564, 115, 151),
                     (620, 655, 115, 151), (713, 748, 115, 151), (806, 841, 115, 151), (898, 934, 115, 151)
                , (249, 285, 191, 227), (341, 378, 191, 227), (433, 470, 191, 227), (527, 564, 191, 227),
                     (620, 655, 191, 227), (713, 748, 191, 227), (806, 841, 191, 227), (898, 934, 191, 227)
                , (249, 285, 268, 303), (341, 378, 268, 303), (433, 470, 268, 303), (527, 564, 268, 303),
                     (620, 655, 268, 303), (713, 748, 268, 303), (806, 841, 268, 303), (898, 934, 268, 303)
                , (249, 285, 343, 380), (341, 378, 343, 380), (433, 470, 343, 380), (527, 564, 343, 380),
                     (620, 655, 343, 380), (713, 748, 343, 380), (806, 841, 343, 380), (898, 934, 343, 380)
                , (249, 285, 420, 456), (341, 378, 420, 456), (433, 470, 420, 456), (527, 564, 420, 456),
                     (620, 655, 420, 456), (713, 748, 420, 456), (806, 841, 420, 456), (898, 934, 420, 456)
                , (249, 285, 498, 533), (341, 378, 498, 533), (433, 470, 498, 533), (527, 564, 498, 533),
                     (620, 655, 498, 533), (713, 748, 498, 533), (806, 841, 498, 533), (898, 934, 498, 533)
                , (249, 285, 574, 610), (341, 378, 574, 610), (433, 470, 574, 610), (527, 564, 574, 610),
                     (620, 655, 574, 610), (713, 748, 574, 610), (806, 841, 574, 610), (898, 934, 574, 610)]
            antennas = [Antenna() for _ in range(len(areas))]
            self.antennas = (areas, antennas)
            self.sub_antenna = SubAntenna(size)
