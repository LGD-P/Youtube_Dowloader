from pytube import Playlist, YouTube
from tkinter import filedialog
import tkinter as tk
import time
from data_view import DataInfo


class YoutubeDlModel:
    PLAYLIST_TAG = "https://www.youtube.com/playlist?list="

    @staticmethod
    def download_audio(link, output_path):
        """
        Choose the right audio method based on a youtube playlist or simple URL
        """

        if YoutubeDlModel.PLAYLIST_TAG in link:
            print("Audio: C'est une playlist:")
            print(link)
            index = 0
            urls = []
            for audio in Playlist(link).videos:
                urls.append(audio.watch_url)

            datas = []
            for element in urls:
                index += 1
                element_to_append = DataInfo.collect_playlist_url_data_pattern(
                    YouTube(element).streams.filter(only_audio=True).first(), element, index)
                datas.append(element_to_append)

            print(datas)
            dl = DataInfo()

            index = 0
            for item in datas:
                print("début de boucle")
                # insert_single_url_data_pattern(item)
                index += 1
                time.sleep(1)
                dl.table.insert("", "end", values=(
                    item["N°"], item["Title"], item["Size"],
                    item["Duration"], item["Completed"]))
                # dl.insert_single_url_data_pattern(item)
                print(f"Insertion N°{index} effectuée")
                # audio.streams.get_audio_only().download(output_path=output_path)

        else:
            print("Audio: C'est un simple lien")
            print(link)
            dl = DataInfo()
            # YouTube(link).streams.get_audio_only().download(output_path=output_path)
            dl.add_single_audio_data_in_table(link)

    @staticmethod
    def download_audio_from_text_list(link, output_path):
        """
        Choose the right audio method based on a youtube playlist or simple URL
        """
        datas = []

        if YoutubeDlModel.PLAYLIST_TAG in link:
            print("Audio: C'est une playlist:")
            print(link)
            index = 0
            urls = []
            for audio in Playlist(link).videos:
                urls.append(audio.watch_url)

            for element in urls:
                index += 1
                element_to_append = DataInfo.collect_playlist_url_data_pattern(
                    YouTube(element).streams.filter(only_audio=True).first(), element, index)
                datas.append(element_to_append)

        else:
            print("Audio: C'est un simple lien")
            print(link)
            datas.append(DataInfo.get_audio_data_from_single_url(link))

        print("DATA APRES TELECHARGEMENT", datas)

        return datas

    @staticmethod
    def insert_data_from_text_list(datas):
        dl = DataInfo()

        index = 0
        for item in datas:
            print("début de boucle")
            # insert_single_url_data_pattern(item)
            index += 1
            time.sleep(1)
            dl.table.insert("", "end", values=(
                index, item["Title"], item["Size"],
                item["Duration"], item["Completed"]))
            # dl.insert_single_url_data_pattern(item)
            print(f"Insertion N°{index} effectuée")
            # audio.streams.get_audio_only().download(output_path=output_path)

    @staticmethod
    def select_path_and_download_audio(link):
        """This function allows the user to select a path
        from explorer then download Youtube link to
        chosen path.
        Returns:
            .mp4: Audio from youtube link as .mp4
        """
        path = filedialog.askdirectory()

        YoutubeDlModel.download_audio(link, path)

    @ staticmethod
    def download_from_list_audio():
        """This function allows the user to download
        audio.mp4 from a list of link register in
        text document.
        """
        path = filedialog.askopenfilename()
        first_list = []
        with open(path, "r", encoding='utf-8') as f:
            for element in f:
                first_list.append(element.strip())
                filtered_list = list(filter(None, first_list))

            output_path = filedialog.askdirectory()
            datas = []
            for link in filtered_list:
                datas.append(YoutubeDlModel.download_audio_from_text_list(
                    link, output_path))

            print("DATA AVANT TRIE", datas)
            new_list = []
            for sublist in datas:
                new_list.extend(sublist)
            datas = new_list
            print("RESULTAT APRES TRIE", datas)
            YoutubeDlModel.insert_data_from_text_list(datas)

    @staticmethod
    def download_video(link, output_path):
        """
        Choose the right audio method based on a youtube playlist or simple URL
            """
        if YoutubeDlModel.PLAYLIST_TAG in link:
            print("Video: C'est une playlist:")
            print(link)
            index = 0
            urls = []
            for audio in Playlist(link).videos:
                urls.append(audio.watch_url)

            datas = []
            for element in urls:
                index += 1
                element_to_append = DataInfo.collect_playlist_url_data_pattern(
                    YouTube(element).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first(), element, index)
                datas.append(element_to_append)

            print(datas)
            dl = DataInfo()

            index = 0
            for item in datas:
                print("début de boucle")
                # insert_single_url_data_pattern(item)
                index += 1
                time.sleep(1)
                dl.table.insert("", "end", values=(
                    item["N°"], item["Title"], item["Size"],
                    item["Duration"], item["Completed"]))
                # dl.insert_single_url_data_pattern(item)
                print(f"Insertion N°{index} effectuée")
                # audio.streams.get_audio_only().download(output_path=output_path)
                # video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=output_path)

        else:
            print("Video: C'est un simple lien")
            print(link)
            dl = DataInfo()
            # YouTube(link).streams.filter(progressive=True).order_by('resolution').desc().first().download(output_path=output_path)
            dl.add_single_video_data_in_table(link)

    @staticmethod
    def download_video_from_text_list(link, output_path):
        """
        Choose the right audio method based on a youtube playlist or simple URL
        """
        datas = []

        if YoutubeDlModel.PLAYLIST_TAG in link:
            print("Audio: C'est une playlist:")
            print(link)
            index = 0
            urls = []
            for audio in Playlist(link).videos:
                urls.append(audio.watch_url)

            for element in urls:
                index += 1
                element_to_append = DataInfo.collect_playlist_url_data_pattern(
                    YouTube(element).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first(), element, index)
                datas.append(element_to_append)

        else:
            print("Video: C'est un simple lien")
            print(link)
            datas.append(DataInfo.get_audio_data_from_single_url(link))

        print("DATA APRES TELECHARGEMENT", datas)

        return datas

    @ staticmethod
    def select_path_and_download_video(link):
        """This function allows the user to select a path
        from explorer then download Youtube link to
        chosen path.
        Returns:
            .mp4: Audio from youtube link as .mp4
        """
        path = filedialog.askdirectory()
        YoutubeDlModel.download_video(link, path)

    @ staticmethod
    def download_from_list_video():
        """This function allows the user to download
        audio.mp4 from list of link register in text
        document.
        """
        path = filedialog.askopenfilename()
        first_list = []
        with open(path, "r", encoding='utf-8') as f:
            for element in f:
                first_list.append(element.strip())
                filtered_list = list(filter(None, first_list))

            output_path = filedialog.askdirectory()
            datas = []
            for link in filtered_list:
                datas.append(YoutubeDlModel.download_video_from_text_list(
                    link, output_path))

            print("DATA AVANT TRIE", datas)
            new_list = []
            for sublist in datas:
                new_list.extend(sublist)
            datas = new_list
            print("RESULTAT APRES TRIE", datas)
            YoutubeDlModel.insert_data_from_text_list(datas)
