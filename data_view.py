import tkinter as tk
from tkinter import ttk
import ttkbootstrap as Tkb
import time
from pytube import YouTube

# Données du tableau
DATA = [
    {"N°": 1, "Title": "Video 1", "Size": 100, "Duration": 10, "Completed": True},
    {"N°": 2, "Title": "Video 2", "Size": 200, "Duration": 20, "Completed": True},
    {"N°": 3, "Title": "Video 3", "Size": 300, "Duration": 30, "Completed": False},
    {"N°": 4, "Title": "Video 4", "Size": 400, "Duration": 40, "Completed": True},
    {"N°": 5, "Title": "Video 5", "Size": 500, "Duration": 50, "Completed": False}
]

URL = "https://www.youtube.com/watch?v=L-iepu3EtyE"
PLAYLIST = "https://www.youtube.com/playlist?list=PL-tdP6nrpQYtlJ6gYUeJvpdLd64O6MvoT"


class DataInfo:

    def __init__(self):
        # Création de la fenêtre
        self.root = tk.Tk()
        self.root.title("Tableau d'informations")

        # Style du thème vapor de ttkbootstrap
        self.style = Tkb.Style("vapor")

        # Création du tableau avec le style du thème vapor
        self.table = ttk.Treeview(self.root, columns=[
            "N°", "Title", "Size", "Duration", "Completed"], show="headings", style="Treeview")

        # Affichage des en-têtes
        self.table.heading("N°", text="N°")
        self.table.heading("Title", text="Title")
        self.table.heading("Size", text="Size")
        self.table.heading("Duration", text="Duration")
        self.table.heading("Completed", text="Completed")

        # Affichage du tableau
        self.table.pack(expand=True, fill=tk.BOTH)

    @ staticmethod
    def convert_duration(dur_in_sec):
        minutes = dur_in_sec // 60
        seconds = dur_in_sec % 60
        return f"{minutes} min {seconds} sec"

    def collect_single_url_data_pattern(object_dl, url):
        object_dl.download()

        # Récupère les informations de la vidéo
        number = 0
        title = YouTube(url).title
        duration = YouTube(url).length
        duration = DataInfo.convert_duration(duration)
        size = object_dl.filesize if object_dl.filesize else "Calculation in progress.."

        # Convertit la taille du fichier en Mo
        size_mb = f"{round(size / (1024 * 1024), 2)} Mo"
        # == object_dl.filesize_approx à voir
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
    def get_audio_data_from_single_url(url):

        object_dl = YouTube(url).streams.get_audio_only()
        item = DataInfo.collect_single_url_data_pattern(object_dl, url)
        return item

    def insert_single_url_data_pattern(self, item):
        self.table.insert("", "end", values=(
            item["N°"], item["Title"], item["Size"],
            item["Duration"], item["Completed"]))
        # Actualisation de la fenêtre à chaque ajout d'une ligne
        self.root.update()
        time.sleep(2)

        # Lancement de la fenêtre principale tkinter
        self.root.mainloop()

    def add_single_audio_data_in_table(self, url):
        item = DataInfo.get_audio_data_from_single_url(url)
        print(item)
        self.insert_single_url_data_pattern(item)

    @ staticmethod
    def get_video_data_from_single_url(url):

        object_dl = YouTube(url).streams.filter(progressive=True).order_by(
            'resolution').desc().first()
        item = DataInfo.collect_single_url_data_pattern(object_dl, url)
        return item

    def add_single_video_data_in_table(self, url):
        item = DataInfo.get_video_data_from_single_url(url)
        print(item)
        self.insert_single_url_data_pattern(item)
