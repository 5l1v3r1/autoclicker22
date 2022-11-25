from buttons.left import LeftButton
from buttons.right import RightButton
from threading import Thread
import time

class Buttons:
	def __init__(self):
		self.leftButton = LeftButton()
		self.rightButton = RightButton()
		self.threadState = False

	def buttonThread(self, button):
		while not self.threadState:
			if button.settings["hold"]:
				if button.hold:
					button.click()

			else:
				if button.on:
					button.click()

			time.sleep(1/button.get_cps())

	def createThreads(self):
		# create the threads
		self.leftButton.thread = Thread(target=self.buttonThread, args=(self.leftButton,))
		self.rightButton.thread = Thread(target=self.buttonThread, args=(self.rightButton,))
		# start them
		self.leftButton.thread.start()
		self.rightButton.thread.start()
		# wow thats some epic commenting

	def stopThreads(self):
		self.threadState = True
		self.leftButton.thread.join()
		self.rightButton.thread.join()
		
			

