import tkinter as tk
import sys
from tkinter import messagebox as msg

from config import Config
from game_statistic import Game_Statistic
from ship import Ship
from player import Player
from board import Board
from loginPage import LoginPage
from scoreboard import ScoreBoard
from main_menu import MainMenu
from info import InfoPage
from registerPage import RegisterPage


class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config
		self.game_statistic = Game.game_statistic
		self.ship = Game.ship

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)
		self.create_container()
		self.pages = {}
		self.create_scoreBoard()
		self.create_infoPage()
		self.create_mainMenu()
		self.create_registerPage()
		self.create_loginPage()

	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)
		self.ship.generate_answer()
		#self.start_time = self.game_statistic.get_current_time()

	def create_loginPage(self):
		self.pages['loginPage'] = LoginPage(self.container, self)

	def create_registerPage(self):
		self.pages['registerPage'] = RegisterPage(self.container, self)

	def create_mainMenu(self):
		self.pages['mainMenu'] = MainMenu(self.container, self)

	def create_scoreBoard(self):
		self.pages['scoreBoard'] = ScoreBoard(self.container, self)

	def create_infoPage(self):
		self.pages['infoPage'] = InfoPage(self.container, self)


	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def auth_login(self):
		username = self.pages['loginPage'].var_username.get()
		password = self.pages['loginPage'].var_password.get()

		granted = self.config.login(username, password)
		if granted:
			self.change_page('mainMenu')

	def clicked_save_register_btn(self):
		confirm = msg.askyesnocancel('Save Confirmation', 'Are you sure to register this account?')
			
		if confirm:
			registered_username = self.pages['registerPage'].var_register_username.get()
			registered_password = self.pages['registerPage'].var_register_password.get()

			if registered_username in self.config.users:
				msg.showerror("Registration Error", "Username already exists")
				self.create_registerPage
			elif len(registered_username) == 0:
				msg.showerror("Registration Error", "Username can't be empty")
				self.create_registerPage()
			elif len(registered_password) == 0:
				msg.showerror("Registration Error", "Password can't be empty")
				self.create_registerPage()
			else:
				new_acc = {
					registered_username : {
             	     "password" : registered_password
            		}
        		}

				self.config.users.update(new_acc)
				self.config.save_userData(self.config.users_path)
				self.change_page('mainMenu')

	def insert_data(self):
		player_name_from_login = self.pages['loginPage'].var_username.get()
		player_name_from_register = self.pages['registerPage'].var_register_username.get()
		player_name = ""
		if len(player_name_from_login) == 0:
			player_name = player_name_from_register
		else:
			player_name = player_name_from_login
		self.config.gameData_counter+=1

		self.pages['scoreBoard'].scoreboard_tree.insert(parent='', index='end', iid=(self.pages['scoreBoard'].scoreboard_iid), text=(self.pages['scoreBoard'].scoreboard_number), values=(player_name, self.game_statistic.score, self.game_statistic.steps))
		self.pages['scoreBoard'].scoreboard_iid = self.pages['scoreBoard'].scoreboard_iid+1
		self.pages['scoreBoard'].scoreboard_number = self.pages['scoreBoard'].scoreboard_number+1

		gameData_label = f"data{self.config.gameData_counter}"

		self.config.gameData[gameData_label] = {
			"name" : player_name,
			"score" : self.game_statistic.score,
			"steps" : self.game_statistic.steps
		}

		self.config.save_gameData(self.config.gameData_path)
		self.config.save_gameData_counter(self.config.gameData_counter)

	def exit(self):
		confirm = msg.askyesnocancel('Exit Confirmation', 'Are you sure to exit?')
		if confirm:
			sys.exit()
		else:
			self.change_page('mainMenu')


class Battleship:

	def __init__(self):
		self.config = Config()
		self.game_statistic = Game_Statistic()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			self.game_statistic.steps+=1
			#self.finish_time = self.game_statistic.get_current_time()
			return True
		else:
			self.game_statistic.steps+=1
			self.game_statistic.score+= -4
			return False

	def button_clicked(self, pos_x, pos_y):
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.window.pages['board'].change_img_button(pos_x, pos_y, win)
		if win:
			print("You Win!!!")
			self.window.insert_data()
			#self.game_statistic.get_game_time()
			#print(self.game_statistic.game_time)
			self.game_statistic.reset_gameStat()
			self.window.change_page('scoreBoard')

	def run(self):
		self.window.mainloop()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()