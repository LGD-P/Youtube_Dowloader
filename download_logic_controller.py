from pytube import Playlist, YouTube
from tkinter import filedialog
import os

from pytube.exceptions import PytubeError

from error_message_gui_controller import ErrorMessagePopup
from data_gui_controller import DataInfo
from file_reader_controller import read_any_file_and_return_list


class YoutubeDlModel:
    PLAYLIST_TAG = "https://www.youtube.com/playlist?list="

    @staticmethod
    def open_download_folder(output_path):
        "Open downloading folder & allow user to check progress"
        os.startfile(output_path)


    def choose_audio_or_video(choice, output_path, element):
        """Will choose appropriate method to download audio or video
        """

        if choice == 'audio':
            return YouTube(element).streams.filter(only_audio=True).first()

        elif choice == 'video':
            return YouTube(element).streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first()

    @staticmethod
    def extract_data_from_youtube_playlist(link, output_path, choice):
        """Extract and return data from a simple url"""
        print(f"{choice}:It's a playlist:")
        print(link)
        index = 0
        urls = []
        for audio in Playlist(link).videos:
            urls.append(audio.watch_url)

        datas = []
        for element in urls:
            index += 1

            object_dl = YoutubeDlModel.choose_audio_or_video(
                choice, output_path, element)
            object_dl.download(output_path)
            YoutubeDlModel.open_download_folder(output_path)
            element_to_append = DataInfo.collect_url_data_pattern(object_dl, output_path, element, int(index))
            datas.append(element_to_append)

        print(datas)
        return datas

    @staticmethod
    def download_audio_or_video(link, output_path, choice):
        """
        Choose the right pattern to download Youtube Playlist or single Url
        """
        try:
            if not link: # Avoid DataInfo to appear
                return False, ErrorMessagePopup()

            if YoutubeDlModel.PLAYLIST_TAG in link:

                datas = YoutubeDlModel.extract_data_from_youtube_playlist(link, output_path, choice)
                print('DATA = ', datas)
                DataInfo.insert_data_from_text_list(datas)

            else:
                print(f"{choice}: It's a simple link")
                print(link)

                file = YoutubeDlModel.choose_audio_or_video(choice, output_path, link)
                file.download(output_path)
                YoutubeDlModel.open_download_folder(output_path)
                info_gui = DataInfo()
                data_collected = info_gui.collect_url_data_pattern(file,output_path,link,1)
                info_gui.add_single_audio_or_video_data_in_table(data_collected)

        except (Exception, PytubeError) as e:
            print(e)
            ErrorMessagePopup()



    @staticmethod
    def extract_data_from_text_list(link, output_path, choice):
        """
        From a list.txt will choose appropriate method to extract data
        """
        try:
            datas = []

            if YoutubeDlModel.PLAYLIST_TAG in link:
                datas = YoutubeDlModel.extract_data_from_youtube_playlist(link, output_path, choice)

            else:
                print(f"{choice}: It's a simple link")
                print(link)
                object_dl = YoutubeDlModel.choose_audio_or_video(choice, output_path, link)

                object_dl.download(output_path)
                datas.append(DataInfo.collect_url_data_pattern(object_dl,output_path,link,1))

            print("DATA APRES TELECHARGEMENT", datas)
            return datas

        except (Exception, PytubeError) as e:
            ErrorMessagePopup()
            print(e)


    @staticmethod
    def select_path_to_download_audio_or_video(link, choice):
        """This method allows the user to select a path
        from explorer then download Youtube link to the
        chosen path.
         """
        output_path = filedialog.askdirectory()
        if not output_path:
            return False
        YoutubeDlModel.download_audio_or_video( link, output_path, choice)


    @ staticmethod
    def read_txt_file_and_download(choice):
        """This method allows the user to download
        audio.mp4 or video.mp4 from a list.txt 
        """
        try:
            path = filedialog.askopenfilename()
            if not path:
                return False

            list_result = read_any_file_and_return_list(path)

            if type(list_result) != list:
                ErrorMessagePopup()
                return False

            output_path = filedialog.askdirectory()

            YoutubeDlModel.open_download_folder(output_path)
            datas = []

            for link in list_result:
                datas.append(YoutubeDlModel.extract_data_from_text_list(
                link, output_path, choice))

            print("DATA BEFORE SORTING", datas)
            new_list = []
            for sublist in datas:
                new_list.extend(sublist)
            datas = new_list
            print("RESULTAT AFTER SORTING", datas)
            DataInfo.insert_data_from_text_list(datas)

        except (Exception, PytubeError):
            return ErrorMessagePopup()


