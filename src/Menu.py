import customtkinter as ctk

class Menu:
    @staticmethod
    def menu(frame):

        title = ctk.CTkLabel(frame, text="MINESWEEPER", font=("Arial", 65))
        title.place(relx=0.5, rely=0.2, anchor='center')

        button_frame = ctk.CTkFrame(frame, fg_color="transparent")
        button_frame.place(relx=0.5, rely=0.55, anchor="center")

        play_button = ctk.CTkButton(
            button_frame,
            text="Jouer",
            font=("Arial", 20),
            width=250,
            height=70
        )
        play_button.pack(pady=(0, 60))  

        quit_button = ctk.CTkButton(
            button_frame,
            text="Quitter",
            font=("Arial", 20),
            width=250,
            height=70,
            command=lambda: quit()
        )
        quit_button.pack()
