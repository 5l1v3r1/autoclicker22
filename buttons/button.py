import json
from pynput.mouse import Controller
import random
from buttons.handler import Handler
from os import path


class Button():
	def __init__(self, btn, name):
		self.name = name
		self.btn = btn
		self.settings = self.get_settings() 
		self.mouse = Controller()
		self.on = False
		self.hold = False
		self.thread = None
		self.handler = Handler(self)

	def check_settings(self):
		if not path.exists("./settings.json") or not path.isfile("./settings.json"):
			f = open("./settings.json", "w")
			default = {"left": {"cps": 1, "random": 0, "hold": False, "hotkey": "h"}, "right": {"cps": 1, "random": 0, "hold": False, "hotkey": "j"}}
			f.write(json.dumps(default))
			f.close()

	def get_settings(self):
		self.check_settings()
		with open("./settings.json", "r") as f:
			settings = json.loads(f.read())[self.name]
			f.close()
		return settings

	def click(self):
		self.mouse.click(self.btn, 1)

	def save_settings(self):
		self.check_settings()
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

			if cps > 5:
				count = random.randint(-5,5)
			elif cps < 5 and cps != 1:
				count = random.randint(-5,5)
			else:
				count = random.randint(0,5)

			base = random.randint(0,110)
			randomiz = self.settings["random"]

			if randomiz > base:
				return cps + count
			else:
				return cps