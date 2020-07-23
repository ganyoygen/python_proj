import tkinter as tk
import tkinter.ttk as ttk
import os

class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.tree = ttk.Treeview(parent, columns=("size", "modified"))
        self.tree["columns"] = ("date", "time", "loc")

        self.tree.column("date", width=80)
        self.tree.column("time", width=80)
        self.tree.column("loc", width=100)

        self.tree.heading("date", text="Date")
        self.tree.heading("time", text="Time")
        self.tree.heading("loc", text="Loc")
        self.tree.bind('<ButtonRelease-1>', self.selectItem)

        self.tree.insert("","end",text = "Name",values = ("Date","Time","Loc"))
        self.tree.insert("","end",text = "John",values = ("2017-02-05","11:30:23","Airport"))
        self.tree.insert("","end",text = "Betty",values = ("2014-06-25","18:00:00","Orchard Road"))

        self.tree.grid()

    def selectItem(self, event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
        os.system("cls")
        print ('curItem = ', curItem)
        print ('col = ', col)

        if col == '#0':
            cell_value = curItem['text']
        elif col == '#1':
            cell_value = curItem['values'][0]
        elif col == '#2':
            cell_value = curItem['values'][1]
        elif col == '#3':
            cell_value = curItem['values'][2]
        print ('cell_value = ', cell_value)


if __name__ == "__main__":
    window = tk.Tk()
    app = App(window)
    window.mainloop()