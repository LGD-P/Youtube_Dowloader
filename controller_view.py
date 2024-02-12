from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import tkinter as tk
from pathlib import Path
from model import YoutubeDlModel


class YoutubeDlGui:
    audio = "audio"
    video = "video"
    current_button_3_state = audio

    def __init__(self):
        self.output_path = Path(__file__).parent
        self.model = YoutubeDlModel()

        self.assets_path = self.output_path / Path("assets/frame0/audio")
        self.assets_video_path = self.output_path / Path("assets/frame0/video")

        self.window = Tk()
        self.window.title("Youtube DL")
        self.window.geometry("512x512")
        self.window.configure(bg="#FFFFFF")
        self.icon_path = "assets/frame0/icon.ico"
        self.window.iconbitmap(self.icon_path)

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=512,
            width=512,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("audio_image_1.png"))
        self.image_1 = self.canvas.create_image(
            256.0,
            256.0,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("audio_entry_1.png"))

        self.entry_bg_1 = self.canvas.create_image(
            249.5,
            485.5,
            image=self.entry_image_1
        )
        self.entry_1 = PlaceholderEntry(self.window,
                                        placeholder='CTRL + V your link here')

        self.entry_1.place(
            x=130.0,
            y=476.0,
            width=235.5,
            height=20.0
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("audio_button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_1_callback,
            relief="flat"
        )
        self.button_1.place(
            x=389.0,
            y=472.0,
            width=94.0,
            height=27.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("audio_button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_2_callback,
            relief="flat"
        )
        self.button_2.place(
            x=378.0,
            y=20.0,
            width=107.0,
            height=29.0
        )

        self.button_image_3_state0 = PhotoImage(
            file=self.relative_to_assets(f"{self.audio}_button_3.png"))
        self.button_image_3_state1 = PhotoImage(
            file=f"{self.assets_video_path}\{self.video}_button_3.png")

        self.button_3 = Button(
            image=self.button_image_3_state0,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_3_callback,
            relief="flat"
        )
        self.button_3.place(
            x=16.0,
            y=20.0,
            width=107.0,
            height=29.0
        )

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def button_1_callback(self):

        if self.current_button_3_state == self.audio:
            return YoutubeDlModel.select_path_to_download_audio_or_video(self.entry_1.get(), self.current_button_3_state)
        else:
            return YoutubeDlModel.select_path_to_download_audio_or_video(self.entry_1.get(), self.current_button_3_state)

    def button_2_callback(self):
        if self.current_button_3_state == self.audio:
            return YoutubeDlModel.read_txt_file_and_download(self.current_button_3_state)
        else:
            return YoutubeDlModel.read_txt_file_and_download(self.current_button_3_state)

    def button_3_callback(self):
        if self.current_button_3_state == self.audio:
            self.assets_path = self.output_path / Path("assets/frame0/video")
            self.current_button_3_state = self.video
        else:
            self.assets_path = self.output_path / Path("assets/frame0/audio")
            self.current_button_3_state = self.audio

        self.button_image_3 = self.button_image_3_state1 if self.current_button_3_state == self.video else self.button_image_3_state0
        self.button_3.config(image=self.button_image_3)

        stem = self.assets_path.stem
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets(f"{stem}_image_1.png"))
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets(f"{stem}_entry_1.png"))
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets(f"{stem}_button_1.png"))
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets(f"{stem}_button_2.png"))
        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets(f"{stem}_button_3.png"))

        self.canvas.itemconfig(self.image_1, image=self.image_image_1)
        self.canvas.itemconfig(self.entry_bg_1, image=self.entry_image_1)
        self.button_1.config(image=self.button_image_1)
        self.button_2.config(image=self.button_image_2)
        self.button_3.config(image=self.button_image_3)

    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()


class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder='', cnf={}, fg='black',
                 fg_placeholder='black', *args, **kw):
        super().__init__(master=None, cnf={
            'bd': 0, 'justify': 'center'}, bg='#bbbebc', *args, **kw)
        self.fg = fg
        self.fg_placeholder = fg_placeholder
        self.placeholder = placeholder
        self.bind('<FocusOut>', lambda event: self.fill_placeholder())
        self.bind('<FocusIn>', lambda event: self.clear_box())
        self.fill_placeholder()

    def clear_box(self):
        if not self.get() and super().get():
            self.config(fg=self.fg)
            self.delete(0, tk.END)

    def fill_placeholder(self):
        if not super().get():
            self.config(fg=self.fg_placeholder)
            self.insert(0, self.placeholder)

    def get(self):
        content = super().get()
        if content == self.placeholder:
            return ''
        return content
