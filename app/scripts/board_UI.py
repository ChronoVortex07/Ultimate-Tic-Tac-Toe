from __future__ import annotations
import tkinter as tk
from PIL import  Image
import numpy as np

from base_elements import Board
from cell_UI import CellUI

class BoardUI(Board, tk.Frame):
    def __init__(self, 
        master = None, 
        circle: Image.Image = None, 
        cross: Image.Image = None, 
        empty: Image.Image = None,
        **kwargs
    ) -> None:
        super(BoardUI, self).__init__(master, **kwargs)
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
        
    def set_up_cells(self, cells: list[tuple[BoardUI | CellUI, int]] | tuple[BoardUI | CellUI, int]):
        if isinstance(cells[0], (list, tuple)):
            cell_type = cells[0][0]
            cell_padding = cells[0][1]
            for i in range(9):
                cell = cell_type(
                    self, 
                    padding = cell_padding, 
                    value = None, 
                    coords = (i//3, i%3),
                    circle = self.circle,
                    cross = self.cross,
                    empty = self.empty
                )
                self.cells.append(cell)
                # propagate set_up_cells() if the cells are Board cells
                if len(cells) > 1 and cell_type == BoardUI:
                    cell.set_up_cells(cells[1:])
        else:
            cell_type = cells[0]
            cell_padding = cells[1]
            for i in range(9):
                cell = cell_type(self, padding = cell_padding, coords = (i//3, i%3))
                self.cells.append(cell)
                
    def set_disabled_state(self, disabled:bool, exception:list = None):
        for i in range(9):
            if not exception:
                self.cells[i].set_disabled_state(disabled)
            elif exception and exception[0] == (i//3, i%3):
                self.cells[i].set_disabled_state(False)
            else:
                self.cells[i].set_disabled_state(True)
                
    def set_color(self, color:str) -> None:
        for cell in self.cells:
            cell.set_color(color)
            
    def get_current_player(self) -> str:
        return self.master.get_current_player()
            
    def cells_pressed(self, coords: list[tuple[int,int]]) -> None:
        self.master.cells_pressed([self.coords, *coords])
        
    def update_disabled_state(self, coords) -> None:
        if coords:
            if self.cells[coords[0][0]*3+coords[0][1]].get_value() == None:
                for i in range(9):
                    if i == coords[0][0]*3+coords[0][1]:
                        self.cells[i].update_disabled_state(coords[1:])
                    else:
                        self.cells[i].set_disabled_state(True)
            else:
                for i in range(9):
                    self.cells[i].set_disabled_state(False)
        else:
            self.set_disabled_state(False)
                
    def update_color(self) -> None:
        if self.get_value() == 'X':
            color = '#003872'
            self.set_color(color)
        elif self.get_value() == 'O':
            color = '#820000'
            self.set_color(color)  
        else:
            for cell in self.cells:
                cell.update_color()
        
if __name__ == '__main__':
    root = tk.Tk()
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    game = BoardUI(
        root,
        circle = Image.open('app/assets/images/circle.png'),
        cross = Image.open('app/assets/images/cross.png'),
    )
    game.grid(row = 0, column = 0, sticky = 'nsew')
    game.set_up_cells([(BoardUI, 5), (CellUI, 2)])
    game.set_disabled_state(True)
    root.mainloop()
                    

        