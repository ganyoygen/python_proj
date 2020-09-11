import tkinter as tk
from tkinter import *
 
class Hours(tk.Frame):
    def __init__(self,frame):
        tk.Frame.__init__(self,frame)
        frame = frame
 
        vcmd = (self.register(self.onValidate), '%d', '%s', '%S')
 
        # Entry to insert a 24 hour format
        entry = Entry(frame, validate="key", validatecommand=vcmd, width=7, justify=tk.CENTER)
        entry.bind("<KeyRelease>", self.hour_24)
        entry.grid(row=2, column=1)

    def onValidate(self, d, s, S):
        # if it's deleting return True
        if d == "0":
            return True
        # Allow only digit, ":" and check the length of the string
        if ((S == ":" and len(s) != 2) or (not S.isdigit() and
                S != ":") or (len(s) == 3 and int(S) > 5) or len(s) > 4):
            self.bell()
            return False
         
        return True
 
    def hour_24(self, event):
        """
        Check and build the correct format hour: hh:mm in 24 format
        it keep in mind the 0x, 1x and 2x hours and the max minutes can be 59
        """
 
        # get the object that triggered the event
        s = event.widget
        # if delete a char do return ok or delete the char ":" and the previous number
        if len(s.get()) == 2 and event.keysym=="BackSpace":
            s.delete(len(s.get())-1, tk.END)
        if event.keysym=="BackSpace":
            return
         
        # check the hour format and add : between hours and minutes
        if len(s.get()) == 1 and int(s.get()) > 2:
            s.insert(0, "0")
            s.insert("end", ":")
        elif len(s.get()) == 2 and int(s.get()) < 24:
            s.insert(2, ":")
        elif len(s.get()) >= 2 and s.get()[2:3] != ":":
            self.bell()
            s.delete(1, tk.END)

# root = tk.Tk()
# Hours(root).pack()
# root.mainloop()