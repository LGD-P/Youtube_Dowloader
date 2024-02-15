import tkinter as tk
from tkinter import ttk
from pytube import YouTube

URL = "https://www.youtube.com/watch?v=L-iepu3EtyE"
PLAYLIST = "https://www.youtube.com/playlist?list=PL-tdP6nrpQYtlJ6gYUeJvpdLd64O6MvoT"


class DataInfo:

    def __init__(self):
        # Create window
        self.root = tk.Toplevel()
        self.root.configure(background="black", bg='black')
        self.root.title("Data-Info")
        self.icon_path = "assets/frame0/icon.ico"
        self.root.iconbitmap(self.icon_path)

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

        # Set style for Treeview
        style = ttk.Style()
        style.configure("Treeview",
                        background="black",
                        foreground="white",
                        fieldbackground="black")
        style.map("Treeview", background=[('selected', 'green')])

        self.table.pack(expand=True, fill=tk.BOTH)

    @ staticmethod
    def convert_duration(dur_in_sec):
        minutes = dur_in_sec // 60
        seconds = dur_in_sec % 60
        return f"{minutes} min {seconds} sec"

    @staticmethod
    def collect_url_data_pattern(object_dl, output_path, url, number):
        """Collect and return data such as title, duration, size and completion status."""

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


    def insert_single_url_data_pattern(self, item):
        """Manage data insertion in table"""
        self.table.insert("", "end", values=(
            item["N°"], item["Title"], item["Size"],
            item["Duration"], item["Completed"]))
        # Refresh data in table
        self.root.update()

        # Running main loop
        self.root.mainloop()

    def add_single_audio_or_video_data_in_table(self, item):
        """Insert data in table"""
        self.insert_single_url_data_pattern(item)


    @staticmethod
    def insert_data_from_text_list(datas):
        """Use DataInfo method to collect and insert data in a table after
        download
        """
        dl = DataInfo()

        index = 0
        for item in datas:
            print("Starting loop")
            index += 1
            dl.table.insert("", "end", values=(
                index, item["Title"], item["Size"],
                item["Duration"], item["Completed"]))
            print(f"Insert N°{index} done")



