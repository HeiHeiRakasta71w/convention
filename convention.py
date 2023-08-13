import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Convention")
root.geometry("1000x500")

def opensettings():
    settingswin = tkinter.Toplevel(root)
    settingswin.geometry("750x250")
    settingswin.title("New Child Window")

def makeoptionbtns():
    text = tkinter.Text(root)
    text.grid(row=2, column=2)
    for i in range(4):
        button = tkinter.Button(text, text="pizza")
        text.window_create("end", window=button)
        text.insert("end", "\n")
        text.configure(state="disabled")
    text.update()

btn1 = tkinter.Button(root, text="button1", fg="black", bg="#7D12FF", height=5, width=20)
btn1.grid(row=10, column=0)

btnExit = tkinter.Button(root, text="Exit", fg="black", bg="red", height=5, width=20)
btnExit.grid(row=0, column=0)

btnSave = tkinter.Button(root, text="Save game", fg="black", bg="green", height=5, width=20)
btnSave.grid(row=0, column=1)

settingslabel = tkinter.Label(root, text="Settings:")
settingslabel.grid(row=1, column=0)

mainText = tkinter.Text(root, width=210, height=40, fg="black", bg="#bcbcbc", font=('Sans Serif', 11, 'italic bold'))
mainText.grid(row=1, column=2)
mainText.insert("insert", "Er din favorittmat pizza, pannekake eller eple?")
mainText.config(state="disabled")

sb = tkinter.Scrollbar(root, command=mainText.yview)
sb.grid(row=1, column=3, sticky='ns')
mainText.configure(yscrollcommand=sb.set)

makeoptionbtns()

root.mainloop()
