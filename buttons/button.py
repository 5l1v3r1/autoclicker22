import json
from pynput.mouse import Controller


class Button():
	def __init__(self, btn, name):
		self.name = name
		self.btn = btn
		self.settings = self.get_settings() 
		self.mouse = Controller()

	def get_settings(self):
		with open("./settings.json", "r") as f:
			settings = json.loads(f.read())[self.name]
			f.close()
		return settings

	def click(self):
		self.mouse.click(self.btn, 1)

	def double_click(self):
		self.mouse.click(self.btn, 2)

	def save_settings(self):
		with open("./settings.json", "r") as f:
			settings = json.loads(f.read())
			f.close()
		
		settings[self.name] = self.settings

		with open("./settings.json", "w") as f:
			f.write(json.dumps(settings))
			f.close()
