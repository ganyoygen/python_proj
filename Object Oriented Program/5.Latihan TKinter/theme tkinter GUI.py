from tkinter import ttk
from ttkthemes import ThemedTk # make sure to pip install ttkthemes

app = ThemedTk(theme='radiance')

ttk.Label(app,text='Username:').grid(row = 0, column = 0)

ttk.Entry(app).grid(row = 0, column = 1, ipady = 5, ipadx = 5)

ttk.Button(app,text='Check').grid(row=0,column=2)

app.mainloop()