import tkinter as tk
from tkinter import ttk

def opensettings():
    settingswin = tk.Toplevel(root)
    settingswin.geometry("750x250")
    settingswin.title("Settings")

def makeoptionbtns():
    options_frame = ttk.Frame(root)
    options_frame.grid(row=2, column=2, padx=20, pady=20)
    
    for i in range(4):
        button = ttk.Button(options_frame, text="Pizza", style="Option.TButton")
        button.grid(row=i, column=0, pady=5, sticky="w")

root = tk.Tk()
root.title("Convention")
root.geometry("800x600")

style = ttk.Style(root)
style.configure("Option.TButton", foreground="black", background="#7D12FF", width=15)

btnExit = ttk.Button(root, text="Exit", style="Option.TButton", command=root.quit)
btnExit.grid(row=0, column=0, padx=20, pady=20, sticky="w")

btnSave = ttk.Button(root, text="Save Game", style="Option.TButton")
btnSave.grid(row=0, column=1, padx=20, pady=20, sticky="w")

settingslabel = tk.Label(root, text="Settings:", font=("Arial", 12, "bold"))
settingslabel.grid(row=1, column=0, padx=20, pady=10, sticky="w")

mainText = tk.Text(root, width=60, height=20, fg="black", bg="#bcbcbc", font=('Sans Serif', 11, 'italic bold'))
mainText.grid(row=1, column=1, padx=20, pady=10, rowspan=4)
mainText.insert("insert", "Er din favorittmat pizza, pannekake eller eple?")
mainText.config(state="disabled")

sb = tk.Scrollbar(root, command=mainText.yview)
sb.grid(row=1, column=2, pady=10, sticky='ns')
mainText.configure(yscrollcommand=sb.set)

makeoptionbtns()

root.mainloop()
