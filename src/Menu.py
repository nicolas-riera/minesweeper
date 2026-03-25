import customtkinter as ctk

from src.Difficulty import Difficulty

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
        play_button.pack(pady=(0, 60))  

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