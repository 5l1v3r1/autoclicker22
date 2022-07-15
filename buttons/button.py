import json
from pynput.mouse import Controller
import random


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

	def get_cps(self):
		if self.settings["random"] == 0:
			return self.settings["cps"]
		else:
			cps = self.settings["cps"]
			if cps > 3:
				count = random.randint(-3,3)
			elif cps < 3 and cps != 1:
				count = random.randint(-1,3)
			else:
				count = random.randint(0,3)
			base = random.randint(0,110)
			randomiz = self.settings["random"]

			if randomiz > base:
				return cps + count
			else:
				return cps