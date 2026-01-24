
import subprocess
from tkinter import filedialog
import os
import re
import tkinter.messagebox as messagebox
import sys

from error_message_gui_controller import ErrorMessagePopup
from file_reader_controller import read_any_file_and_return_list


class YoutubeDlModel:
    PLAYLIST_TAG = "https://www.youtube.com/playlist?list="

    @staticmethod
    def open_download_folder(output_path):
        "Open downloading folder & allow user to check progress"
        os.startfile(output_path)


    def choose_audio_or_video(choice, output_path, element):
        """Télécharge audio ou vidéo via yt-dlp. Utilise --ffmpeg-location pour pointer vers ffmpeg local."""
        import time
        import os

        # Pour éviter les téléchargements de playlist pour les liens avec &list=, supprimer le paramètre list et start_radio
        if 'list=' in element and 'youtube.com/playlist?' not in element:
            element = re.sub(r'&list=[^&]*', '', element)
            element = re.sub(r'&start_radio=[^&]*', '', element)

        # Détecter si c'est un exe PyInstaller
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        # Cherche ffmpeg local
        ffmpeg_local = os.path.join(base_path, 'ffmpeg.exe')
        if not os.path.isfile(ffmpeg_local):
            ffmpeg_local = os.path.join(base_path, 'ffmpeg-8.0.1-full_build', 'bin', 'ffmpeg.exe')
        ffmpeg_option = ['--ffmpeg-location', ffmpeg_local] if os.path.isfile(ffmpeg_local) else []

        if choice == 'audio':
            cmd = [
                'yt-dlp',
                '-f', 'bestaudio',
                '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
                '--extract-audio',
                '--audio-format', 'mp3',
                *ffmpeg_option,
                element
            ]
        elif choice == 'video':
            cmd = [
                'yt-dlp',
                '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
                *ffmpeg_option,
                element
            ]
        else:
            raise ValueError('Le choix doit être "audio" ou "video"')

        try:
            subprocess.run(cmd, check=True)
            return True
        except Exception as e:
            print(f"Erreur yt-dlp/pydub: {e}")
            ErrorMessagePopup()
            return False

    @staticmethod
    def extract_data_from_youtube_playlist(link, output_path, choice):
        """Télécharge tous les éléments d'une playlist YouTube via yt-dlp"""
        print(f"{choice}: It's a playlist:")
        print(link)
        # Récupère toutes les URLs de la playlist avec yt-dlp
        try:
            result = subprocess.run([
                'yt-dlp', '--flat-playlist', '--print', 'url', link
            ], capture_output=True, text=True, check=True)
            urls = [u.strip() for u in result.stdout.splitlines() if u.strip()]
        except Exception as e:
            print(f"Erreur extraction playlist: {e}")
            ErrorMessagePopup()
            return []

        for idx, element in enumerate(urls, 1):
            YoutubeDlModel.choose_audio_or_video(choice, output_path, element)
        YoutubeDlModel.open_download_folder(output_path)

    @staticmethod
    def download_audio_or_video(link, output_path, choice):
        """
        Utilise yt-dlp pour télécharger une vidéo ou une playlist
        """
        try:
            if not link:
                return False, ErrorMessagePopup()

            if YoutubeDlModel.PLAYLIST_TAG in link:
                YoutubeDlModel.extract_data_from_youtube_playlist(link, output_path, choice)
                messagebox.showinfo("Téléchargement", "Téléchargement terminé")
            else:
                print(f"{choice}: It's a simple link")
                print(link)
                file_path = YoutubeDlModel.choose_audio_or_video(choice, output_path, link)
                YoutubeDlModel.open_download_folder(output_path)
                messagebox.showinfo("Téléchargement", "Téléchargement terminé")
        except Exception as e:
            print(e)
            ErrorMessagePopup()



    @staticmethod
    def extract_data_from_text_list(link, output_path, choice):
        """
        Utilise yt-dlp pour télécharger depuis une liste
        """
        try:
            if YoutubeDlModel.PLAYLIST_TAG in link:
                YoutubeDlModel.extract_data_from_youtube_playlist(link, output_path, choice)
            else:
                print(f"{choice}: It's a simple link")
                print(link)
                YoutubeDlModel.choose_audio_or_video(choice, output_path, link)
        except Exception as e:
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

            for link in list_result:
                YoutubeDlModel.extract_data_from_text_list(link, output_path, choice)

            messagebox.showinfo("Téléchargement", "Téléchargement terminé")
            YoutubeDlModel.open_download_folder(output_path)

        except Exception:
            return ErrorMessagePopup()


