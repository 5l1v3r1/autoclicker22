from buttons import button
from pynput.mouse import Button

class RightButton(button.Button):
	def __init__(self):
		super().__init__(Button.right, "right")