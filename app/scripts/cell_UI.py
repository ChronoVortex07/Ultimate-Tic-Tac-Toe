import tkinter as tk
from PIL import ImageTk, Image

from base_elements import Cell

class CellUI(Cell, tk.Label):
    def __init__(self, 
        master=None, 
        circle: Image.Image = None, 
        cross: Image.Image = None, 
        empty: Image.Image = None,
        **kwargs
    ) -> None:
        super(CellUI, self).__init__(master, **kwargs)
        self.grid_propagate(False)
        self.configure(
            width = 100,
            height = 100,
            bg = 'white', 
            text = '',
        )
        self.bind('<Configure>', self.resize)
        self.bind('<Button-1>', self.on_press)
        self.bind('<Enter>', lambda x: self.set_hover(True))
        self.bind('<Leave>', lambda x: self.set_hover(False))
        self.grid(row = self.coords[0], column = self.coords[1], sticky = 'nsew', padx = self.padding, pady = self.padding)
        
        self.color = '#FFFFFF'
        self.circle = circle
        self.cross = cross
        self.empty = empty
        self.disabled_state = False
        self.hover = False
        
    def set_display(self, value) -> None:
        if value in ['X', 'O', None]:
            self.value = value
        self.resize()
        
    def set_color(self, color:str) -> None:
        self.color = color
        self.configure(bg = color)
        
    def update_color(self) -> None:
        pass
        
    def resize(self, event = None) -> None:
        img_size = round(min(self.winfo_width(), self.winfo_height())*0.8)
        if self.value == 'X':
            self.PI_cross = ImageTk.PhotoImage(self.cross.resize((img_size, img_size)))
            self.configure(image = self.PI_cross)
        elif self.value == 'O':
            self.PI_circle = ImageTk.PhotoImage(self.circle.resize((img_size, img_size)))
            self.configure(image = self.PI_circle)
        else:
            self.PI_empty = ImageTk.PhotoImage(self.empty.resize((img_size, img_size)))
            self.configure(image = self.PI_empty)
        # self.update()
    
    def on_press(self, event = None) -> None:
        # print(self.coords)
        if self.get_value() == None and not self.disabled_state:
            current_player = self.master.get_current_player()
            self.set_display(current_player)
            self.master.cells_pressed([self.coords])
            
    def set_hover(self, hover: bool):
        self.hover = hover
        if not self.disabled_state:
            if hover and self.get_value() == None:
                self.configure(bg = '#bababa')
            else:
                self.configure(bg = self.color)
        # self.update_color()
        
    def set_disabled_state(self, disabled: bool, exception: list = None) -> None:
        self.disabled_state = disabled
        if disabled and self['bg'] not in ['#003872', '#820000']:
            self.configure(bg = '#757575')
        else:
            self.configure(bg = self.color)
        # self.update_color()
            
if __name__ == '__main__':
    root = tk.Tk()
    cell = CellUI(
        root, 
        circle = Image.open('app/assets/images/circle.png'), 
        cross = Image.open('app/assets/images/cross.png')
    )
    cell.set_value('X')
    cell.grid(row=0, column=0)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()