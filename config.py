import json
from tkinter import messagebox as msg


class Config:

	def __init__(self):

		self.app_title = "Battleship"

		#GAME CONFIG
		self.row = 5
		self.column = 5

		#WINDOW CONFIG
		base = 130
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+500"


		#IMG BUTTON PATH
		self.init_img_btn = "img/init_img.jfif"
		self.final_img_btn = "img/final_img.jfif"
		self.win_img_btn = "img/win_img.jfif"

		#LOGO PATH
		self.logo_path = "img/logo.jpg"
		self.main_menu_logo_path = "img/main_menu_logo.jpg"
		self.scoreboard_logo_path = "img/scoreboard_logo.jpg"

		#DATA CONFIG
		self.users_path = "json/users.json"
		self.gameData_path = "json/gameData.json"
		self.gameData_counter_path = "json/gameData_counter.json"
		self.howToPlay_path = "json/howToPlay.json"
		self.aboutGame_path = "json/aboutGame.json"

		self.users = self.load_userData(self.users_path)
		self.gameData = self.load_gameData(self.gameData_path)
		self.gameData_counter = self.load_gameData_counter(self.gameData_counter_path)
		self.howToPlay = self.load_howToPlay(self.howToPlay_path)
		self.aboutGame = self.load_aboutGame(self.aboutGame_path)

	def load_userData(self, users_path):
		with open(users_path, "r") as json_data:
			userData = json.load(json_data)
		return userData

	def save_userData(self, users_path):
		with open(users_path, 'w') as json_data:
			json.dump(self.users, json_data)

	def load_gameData(self, gameData_path):
		with open(self.gameData_path, "r") as json_data:
			gameData = json.load(json_data)
		return gameData

	def save_gameData(self, gameData_path):
		with open(self.gameData_path, "w") as json_data:
			json.dump(self.gameData, json_data)

	def load_gameData_counter(self, gameData_counter_path):
		with open(self.gameData_counter_path, "r") as json_data:
			gameData_counter = json.load(json_data)
		return gameData_counter

	def save_gameData_counter(self, gameData_counter_path):
		with open(self.gameData_counter_path, "w") as json_data:
			json.dump(self.gameData_counter, json_data)

	def load_howToPlay(self, howToPlay_path):
		with open(self.howToPlay_path, "r") as json_data:
			howToPlay = json.load(json_data)
		return howToPlay

	def load_aboutGame(self, aboutGame_path):
		with open(self.aboutGame_path, "r") as json_data:
			aboutGame = json.load(json_data)
		return aboutGame

	def login(self, username, password):
		if username in self.users:
			if password == self.users[username]["password"]:
				return True
			else:
				msg.showerror("Login Error", "Password is wrong")
				return False
		else:
			msg.showerror("Login Error", "Username does not exist")
			return False