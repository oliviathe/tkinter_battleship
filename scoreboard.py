import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ScoreBoard(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="alice blue")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)


		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="alice blue")
		self.main_frame.pack(expand=True)

		#LOGO
		image = Image.open(self.config.scoreboard_logo_path)
		image_w, image_h = image.size
		ratio = image_w/self.config.side
		image = image.resize((int(image_w//ratio),int(image_h//ratio)))

		self.scoreboard_logo = ImageTk.PhotoImage(image)
		self.label_scoreboard_logo = tk.Label(self.main_frame, image=self.scoreboard_logo)
		self.label_scoreboard_logo.pack(side="top", padx=10, pady=30)


		#SCOREBOARD TREEVIEW
		self.scroll_scoreboard = ttk.Scrollbar(self)
		self.scroll_scoreboard.pack(side="right", fill="y")

		self.scoreboard_tree = ttk.Treeview(self)
		self.scoreboard_tree['columns'] = ("Player", "Score", "Steps", "Time")
		
		self.scoreboard_tree.column("#0", width=35, minwidth=35)
		self.scoreboard_tree.column("Player", width=325, minwidth=325)
		self.scoreboard_tree.column("Score", width=220, minwidth=220)
		self.scoreboard_tree.column("Steps", width=220, minwidth=220)
		#self.scoreboard_tree.column("Time", width=170, minwidth=170)

		self.scoreboard_tree.heading("#0", text="No.")
		self.scoreboard_tree.heading("Player", text="Player")
		self.scoreboard_tree.heading("Score", text="Score")
		self.scoreboard_tree.heading("Steps", text="Steps")
		#self.scoreboard_tree.heading("Time", text="Time")

		self.scoreboard_number=1
		self.scoreboard_iid=0

		self.scoreboard_tree.pack()

		self.scoreboard_tree.configure(yscrollcommand=self.scroll_scoreboard.set)
		self.scroll_scoreboard.configure(command=self.scoreboard_tree.yview)

		gameData = self.config.gameData

		for data in gameData:
			self.scoreboard_tree.insert(parent='', index="end", iid=(self.scoreboard_iid), text=(self.scoreboard_number), values=(gameData[data]['name'], gameData[data]['score'], gameData[data]['steps']))
			self.scoreboard_iid+=1
			self.scoreboard_number+=1


		#BUTTON
		self.btn_play = tk.Button(self.main_frame, text="Play", font=("Monaco", 22, "bold"), command=lambda:self.game.create_board())
		self.btn_play.pack(side="left", padx=(190,10), pady=(30,0))

		self.btn_mainMenu = tk.Button(self.main_frame, text="Main Menu", font=("Monaco", 22, "bold"), command=lambda:self.game.change_page('mainMenu'))
		self.btn_mainMenu.pack(side="left", padx=10,  pady=(30,0))

		self.btn_exit = tk.Button(self.main_frame, text="Exit", font=("Monaco", 22, "bold"), command=lambda:self.game.exit())
		self.btn_exit.pack(side="left", padx=(10,190), pady=(30,0))
