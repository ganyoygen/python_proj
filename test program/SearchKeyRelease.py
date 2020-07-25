import tkinter as tk

# --- functions ---

def search_command(event=None):

    # to compare lower case
    text = e1.get().lower()

    list1.delete(0, 'end')

    if text: # search only if text is not empty
        for word in liststuff:
            if word.lower().startswith(text):
                list1.insert('end', word)

# --- main ---

liststuff = ["bob", "john", "theo", "bobby"]

# GUI

root = tk.Tk()

l1 = tk.Label(root, text='Name')
l1.grid(row=0, column=0)

title_text = tk.StringVar()

e1 = tk.Entry(root, textvariable=title_text)
e1.grid(row=0, column=1)
e1.bind('<KeyRelease>', search_command)

list1 = tk.Listbox(root, height=0, width=35)
list1.grid(row=1, rowspan=4, columnspan=2)

sb1 = tk.Scrollbar(root)
sb1.grid(row=1, column=3)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = tk.Button(root, text="Search", width=12, command=search_command)
b1.grid(row=0, column=4)

root.mainloop()
