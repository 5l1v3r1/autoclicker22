from PyQt5 import QtWidgets
import sys
from widget import Ui
from buttons import handler, left, right
import threading
from pynput import keyboard
from pynput.keyboard import KeyCode
import time

leftBtn = left.LeftButton();
rightBtn = right.RightButton();

leftHandler = handler.Handler(leftBtn)
rightHandler = handler.Handler(rightBtn)

leftState = False
rightState = False
leftHold = False
rightHold = False

thread_stop = False

def click_btn(btn):
	while not thread_stop:
		if btn.name == "left":
			if btn.settings["hold"]:
				if leftHold:
						if btn.settings["double"]:
							btn.double_click()
						else:
							btn.click()
			else:
				if leftState:	
					if btn.settings["double"]:
							btn.double_click()
					else:
						btn.click()
			time.sleep(1/btn.get_cps())

		elif btn.name == "right":
			if btn.settings["hold"]:
				if rightHold:
						if btn.settings["double"]:
							btn.double_click()
						else:
							btn.click()
			else:
				if rightState:	
					if btn.settings["double"]:
							btn.double_click()
					else:
						btn.click()
			time.sleep(1/btn.get_cps())

			

def on_press(key):
	global leftHold
	global rightHold
	global leftState
	global rightState
	if key == KeyCode.from_char(leftBtn.settings["hotkey"]):
		leftHold = True
		leftState = not leftState
	elif key == KeyCode.from_char(rightBtn.settings["hotkey"]):
		rightHold = True
		rightState = not rightState

def on_release(key):
	global leftHold
	global rightHold
	if key == KeyCode.from_char(leftBtn.settings["hotkey"]):
		leftHold = False
	elif key == KeyCode.from_char(rightBtn.settings["hotkey"]):
		rightHold = False

listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()

leftThread = threading.Thread(target=click_btn, args=(leftBtn,))
rightThread = threading.Thread(target=click_btn, args=(rightBtn,))
leftThread.start()
rightThread.start()

app = QtWidgets.QApplication(sys.argv)
window = Ui(leftHandler, rightHandler)
app.exec_()
thread_stop = True
leftThread.join()
rightThread.join()
