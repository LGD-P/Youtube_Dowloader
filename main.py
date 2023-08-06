from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog
from pathlib import Path

from pytube import YouTube


class YoutubeDL:
    audio = "audio"
    video = "video"
    current_button_3_state = audio

    def __init__(self):
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path("assets/frame0/audio")
        self.assets_video_path = self.output_path / \
            Path("assets/frame0/video")

        self.window = Tk()
        self.window.geometry("512x512")
        self.window.configure(bg="#FFFFFF")

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
        self.entry_1 = Entry(
            bd=0,
            bg="#bbbebc",
            fg="#000000",
            highlightthickness=0
        )
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
            width=96.0,
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

    def run(self):
        self.window.resizable(False, False)
        self.window.mainloop()

    def select_path_and_download_audio(self):
        """This function allow user to select a path from explorer
        then download Youtube link in chosen path

        Returns:
            .mp4: Audio from youtube link as .mp4
        """
        path = filedialog.askdirectory()
        return YouTube(self.entry_1.get()).streams.get_audio_only().download(path)

    def download_from_list_audio(self):
        """This function allow user to download audio.mp4 from a list of link
        register in text document
        """
        path = filedialog.askopenfilename()
        first_list = []
        with open(path, "r", encoding='utf-8') as f:
            for element in f:
                first_list.append(element.strip())
                filtered_list = list(filter(None, first_list))
            path_to_downdload = filedialog.askdirectory()
            for url in filtered_list:
                print(url)
                YouTube(url).streams.get_audio_only().download(
                    path_to_downdload)

    def select_path_and_download_video(self):
        """This function allow user to select a path from explorer
        then download Youtube link in chosen path

        Returns:
            .mp4: Audio from youtube link as .mp4
        """
        path = filedialog.askdirectory()
        return YouTube(self.entry_1.get()).streams.filter(progressive=True)\
            .get_highest_resolution().download(path)

    def download_from_list_video(self):
        """This function allow user to download audio.mp4 from a list of link
        register in text document
        """
        path = filedialog.askopenfilename()
        first_list = []
        with open(path, "r", encoding='utf-8') as f:
            for element in f:
                first_list.append(element.strip())
                filtered_list = list(filter(None, first_list))
            path_to_downdload = filedialog.askdirectory()
            for url in filtered_list:
                print(url)
                YouTube(url).streams.filter(progressive=True).get_highest_resolution().download(
                    path_to_downdload)

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def button_1_callback(self):
        if self.current_button_3_state == self.audio:
            return self.select_path_and_download_audio()
        else:
            return self.select_path_and_download_video()

    def button_2_callback(self):
        if self.current_button_3_state == self.audio:
            return self.download_from_list_audio()
        else:
            return self.download_from_list_video()

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

        self.canvas.itemconfig(self.image_1, image=self.image_image_1)
        self.canvas.itemconfig(self.entry_bg_1, image=self.entry_image_1)
        self.button_1.config(image=self.button_image_1)
        self.button_2.config(image=self.button_image_2)


if __name__ == "__main__":
    app = YoutubeDL()
    app.run()
