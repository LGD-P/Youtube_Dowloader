import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path
import os
import sys

class ErrorMessagePopup:
    def __init__(self):
        self.error_window = tk.Toplevel()
        self.error_window.title("Error")
        self.error_window.geometry("500x100")
        self.error_window.configure(bg='black')
        # Détecter si c'est un exe PyInstaller
        if hasattr(sys, '_MEIPASS'):
            self.output_path = Path(sys._MEIPASS)
        else:
            self.output_path = Path(__file__).parent
        self.assets_path = os.path.join(self.output_path, "assets", "frame0")
        self.image_path = os.path.join(self.assets_path, "error.png")
        original_image = Image.open(self.image_path)
        self.icon_path = os.path.join(self.output_path, "assets", "frame0", "icon.ico")
        self.error_window.iconbitmap(self.icon_path)
        black_background = Image.new("RGB", original_image.size, (0, 0, 0))
        black_background.paste(original_image, (0, 0), original_image)

        resized_image = black_background.resize((25, 25))
        self.error_window.resized_tk_image = ImageTk.PhotoImage(resized_image)

        frame = tk.Frame(self.error_window, bg='black')
        frame.pack(padx=5, pady=10)

        image_label = tk.Label(frame, image=self.error_window.resized_tk_image, bg='black')
        image_label.grid(row=0, column=0)

        message = "Please check the Youtube URL you have entered."
        message_label = tk.Label(frame, text=message, padx=20, pady=10, foreground='white', bg='black')
        message_label.grid(row=0, column=1)

        button = tk.Button(self.error_window, text="OK", command=self.error_window.destroy)
        button.pack(pady=(5, 5), padx=10)

        self.error_window.mainloop()
