import tkinter

main_window = tkinter.Tk()

def exit_windows():
    label2 = tkinter.Label(main_window,text = 'silahkan tekan tanda silang')
    label2.pack()

label1 = tkinter.Label(main_window,text = 'ini test label')
tombol1 = tkinter.Button(main_window,text = 'Test')
exit_tombol = tkinter.Button(main_window,text='Exit', command = exit_windows)
scrolbar = tkinter.Scrollbar()

# method positioning
label1.pack()
tombol1.pack()
exit_tombol.pack()
scrolbar.pack()


# method menampilkan GUI
main_window.mainloop()

print(tkinter.__dict__)

