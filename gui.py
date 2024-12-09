import tkinter as tk


class Display(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('2048')
        self.create_grid()
        self.text = Text()


    def bind_handler(self, func):
        self.bind('<Key>', func)


    def create_grid(self):
        self.grid = self.grid = [[0 for col in range(4)] for row in range(4)]
        for x in range(4):
            for y in range(4):
                self.grid[x][y] = Cell()
                self.grid[x][y].grid(row=x, column=y)


    def update_numbers(self, grid:list):
        colors = {0:'#E8E4E3',
                  2:'#FFFCEC',
                  4:'#FFF3CB',
                  8:'#FFD5A4',
                  16:'#FFB588',
                  32:'#FF9271',
                  64:'#FF6854',
                  128:'#FFE280',
                  256:'#FFD76B',
                  512:'#FFCD55',
                  1024:'#FFD543',
                  2048:'#FFC732',
                  'max':'#232426'}

        for x in range(4):
            for y in range(4):
                num = grid[x][y]
                string = ' ' if num == 0 else num
                self.grid[x][y].text(string)
                self.grid[x][y].color(colors[num if num <= 2048 else 'max'])




class Cell(tk.Frame):
    def __init__(self):
        super().__init__(height=100, width=100, borderwidth=5, relief='groove')
        self.label = tk.Label(self, font=("Consolas, 15"))
        self.label.pack(anchor='center', pady=25)
        self.pack_propagate(0)


    def text(self, string:str):
        self.label.configure(text=str(string))

    
    def color(self, hex_code:str):
        self.configure(bg=hex_code)
        self.label.configure(bg=hex_code)




class Text(tk.Frame):
    def __init__(self):
        super().__init__(height=100, width=400, bg='#120E11')
        self.label = tk.Label(self, bg='#120E11', fg='white',
                              font=("Consolas, 15"),
                              text='GAME OVER\nPress [ space ] to play again')
        self.label.pack(anchor='center', pady=20)
        self.pack_propagate(0)


    def show(self):
        self.place(anchor='center', x=200, y=200)


    def hide(self):
        self.place_forget()
