from __future__ import annotations
import tkinter as tk
from PIL import  Image
import numpy as np

from cell_UI import CellUI
from board_UI import BoardUI

class MainBoardUI(BoardUI, tk.Frame):
    def __init__(self, 
        master = None, 
        circle: Image.Image = None, 
        cross: Image.Image = None, 
        empty: Image.Image = None,
        **kwargs
    ) -> None:
        super(BoardUI, self).__init__(
            master,
            # circle = circle,
            # cross = cross,
            **kwargs
        )
        self.grid_rowconfigure((0,1,2), weight = 1)
        self.grid_columnconfigure((0,1,2), weight = 1)
        self.grid_propagate(False)
        self.configure(
            width = 1000,
            height = 1000,
            bg = 'black', 
        )
        self.grid(row = self.coords[0], column = self.coords[1], sticky = 'nsew', padx = self.padding, pady = self.padding)
        
        self.circle = circle
        self.cross = cross
        self.empty = empty
        
        self.current_player = 'X'
        
    def get_current_player(self) -> str:
        self.current_player = 'X' if self.current_player == 'O' else 'O'
        return self.current_player
        
    def cells_pressed(self, coords: list[tuple[int,int]]) -> None:
        self.update_color()
        self.update_disabled_state(coords[1:])
    
    def update_disabled_state(self, coords) -> None:
        if self.cells[coords[0][0]*3+coords[0][1]].get_value() == None:
            for i in range(9):
                if i == coords[0][0]*3+coords[0][1]:
                    self.cells[i].update_disabled_state(coords[1:])
                else:
                    self.cells[i].set_disabled_state(True)
        else:
            for i in range(9):
                self.cells[i].set_disabled_state(False)
        
if __name__ == '__main__':
    root = tk.Tk()
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    game = MainBoardUI(
        root,
        circle = Image.open('app/assets/images/circle.png'),
        cross = Image.open('app/assets/images/cross.png'),
        empty = Image.open('app/assets/images/empty.png')
    )
    game.grid(row = 0, column = 0, sticky = 'nsew')
    game.set_up_cells([(BoardUI, 5), (CellUI, 2)])
    # game.set_disabled(True)
    root.mainloop()