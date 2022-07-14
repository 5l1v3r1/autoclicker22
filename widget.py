from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self, leftHandler, rightHandler):
        super(Ui, self).__init__()
        uic.loadUi('form.ui', self)
        self.show()

        self.setMinimumWidth(424)
        self.setMinimumHeight(328)
        self.setMaximumWidth(424)
        self.setMaximumHeight(328)
        self.setWindowTitle("Autoclicker")

        #spinbox
        self.leftSB.setMinimum(0)
        self.rightSB.setMinimum(0)
        self.leftSB.setMaximum(70)
        self.rightSB.setMaximum(70)

        self.leftSB.setValue(leftHandler.btn.settings["cps"])
        self.rightSB.setValue(rightHandler.btn.settings["cps"])

        self.leftSB.valueChanged.connect(leftHandler.set_cps)
        self.rightSB.valueChanged.connect(rightHandler.set_cps)

        #slide
        self.leftSlide.valueChanged.connect(leftHandler.set_random)
        self.rightSlide.valueChanged.connect(rightHandler.set_random)

        self.leftSlide.setValue(leftHandler.btn.settings["random"])
        self.rightSlide.setValue(rightHandler.btn.settings["random"])

        #checkbox1
        self.left1CB.stateChanged.connect(leftHandler.set_hold)
        self.right1CB.stateChanged.connect(rightHandler.set_hold)

        if leftHandler.btn.settings["hold"]:
            self.left1CB.setCheckState(2)
        else:
            self.left1CB.setCheckState(0)

        if rightHandler.btn.settings["hold"]:
            self.right1CB.setCheckState(2)
        else:
            self.right1CB.setCheckState(0)

        #checkbox2
        self.left2CB.stateChanged.connect(leftHandler.set_double)
        self.right2CB.stateChanged.connect(rightHandler.set_double)

        if leftHandler.btn.settings["double"]:
            self.left2CB.setCheckState(2)
        else:
            self.left2CB.setCheckState(0)

        if rightHandler.btn.settings["double"]:
            self.right2CB.setCheckState(2)
        else:
            self.right2CB.setCheckState(0)

        #lineEdit
        self.leftHotkey.setMaxLength(10)
        self.rightHotkey.setMaxLength(10)
        self.leftHotkey.textChanged.connect(leftHandler.set_key)
        self.rightHotkey.textChanged.connect(rightHandler.set_key)

        self.leftHotkey.setText(leftHandler.btn.settings["hotkey"])
        self.rightHotkey.setText(rightHandler.btn.settings["hotkey"])