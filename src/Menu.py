import customtkinter as ctk

from src.Difficulty import Difficulty
from src.JsonManager import JsonManager

class Menu:
    @staticmethod
    def menu(root):

        root.clear_container()

        title = ctk.CTkLabel(root.container, text="MINESWEEPER", font=("Arial", 65))
        title.place(relx=0.5, rely=0.2, anchor='center')

        button_frame = ctk.CTkFrame(root.container, fg_color="transparent")
        button_frame.place(relx=0.5, rely=0.55, anchor="center")

        play_button = ctk.CTkButton(
            button_frame,
            text="Play",
            font=("Arial", 20),
            width=250,
            height=70,
            command=lambda: Menu.difficulty_menu(root)
        )
        play_button.pack(pady=(0, 30))  

        score_button = ctk.CTkButton(
            button_frame,
            text="Scores",
            font=("Arial", 20),
            width=250,
            height=70,
            command=lambda: Menu.score_menu(root)
        )
        score_button.pack(pady=(0, 30))  

        if JsonManager.read_scores() == []:
            score_button.configure(fg_color="#4e4f50",state="disabled")

        quit_button = ctk.CTkButton(
            button_frame,
            text="Quit",
            font=("Arial", 20),
            width=250,
            height=70,
            command=root.exit
        )
        quit_button.pack()

    @staticmethod
    def difficulty_menu(root):

        root.clear_container()
        
        title = ctk.CTkLabel(root.container, text="MINESWEEPER", font=("Arial", 65))
        title.place(relx=0.5, rely=0.2, anchor='center')

        button_frame = ctk.CTkFrame(root.container, fg_color="transparent")
        button_frame.place(relx=0.5, rely=0.55, anchor="center")

        text = ctk.CTkLabel(button_frame, text="Choose a difficulty", font=("Arial", 30))
        text.pack(pady=(0, 40))  

        easy_button = ctk.CTkButton(
            button_frame,
            text="Easy",
            font=("Arial", 20),
            width=250,
            height=50,
            command=lambda: (Difficulty.easy(root), root.start_game())
        )
        easy_button.pack(pady=(0, 30))  

        medium_button = ctk.CTkButton(
            button_frame,
            text="Medium",
            font=("Arial", 20),
            width=250,
            height=50,
            command=lambda: (Difficulty.medium(root), root.start_game())
        )
        medium_button.pack(pady=(0, 30))  

        hard_button = ctk.CTkButton(
            button_frame,
            text="Hard",
            font=("Arial", 20),
            width=250,
            height=50,
            command=lambda: (Difficulty.hard(root), root.start_game())
        )
        hard_button.pack()

    @staticmethod
    def score_menu(root):

        root.clear_container()

        title = ctk.CTkLabel(root.container, text="Scores", font=("Arial", 50))
        title.place(relx=0.5, rely=0.1, anchor="center")

        scores = JsonManager.read_scores()

        difficulty_order = {"hard": 0, "medium": 1, "easy": 2}

        scores = sorted(
            scores,
            key=lambda s: (difficulty_order.get(s["difficulty"], 3), s["timer"])
        )

        scroll_frame = ctk.CTkScrollableFrame(root.container, width=600, height=400)
        scroll_frame.place(relx=0.5, rely=0.55, anchor="center")

        legend_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        legend_frame.pack(fill="x", pady=(0, 5), padx=10)

        ctk.CTkLabel(legend_frame, text="Rang", width=30, font=("Arial", 16, "bold")).grid(row=0, column=0, padx=5, sticky="w")
        ctk.CTkLabel(legend_frame, text="Difficulty", width=150, font=("Arial", 16, "bold")).grid(row=0, column=1, padx=5, sticky="w")
        ctk.CTkLabel(legend_frame, text="Score", width=100, font=("Arial", 16, "bold")).grid(row=0, column=2, padx=5, sticky="w")
        ctk.CTkLabel(legend_frame, text="Date", width=150, font=("Arial", 16, "bold")).grid(row=0, column=3, padx=5, sticky="w")

        for i, score in enumerate(scores, start=1):
            frame = ctk.CTkFrame(scroll_frame)
            frame.pack(fill="x", pady=5, padx=10)

            rank_label = ctk.CTkLabel(frame, text=f"{i}.", width=30)
            rank_label.grid(row=0, column=0, padx=5, sticky="w")

            difficulty_label = ctk.CTkLabel(frame, text=score["difficulty"].capitalize(), width=150)
            difficulty_label.grid(row=0, column=1, padx=5, sticky="w")

            score_label = ctk.CTkLabel(frame, text=str(score["timer"]), width=100)
            score_label.grid(row=0, column=2, padx=5, sticky="w")

            date_label = ctk.CTkLabel(frame, text=score["datetime"], width=150)
            date_label.grid(row=0, column=3, padx=5, sticky="w")

        button_frame = ctk.CTkFrame(root.container, fg_color="transparent")
        button_frame.place(relx=0.5, rely=0.91, anchor="center")

        back_button = ctk.CTkButton(
            button_frame,
            text="Back",
            font=("Arial", 20),
            width=150,
            height=50,
            command=lambda: Menu.menu(root)
        )
        back_button.pack(side="left", padx=10)

        clear_button = ctk.CTkButton(
            button_frame,
            text="Clear",
            font=("Arial", 20),
            width=150,
            height=50,
            command=lambda: (JsonManager.clear_scores(), Menu.menu(root))
        )
        clear_button.pack(side="left", padx=10)