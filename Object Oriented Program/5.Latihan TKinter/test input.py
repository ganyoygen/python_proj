from tkinter import Tk,Label,StringVar,Entry,Button

root = Tk()
root.title("Test App")
root.geometry("640x640+0+0")

heading = (Label(
    root,
    text = "Welcome to the Test App", 
    font=("arial",40,"bold"),
    fg="steelblue")
    .pack()
    )

label1 = (Label(
    root,
    text = 'Enter Your Name',    
    font =('arial,',20,'bold'),    
    fg="black")
    .place(x=10, y=200)    
    )

inputan = StringVar()
box_input = (Entry(
    root,
    textvar=inputan,
    width=25,
    bg='lightgreen')
    .place(x=280,y=210)
)

def do_it():
    print("Input data:",inputan.get())

startbutton = (Button(
    root,
    text='Start',
    width=10,
    height=5,
    bg='lightblue',
    command = do_it)   
    .place(x=250,y=300)
    )



root.mainloop()