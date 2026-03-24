import customtkinter as ctk


class GameRendering:

    @staticmethod
    def game_rendering(game):
        game.ui_frame = ctk.CTkFrame(game.root.container, fg_color="transparent")
        game.ui_frame.pack(side="top", fill="x", padx=10, pady=5)

        game.grid_frame = ctk.CTkFrame(game.root.container, fg_color="transparent")
        game.grid_frame.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        GameRendering.grid_rendering(game)

    @staticmethod
    def grid_rendering(game):
        
        rows = cols = game.root.grid_lengh

        game.grid_buttons = [[None for _ in range(cols)] for _ in range(rows)]

        def gui_dig_cells(row, col):
            cell = game.grid.grid[row][col]
            button = game.grid_buttons[row][col]

            button.configure(text="‎", fg_color="#ffffff", hover="#ffffff")
            # todo : algo creusage

        def on_cell_click(row, col):
            cell = game.grid.grid[row][col]
            button = game.grid_buttons[row][col]

            if game.first_launch:
                cell.is_dug = True
                game.spawn_mines()

                if cell.surrounding_bombs == 0:
                    gui_dig_cells(row, col)
                else:
                    cell.is_dug = True
                    button.configure(text=str(cell.surrounding_bombs))
                    
                return

            if cell.flag:  
                return

            if cell.mine:
                button.configure(text="💣")
                print("BOOM ! Perdu.") # todo gui message
            elif not cell.is_dug:
                cell.is_dug = True
                if cell.surrounding_bombs == 0:
                    gui_dig_cells(row, col)
                else:
                    cell.is_dug = True
                    button.configure(text=str(cell.surrounding_bombs))

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
            elif not cell.is_dug:
                cell.flag = True
                button.configure(text="🚩")
        
        for r in range(rows):
            for c in range(cols):
                btn = ctk.CTkButton(
                    game.grid_frame,
                    text="‎",
                    command=lambda r=r, c=c: on_cell_click(r, c)
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