import tkinter as tk
from tkinter import ttk

# Funksjon som åpner vinduet for innstillinger
def opensettings():
    settingswin = tk.Toplevel(root)  # Opprett et nytt toppnivå vindu (nytt vindu)
    settingswin.geometry("300x200")   # Angi størrelsen på vinduet
    settingswin.title("Settings")     # Angi tittelen på vinduet
    
    # Her kan du legge til innstillinger og relevante widgeter i det nye vinduet

# Funksjon for å opprette knapper med forskjellige alternativer
def makeoptionbtns():
    options_frame = ttk.Frame(root)  # Opprett en ramme for knappene
    options_frame.grid(row=2, column=2, padx=20, pady=20)  # Plasser rammen i hovedvinduet
    
    for i in range(4):
        button = ttk.Button(options_frame, text="Pizza", style="Option.TButton")  # Opprett en knapp
        button.grid(row=i, column=0, pady=5, sticky="w")  # Plasser knappen i rammen

# Hovedvinduet
root = tk.Tk()
root.title("Convention")  # Angi tittelen på hovedvinduet
root.geometry("800x600")        # Angi størrelsen på hovedvinduet

# Hindre endring av vindusstørrelse
root.resizable(False, False)

style = ttk.Style(root)
style.configure("Option.TButton", foreground="black", background="#7D12FF", width=15)

# Opprett og plasser "Exit" knapp
btnExit = ttk.Button(root, text="Exit", style="Option.TButton", command=root.quit)
btnExit.grid(row=0, column=0, padx=20, pady=20, sticky="w")

# Opprett og plasser "Save Game" knapp
btnSave = ttk.Button(root, text="Save Game", style="Option.TButton")
btnSave.grid(row=0, column=1, padx=20, pady=20, sticky="w")

# Opprett og plasser "Settings" knapp
btnSettings = ttk.Button(root, text="Settings", style="Option.TButton", command=opensettings)
btnSettings.grid(row=0, column=2, padx=20, pady=20, sticky="w")

# Opprett og plasser hovedtekst-widget
mainText = tk.Text(root, width=60, height=20, fg="black", bg="#bcbcbc", font=('Sans Serif', 11, 'italic bold'))
mainText.grid(row=1, column=1, padx=20, pady=10, rowspan=4)
mainText.insert("insert", "Er din favorittmat pizza, pannekake eller eple?")
mainText.config(state="disabled")

# Opprett og plasser scrollbar for hovedtekst-widget
sb = tk.Scrollbar(root, command=mainText.yview)
sb.grid(row=1, column=2, pady=10, sticky='ns')
mainText.configure(yscrollcommand=sb.set)

# Kall funksjonen for å opprette knapper med alternativer
makeoptionbtns()

# Start hovedløkken for GUI
root.mainloop()
