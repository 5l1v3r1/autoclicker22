from buttons import button
from pynput.mouse import Button

class LeftButton(button.Button):
	def __init__(self):
		super().__init__(Button.left, "left")