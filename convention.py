import tkinter as tk
from tkinter import ttk

class TextBasedGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-Based Game")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.style = ttk.Style(self.root)
        self.style.configure("Option.TButton", foreground="black", background="#7D12FF", width=15)

        self.create_widgets()

    def create_widgets(self):
        self.btn_exit = ttk.Button(self.root, text="Exit", style="Option.TButton", command=self.root.quit)
        self.btn_exit.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.btn_save = ttk.Button(self.root, text="Save Game", style="Option.TButton")
        self.btn_save.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.btn_settings = ttk.Button(self.root, text="Settings", style="Option.TButton", command=self.open_settings)
        self.btn_settings.grid(row=0, column=2, padx=20, pady=20, sticky="w")

        self.main_text = tk.Text(self.root, width=60, height=20, fg="black", bg="#bcbcbc", font=('Sans Serif', 11, 'italic bold'))
        self.main_text.grid(row=1, column=1, padx=20, pady=10, rowspan=4)
        self.main_text.insert("insert", "Er din favorittmat pizza, pannekake eller eple?")
        self.main_text.config(state="disabled")

        self.sb = tk.Scrollbar(self.root, command=self.main_text.yview)
        self.sb.grid(row=1, column=2, pady=10, sticky='ns')
        self.main_text.configure(yscrollcommand=self.sb.set)

        self.make_option_btns()

    def open_settings(self):
        self.root.withdraw()

        settings_win = tk.Toplevel(self.root)
        settings_win.geometry("300x200")
        settings_win.title("Settings")
        settings_win.resizable(False, False)

        def close_settings():
            settings_win.destroy()
            self.root.deiconify()

        settings_win.protocol("WM_DELETE_WINDOW", close_settings)
        # Legg til innstillinger og relevante widgeter i det nye vinduet

    def make_option_btns(self):
        options_frame = ttk.Frame(self.root)
        options_frame.grid(row=2, column=2, padx=20, pady=20)

        for i in range(4):
            button = ttk.Button(options_frame, text="Pizza", style="Option.TButton")
            button.grid(row=i, column=0, pady=5, sticky="w")

def main():
    root = tk.Tk()
    app = TextBasedGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
