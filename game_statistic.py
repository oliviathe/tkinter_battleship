from datetime import datetime
import json


class Game_Statistic:

	def __init__(self):
		self.win = False
		self.score = 200
		self.steps = 0
		self.start_time = ""
		self.finish_time = ""
		self.game_time = ""

	def reset_gameStat(self):
		self.win = False
		self.score = 200
		self.steps = 0
		self.start_time = ""
		self.finish_time = ""
		self.game_time = ""

	def get_current_time(self):
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")

	def get_game_time(self):
		#start_time = self.game.start_time
		#finish_time = self.game.finish_time
		start_hour, start_minute, start_sec = self.start_time.split(":")
		finish_hour, finish_minute, finish_sec = self.finish_time.split(":")

		total_start_time = start_hour*24 + start_minute*60 + start_sec
		total_finish_time = finish_hour*24 + finish_minute*60 + finish_sec

		if total_start_time > total_finish_time:
			total_game_time = total_start_time - total_finish_time
		else:
			total_game_time = total_finish_time - total_start_time

		game_hour = total_game_time//24
		left_time = total_game_time%24
		game_minute = left_time//60
		game_second = left_time%60

		self.game_time = f"{game_hour}:{game_minute}:{game_second}"