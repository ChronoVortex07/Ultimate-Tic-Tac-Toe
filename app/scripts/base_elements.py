from __future__ import annotations
import numpy as np

class Cell(object):
    def __init__(self, *args, coords: tuple[int, int] = (0, 0), padding: int = 0, value: str | None = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.padding = padding
        self.coords = coords
        self.value = value
        
    def set_value(self, value: str | None) -> None:
        self.value = value
        
    def get_value(self) -> str | None:
        return self.value
    
    def get_raw_cell_values(self) -> str | None:
        return self.value
    
class Board(object):
    def __init__(self, *args, coords: tuple[int, int] = (0, 0), padding: int = 0, value: str | None = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.padding = padding
        self.coords = coords
        self.value = value
        
        self.cells = []
        
    def set_up_cells(self, cells: list[tuple[Board | Cell, int]] | tuple[Board | Cell, int]):
        if isinstance(cells[0], (list, tuple)):
            cell_type = cells[0][0]
            cell_padding = cells[0][1]
            for i in range(9):
                cell = cell_type(padding = cell_padding, value = None)
                self.cells.append(cell)
                # propagate set_up_cells() if the cells are Board cells
                if len(cells) > 1 and cell_type == Board:
                    cell.set_up_cells(cells[1:])
        else:
            cell_type = cells[0]
            cell_padding = cells[1]
            for i in range(9):
                cell = cell_type(padding = cell_padding)
                self.cells.append(cell)
                
    def get_cell_values(self) -> list[list | str | None]:
        return [cell.get_value() for cell in self.cells]
    
    def get_raw_cell_values(self) -> list[list | str | None]:
        return [cell.get_raw_cell_values() for cell in self.cells]
        
    def get_value(self) -> str | None:
        cell_values = np.array(self.get_cell_values()).reshape((3,3))
        # Check rows
        for row in cell_values:
            if row[0] == row[1] == row[2] != None:
                return row[0]

        # Check columns
        for col in range(3):
            if cell_values[0][col] == cell_values[1][col] == cell_values[2][col] != None:
                return cell_values[0][col]

        # Check diagonals
        if cell_values[0][0] == cell_values[1][1] == cell_values[2][2] != None:
            return cell_values[0][0]
        if cell_values[0][2] == cell_values[1][1] == cell_values[2][0] != None:
            return cell_values[0][2]

        # No winner yet
        return None
    
    def get_current_player(self) -> str:
        return self.master.get_current_player()
    
if __name__ == '__main__':
    board = Board()
    board.set_up_cells([(Board, 5), (Cell, 2)])
    print(board.get_value())