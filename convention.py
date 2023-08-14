import tkinter as tk
from tkinter import ttk
import time

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
        self.root.destroy()
        game_window = tk.Tk()
        app = TextBasedGameApp(game_window)
        game_window.mainloop()

    def load_saved_game(self):
        self.root.destroy()
        saved_game_window = tk.Tk()
        app = LoadSavedGameApp(saved_game_window)
        saved_game_window.mainloop()

    def show_credits(self):
        self.root.destroy()
        credits_window = tk.Tk()
        app = CreditsApp(credits_window)
        credits_window.mainloop()

class TextBasedGameApp:
    current_resolution = "800x600"

    def __init__(self, root):
        self.root = root
        self.root.title("Text-Based Game")
        self.root.geometry(self.current_resolution)
        self.root.resizable(False, False)

        self.typewriter_delay = 50  # Delay in milliseconds between each character
        self.character_format = {'Player': ('blue', 'bold'), 'NPC': ('green', 'italic')}
        self.current_character = 'Player'

        self.style = ttk.Style(self.root)
        self.style.configure("Option.TButton", foreground="black", background="#7D12FF", width=15)

        self.create_widgets()

    def print_text_with_typewriter(self, text):
        self.main_text.config(state="normal")
        self.main_text.delete("1.0", "end")

        font_config = self.main_text.cget("font")  # Get the font configuration of the main text widget
        font_color = self.main_text.cget("fg")  # Get the font color of the main text widget

        self.main_text.tag_configure("format", foreground=font_color, font=font_config)
        self.root.update()

        for i, char in enumerate(text):
            self.main_text.insert("end", char, "format")
            self.root.update()
            time.sleep(self.typewriter_delay / 1000)

        self.main_text.config(state="disabled")

    def change_character_format(self, character):
        self.current_character = character

    def create_widgets(self):
        self.btn_exit = ttk.Button(self.root, text="Exit", style="Option.TButton", command=self.root.quit)
        self.btn_exit.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.btn_save = ttk.Button(self.root, text="Save Game", style="Option.TButton")
        self.btn_save.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.btn_settings = ttk.Button(self.root, text="Settings", style="Option.TButton", command=self.open_settings)
        self.btn_settings.grid(row=0, column=2, padx=20, pady=20, sticky="w")

        self.main_text = tk.Text(self.root, width=60, height=20, fg="black", bg="#bcbcbc", font=('Sans Serif', 11, 'italic bold'))
        self.main_text.grid(row=1, column=1, padx=20, pady=10, rowspan=3)
        self.change_character_format('NPC')  # Set formatting for NPC speech
        self.print_text_with_typewriter("It's late and you have to set your alarm on your phone to catch the ride to the convention you are going to.")
        self.main_text.config(state="disabled")

        self.choice_entry = tk.Entry(self.root, width=60, fg="black", bg="white", font=('Sans Serif', 11, 'italic bold'))
        self.choice_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        self.sb = tk.Scrollbar(self.root, command=self.main_text.yview)
        self.sb.grid(row=1, column=2, pady=10, sticky='ns')
        self.main_text.configure(yscrollcommand=self.sb.set)

    def open_settings(self):
        self.root.withdraw()

        settings_win = tk.Toplevel(self.root)
        settings_win.geometry("300x200")
        settings_win.title("Settings")
        settings_win.resizable(False, False)

        def close_settings():
            settings_win.destroy()
            self.root.deiconify()

        def apply_settings():
            new_resolution = resolution_entry.get()
            width, height = map(int, new_resolution.split("x"))
            self.current_resolution = f"{width}x{height}"
            self.root.geometry(self.current_resolution)
            settings_win.destroy()
            self.root.deiconify()

        settings_win.protocol("WM_DELETE_WINDOW", close_settings)

        resolution_label = tk.Label(settings_win, text="Enter new resolution (e.g. 800x600):")
        resolution_label.pack(pady=10)

        resolution_entry = tk.Entry(settings_win)
        resolution_entry.pack(pady=5)

        apply_button = ttk.Button(settings_win, text="Apply", command=apply_settings)
        apply_button.pack(pady=5)

        exit_button = ttk.Button(settings_win, text="Exit", command=close_settings)
        exit_button.pack(pady=5)


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
