import tkinter as tk

class Page3(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="This is page 3")
        label.pack(fill ="both", expand=True, padx=20, pady=10)