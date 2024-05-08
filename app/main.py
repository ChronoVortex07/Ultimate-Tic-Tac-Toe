import tkinter as tk
import customtkinter as ctk

import scripts

# from assets.ui_files.board import Board
# from assets.ui_files.cell import Cell

# if __name__ == '__main__':
#     root = ctk.CTk()
#     main_board = Board(root)
#     sub_boards = main_board.set_up_cells(Board)#[[Board(main_board) for _ in range(3)] for _ in range(3)]
#     for i in range(3):
#         for j in range(3):
#             sub_boards[i][j].configure(padx=5, pady=5)
#             sub_boards[i][j].grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
#             sub_boards[i][j].set_up_cells(Cell)
#             sub_boards[i][j].set_display([['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']])
#     root.mainloop()