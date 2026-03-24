import customtkinter as ctk


class GameRendering:

    @staticmethod
    def game_rendering(game):
        game.ui_frame = ctk.CTkFrame(game.root.container, fg_color="transparent")
        game.ui_frame.pack(side="top", fill="x", padx=10, pady=5)

        game.grid_frame = ctk.CTkFrame(game.root.container, fg_color="transparent")
        game.grid_frame.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        GameRendering.ui_rendering(game)
        GameRendering.grid_rendering(game)

    @staticmethod
    def ui_rendering(game):

        exit_button = ctk.CTkButton(
            game.ui_frame,
            text="Exit",
            command= game.exit_to_main_menu,
            fg_color="transparent",
            width=50
        )
        exit_button.pack(side="left", padx=10)

        restart_button = ctk.CTkButton(
            game.ui_frame,
            text="Restart",
            command= game.restart,
            fg_color="transparent",
            width=50
        )
        restart_button.pack(side="left", padx=5)

        game.timer_label = ctk.CTkLabel(
        game.ui_frame, 
        text="⌛ 000", 
        font=("Arial", 20, "bold")
        )
        
        game.timer_label.pack(side="right", padx=20)

        game.flag_label = ctk.CTkLabel(
        game.ui_frame, 
        text=f"🚩 {game.root.nb_flags:03d}", 
        font=("Arial", 20, "bold")
        )
        
        game.flag_label.pack(side="right", padx=5)

    @staticmethod
    def grid_rendering(game):
        
        rows = cols = game.root.grid_length

        game.grid_buttons = [[None for _ in range(cols)] for _ in range(rows)]

        def update_timer(game):
            if game.timer_running:
                game.seconds += 1
                game.timer_label.configure(text=f"⌛ {game.seconds:03d}")
                
                game.root.after(1000, lambda: update_timer(game))

        def update_flag_counter(game, add=False, rem=False):
            if add:
                game.root.nb_flags +=1
            if rem:
                game.root.nb_flags -=1

            game.flag_label.configure(text=f"🚩 {game.root.nb_flags:03d}")

        def mine_clicked():
            game.timer_running = False
            for r in range(rows):
                for c in range(cols):
                    cell = game.grid.grid[r][c]
                    button = game.grid_buttons[r][c]
                    button.configure(state="disabled")
                    if cell.mine:
                        if 9 <= game.root.nb_mines <= 11:
                            bomb_size = 45
                        elif 38 <= game.root.nb_mines <= 42:
                            bomb_size = 30
                        else:
                            bomb_size = 20
                            
                        button.configure(text="💣", font=("Arial", bomb_size), fg_color= "#E40000")

        def refresh_cells(game):
            for r in range(game.root.grid_length):
                for c in range(game.root.grid_length):
                    cell = game.grid.grid[r][c]
                    button = game.grid_buttons[r][c]
                    if cell.is_dug:
                        if cell.surrounding_bombs == 0:
                            button.configure(fg_color="#4e4f50", state="disabled")
                        else:
                            button.configure(text=str(cell.surrounding_bombs), fg_color="#4e4f50", state="disabled")
                       

        def gui_dig_cells(row, col):
            cell = game.grid.grid[row][col]
            button = game.grid_buttons[row][col]

            button.configure(text="‎", fg_color="#4e4f50", state="disabled")

            game.reveal_empty_cells(row, col)

            refresh_cells(game)

        def on_cell_click(row, col):
            cell = game.grid.grid[row][col]
            button = game.grid_buttons[row][col]

            if game.first_launch and not cell.flag:
                cell.is_dug = True
                game.spawn_mines()
                game.calculate_surrounding_bombs()
                game.timer_running = True
                update_timer(game)

                cell.is_dug = False
                if cell.surrounding_bombs == 0:
                    gui_dig_cells(row, col)
                else:
                    cell.is_dug = True
                    button.configure(text=str(cell.surrounding_bombs), fg_color="#4e4f50", state="disabled")
                    
                return

            if cell.flag:  
                return

            if cell.mine:
                mine_clicked()
            elif not cell.is_dug:
                if cell.surrounding_bombs == 0:
                    gui_dig_cells(row, col)
                else:
                    cell.is_dug = True
                    button.configure(text=str(cell.surrounding_bombs), fg_color="#4e4f50", state="disabled")

        def on_right_click(row, col):
            cell = game.grid.grid[row][col]
            button = game.grid_buttons[row][col]

            if cell.questionmark:
                cell.flag = False
                cell.questionmark = False
                button.configure(text="‎")
            elif cell.flag:
                cell.flag = False
                cell.questionmark = True
                button.configure(text="?")
                update_flag_counter(game, add=True)
            elif not cell.is_dug:
                if game.root.nb_flags > 0:
                    cell.flag = True
                    button.configure(text="🚩")
                    update_flag_counter(game, rem=True)
                else:
                    cell.questionmark = True
                    button.configure(text="?")
        
        for r in range(rows):
            for c in range(cols):
                btn = ctk.CTkButton(
                    game.grid_frame,
                    text="‎",
                    command=lambda r=r, c=c: on_cell_click(r, c),
                    fg_color="#757270"
                )
                btn.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")
                btn.bind("<Button-3>", lambda e, r=r, c=c: on_right_click(r, c))
                game.grid_buttons[r][c] = btn

        for i in range(rows):
            game.grid_frame.grid_rowconfigure(i, weight=1)
        for j in range(cols):
            game.grid_frame.grid_columnconfigure(j, weight=1)

        def adjust_buttons(event):
            frame_width = event.width
            frame_height = event.height

            cell_size = min((frame_width - 2*cols) // cols, (frame_height - 2*rows) // rows)

            for r in range(rows):
                for c in range(cols):
                    btn = game.grid_buttons[r][c]
                    btn.configure(width=cell_size, height=cell_size)

        game.grid_frame.bind("<Configure>", adjust_buttons)