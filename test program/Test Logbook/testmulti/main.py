'''
https://stackoverflow.com/questions/36032712/ttk-notebook-share-data-between-imported-tabs
'''
import tkinter as tk
from tkinter import ttk
from page1 import Page1
from page3 import Page3

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        page1 = Page1(self.notebook)
        page3 = Page3(self.notebook)
        self.notebook.add(page1, text="Page 1")
        self.notebook.add(page3, text="Page 3")

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()