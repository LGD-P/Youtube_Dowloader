import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as Tkb
import time
from pytube import YouTube


URL = "https://www.youtube.com/watch?v=L-iepu3EtyE"
PLAYLIST = "https://www.youtube.com/playlist?list=PL-tdP6nrpQYtlJ6gYUeJvpdLd64O6MvoT"


class DataInfo:

    def __init__(self):
        # Create window
        self.root = tk.Tk()
        self.root.title("Data-Info")

        self.table = ttk.Treeview(self.root, columns=[
            "N°", "Title", "Size", "Duration", "Completed"], show="headings")

        # Headers
        self.table.heading("N°", text="N°")
        self.table.heading("Title", text="Title")
        self.table.heading("Size", text="Size")
        self.table.heading("Duration", text="Duration")
        self.table.heading("Completed", text="Completed")

        # Display table
        for column in ["N°", "Title", "Size", "Duration", "Completed"]:
            self.table.column(column, anchor="center")

        self.table.pack(expand=True, fill=tk.BOTH)

    @ staticmethod
    def convert_duration(dur_in_sec):
        minutes = dur_in_sec // 60
        seconds = dur_in_sec % 60
        return f"{minutes} min {seconds} sec"

    def collect_url_data_pattern(object_dl, output_path, url, number):
        """Collect and return data such as title, duration, size and completion status."""

        object_dl.download(output_path)

        # Get video data
        title = YouTube(url).title
        duration = YouTube(url).length
        duration = DataInfo.convert_duration(duration)

        # Convert size in Mo
        size_mb = f"{round(object_dl.filesize / (1024 * 1024), 2)} Mo"

        Completed = "Completed." if object_dl.filesize else "Loading..."
        data = {
            "N°": number,
            "Title": title,
            "Size": size_mb,
            "Duration": duration,
            "Completed": Completed
        }
        return data

    @ staticmethod
    def get_audio_or_video_data_from_single_url(url, output_path, choice):
        """This method adapte collecting process from a video or a audio choice
        """
        if choice == 'audio':
            object_dl = YouTube(url).streams.filter(
                only_audio=True).first()
        elif choice == 'video':
            object_dl = YouTube(url).streams.filter(
                progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        item = DataInfo.collect_url_data_pattern(
            object_dl, output_path, url, 1)
        return item

    def insert_single_url_data_pattern(self, item):
        self.table.insert("", "end", values=(
            item["N°"], item["Title"], item["Size"],
            item["Duration"], item["Completed"]))
        # Refresh data in table
        self.root.update()

        # Running main loop
        self.root.mainloop()

    def add_single_audio_or_video_data_in_table(self, url, output_path, choice):
        item = DataInfo.get_audio_or_video_data_from_single_url(
            url, output_path, choice)
        print(item)
        self.insert_single_url_data_pattern(item,)
