from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self, leftHandler, rightHandler):
        super(Ui, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.show()

        self.setMinimumWidth(419)
        self.setMinimumHeight(333)
        self.setMaximumWidth(419)
        self.setMaximumHeight(333)
        self.setWindowTitle("Autoclicker - Github/ngn13")

        #spinbox
        self.leftSB.setMinimum(1)
        self.rightSB.setMinimum(1)
        self.leftSB.setMaximum(200)
        self.rightSB.setMaximum(200)

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

        #lineEdit
        self.leftHotkey.setMaxLength(10)
        self.rightHotkey.setMaxLength(10)
        self.leftHotkey.textChanged.connect(leftHandler.set_key)
        self.rightHotkey.textChanged.connect(rightHandler.set_key)

        self.leftHotkey.setText(leftHandler.btn.settings["hotkey"])
        self.rightHotkey.setText(rightHandler.btn.settings["hotkey"])