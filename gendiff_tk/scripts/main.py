import tkinter as tk
from tkinter.scrolledtext import ScrolledText


# from tkinter import messagebox as mb
# from tkinter import filedialog as fd


class Window:
    def __init__(self, width, height, title="MyWindow"):
        self.root = tk.Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        self.root.geometry("+600+300")
        # self.root.resizable(resizable[0], resizable[1])
        self.text = ScrolledText(self.root)

    def run(self):
        # self.draw_widgets()
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(500, 500, "Gendiff")
    window.run()
