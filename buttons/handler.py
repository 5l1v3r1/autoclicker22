class Handler:
	def __init__(self, btn):
		self.btn = btn

	def set_cps(self, cps):
		self.btn.settings["cps"] = cps
		self.btn.save_settings()

	def set_random(self, random):
		self.btn.settings["random"] = random
		self.btn.save_settings()

	def set_hold(self, state):
		if state == 2:
			self.btn.settings["hold"] = True
		else:
			self.btn.settings["hold"] = False
		self.btn.save_settings()

	def set_key(self, char):
		self.btn.settings["hotkey"] = char
		self.btn.save_settings()