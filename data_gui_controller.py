import tkinter as tk
from tkinter import ttk
import subprocess
import json
import os

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
            "N°", "Title", "Size", "Completed"], show="headings")

        # Headers
        self.table.heading("N°", text="N°")
        self.table.heading("Title", text="Title")
        self.table.heading("Size", text="Size")
        self.table.heading("Completed", text="Completed")

        # Display table
        for column in ["N°", "Title", "Size", "Completed"]:
            self.table.column(column, anchor="center")

        # Set style for Treeview
        style = ttk.Style()
        style.configure("Treeview",
                        background="black",
                        foreground="white",
                        fieldbackground="black")
        style.map("Treeview", background=[('selected', 'green')])

        self.table.pack(expand=True, fill=tk.BOTH)

    @staticmethod
    def collect_url_data_pattern(file_path, output_path, url, number):
        """Collect and return data such as title, size and completion status."""

        # Get video data using yt-dlp
        try:
            result = subprocess.run(['yt-dlp', '--print-json', url], capture_output=True, text=True, check=True)
            info = json.loads(result.stdout)
            title = info.get('title', 'Unknown')
        except Exception as e:
            print(f"Error getting metadata: {e}")
            title = 'Unknown'

        # If title is unknown, extract from file name
        if title == 'Unknown' and file_path:
            title = os.path.splitext(os.path.basename(file_path))[0]

        # Convert size in Mo
        try:
            size_mb = f"{round(os.path.getsize(file_path) / (1024 * 1024), 2)} Mo" if file_path else 'Unknown'
        except Exception as e:
            print(f"Error getting file size: {e}")
            size_mb = 'Unknown'

        Completed = "Completed." if file_path and os.path.exists(file_path) else "Loading..."
        data = {
            "N°": number,
            "Title": title,
            "Size": size_mb,
            "Completed": Completed
        }
        return data


    def insert_single_url_data_pattern(self, item):
        """Manage data insertion in table"""
        self.table.insert("", "end", values=(
            item["N°"], item["Title"], item["Size"],
            item["Completed"]))
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
                item["Completed"]))
            print(f"Insert N°{index} done")

        dl.root.mainloop()



