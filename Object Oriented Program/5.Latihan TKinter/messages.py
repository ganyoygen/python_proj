from tkinter import messagebox


result1 = messagebox.askokcancel('Title1','Do you really?')
print(result1) # yes = True, no = False

result2 = messagebox.askyesno('Title2','Do you really?')
print(result2) # yes = True, no = False

result3 = messagebox.askyesnocancel('Title2','Do you really?')
print(result3) # yes = True, no = False, cancel = None

result4 = messagebox.askretrycancel(title='Warning',message='Game over')
print(result4)