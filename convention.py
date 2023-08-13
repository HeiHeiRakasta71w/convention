import tkinter

root=tkinter.Tk()
root.title("Convention")
root.geometry("1000x500")

def opensettings():
    settingswin = tkinter.Toplevel(root)
    settingswin.geometry("750x250")
    settingswin.title("New Child Window")

def makeoptionbtns(quantity):
    for i in range(quantity):
        button = tkinter.Button(optionswin, text="pizza")
        optionswin.window_create("end", window=button)
        optionswin.insert("end", "\n")
        optionswin.configure(state="disabled")


btn1=tkinter.Button(root, text="button1", fg="black", bg ="#7D12FF", height=5, width= 20)
btn1.grid(row=10,column=0)

btnExit=tkinter.Button(root, text="Exit", fg="black", bg ="red", height=5, width= 20)
btnExit.grid(row=0,column=0)

btnSave = tkinter.Button(root, text = "Save game", fg = "black", bg = "green", height=5, width = 20)
btnSave.grid(row=0,column=1)

settingslabel = tkinter.Label(root, text = "Settings:")
settingslabel.grid(row=1,column=0)

mainText=tkinter.Text(root,width=210, height=40 , fg="black" , bg="#bcbcbc", font= ('Sans Serif', 11, 'italic bold'))
mainText.grid(row=1, column=2)
mainText.insert("insert", "You come to a place with two corridors to the left and to the right of you.")
mainText.config(state="disabled")


mainText.insert("insert", "Taking it out of its place makes a spreadsheet lie in your hands")

queestions = {"First question: Which following age group are you apart of?", "Second question: What is your gender-identity?",
              "third question: What is your sexual orientation?", "Fourth question: "}

for i in range(10):
    mainText.insert()
    mainText.insert("insert", "You check the corresponding checkbox")

mainText.insert("insert", "Taking it out of its place makes a spreadsheet lie in your hands")

optionswin = tkinter.Text(root)
optionswin.grid(row = 2, column = 2)
sb = tkinter.Scrollbar(root, command=optionswin.yview)
sb.grid(row = 3, column = 1)
optionswin.configure(yscrollcommand=sb.set)

makeoptionbtns(10)

root.mainloop()