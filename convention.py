import tkinter as tk
from tkinter import ttk

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.style = ttk.Style(self.root)
        self.style.configure("Option.TButton", foreground="black", background="#7D12FF", width=20)

        self.create_widgets()

    def create_widgets(self):
        self.btn_new_game = ttk.Button(self.root, text="Start New Game", style="Option.TButton", command=self.start_new_game)
        self.btn_new_game.pack(pady=10)

        self.btn_load_game = ttk.Button(self.root, text="Load Game", style="Option.TButton", command=self.load_saved_game)
        self.btn_load_game.pack(pady=10)

        self.btn_credits = ttk.Button(self.root, text="Credits", style="Option.TButton", command=self.show_credits)
        self.btn_credits.pack(pady=10)

    def start_new_game(self):
        self.root.destroy()  # Lukk hovedmeny-vinduet
        game_window = tk.Tk()  # Opprett et nytt spillvindu
        app = TextBasedGameApp(game_window)
        game_window.mainloop()

    def load_saved_game(self):
        self.root.destroy()  # Lukk hovedmeny-vinduet
        saved_game_window = tk.Tk()  # Opprett et nytt lagret spill-vindu
        app = LoadSavedGameApp(saved_game_window)
        saved_game_window.mainloop()

    def show_credits(self):
        self.root.destroy()  # Lukk hovedmeny-vinduet
        credits_window = tk.Tk()  # Opprett et nytt vindu for kreditter
        app = CreditsApp(credits_window)
        credits_window.mainloop()

class TextBasedGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-Based Game")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.style = ttk.Style(self.root)
        self.style.configure("Option.TButton", foreground="black", background="#7D12FF", width=15)

        self.options = ["Pizza", "Pannekake", "Eple"]  # Liste med forskjellige alternativer

        self.create_widgets()

    def create_widgets(self):
        # Opprett knapper og andre GUI-elementer
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
        
        # Opprett knapper for hvert alternativ i self.options
        for i, option in enumerate(self.options):
            button = ttk.Button(options_frame, text=option, style="Option.TButton")
            button.grid(row=i, column=0, pady=5, sticky="w")

class LoadSavedGameApp:
    pass

class CreditsApp:
    pass

def main():
    root = tk.Tk()
    main_menu = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
