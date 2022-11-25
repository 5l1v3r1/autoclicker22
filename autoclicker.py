from PyQt5 import QtWidgets
import sys
from ui import Ui
from buttons import Buttons
from pynput import keyboard
from pynput.keyboard import KeyCode

buttons = Buttons()

buttons.createThreads()

def on_press(key):
	if key == KeyCode.from_char(buttons.leftButton.settings["hotkey"]):
		buttons.leftButton.hold = True
		buttons.leftButton.on = not buttons.leftButton.on
	elif key == KeyCode.from_char(buttons.rightButton.settings["hotkey"]):
		buttons.rightButton.hold = True
		buttons.rightButton.on = not buttons.rightButton.on

def on_release(key):
	if key == KeyCode.from_char(buttons.leftButton.settings["hotkey"]):
		buttons.leftButton.hold = False
	elif key == KeyCode.from_char(buttons.rightButton.settings["hotkey"]):
		buttons.rightButton.hold = False

listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()

app = QtWidgets.QApplication(sys.argv)
window = Ui(buttons.leftButton.handler, buttons.rightButton.handler)
app.exec_()
buttons.stopThreads()