from pytube import Playlist, YouTube
from tkinter import filedialog
import time
from data_view import DataInfo


class YoutubeDlModel:
    PLAYLIST_TAG = "https://www.youtube.com/playlist?list="

    @staticmethod
    def choose_audio_or_video(choice, element):
        """Will choose approriate method to download audio or video
        """
        if choice == 'audio':
            return YouTube(element).streams.filter(only_audio=True).first()
        elif choice == 'video':
            return YouTube(element).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    @staticmethod
    def download_audio_or_video(link, output_path, choice):
        """
        Choose the right patter to download Youtube Playlist or single Url
        """

        if YoutubeDlModel.PLAYLIST_TAG in link:
            print(f"{choice}:It's a playlist:")
            print(link)
            index = 0
            urls = []
            for audio in Playlist(link).videos:
                urls.append(audio.watch_url)

            datas = []
            for element in urls:
                index += 1
                element_to_append = DataInfo.collect_url_data_pattern(
                    YoutubeDlModel.choose_audio_or_video(choice, element), element, index)
                datas.append(element_to_append)

            print(datas)
            dl = DataInfo()

            index = 0
            for item in datas:
                print("Starting loop")
                index += 1
                time.sleep(1)
                dl.table.insert("", "end", values=(
                    item["N°"], item["Title"], item["Size"],
                    item["Duration"], item["Completed"]))
                print(f"Insert N°{index} done")

        else:
            print(f"{choice}: It's a simple link")
            print(link)
            dl = DataInfo()
            dl.add_single_audio_or_video_data_in_table(link, choice)

    @staticmethod
    def download_audio_or_video_from_text_list(link, output_path, choice):
        """
        Will choose approriate method to download audio or video from a list.txt
        """
        datas = []

        if YoutubeDlModel.PLAYLIST_TAG in link:
            print(f"{choice}:It's a playlist:")
            print(link)
            index = 0
            urls = []
            for audio in Playlist(link).videos:
                urls.append(audio.watch_url)

            for element in urls:
                index += 1
                element_to_append = DataInfo.collect_url_data_pattern(
                    YoutubeDlModel.choose_audio_or_video(choice, element), element, index)
                datas.append(element_to_append)

        else:
            print(f"{choice}: It's a simple link")
            print(link)
            datas.append(
                DataInfo.get_audio_or_video_data_from_single_url(link, choice))

        print("DATA APRES TELECHARGEMENT", datas)

        return datas

    @staticmethod
    def insert_data_from_text_list(datas):
        """Use DataInfo class to collect and insert data in a table after 
        download
        """
        dl = DataInfo()

        index = 0
        for item in datas:
            print("Starting loop")
            index += 1
            time.sleep(1)
            dl.table.insert("", "end", values=(
                index, item["Title"], item["Size"],
                item["Duration"], item["Completed"]))
            print(f"Insert N°{index} done")

    @staticmethod
    def select_path_to_download_audio_or_video(link, choice):
        """This function allows the user to select a path
        from explorer then download Youtube link to
        chosen path.
         """
        path = filedialog.askdirectory()

        YoutubeDlModel.download_audio_or_video(link, path, choice)

    @ staticmethod
    def download_from_text_list_audio_or_video(choice):
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
                datas.append(YoutubeDlModel.download_audio_or_video_from_text_list(
                    link, output_path, choice))

            print("DATA BEFORE SORTING", datas)
            new_list = []
            for sublist in datas:
                new_list.extend(sublist)
            datas = new_list
            print("RESULTAT AFTER SORTING", datas)
            YoutubeDlModel.insert_data_from_text_list(datas)
