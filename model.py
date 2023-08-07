from pytube import YouTube, Playlist
from tkinter import filedialog


class YoutubeDlModel:
    PLAYLIST_TAG = "https://www.youtube.com/playlist?list="

    @staticmethod
    def download_audio(link, output_path):
        """
        Choose the right audio method based on a youtube playlist or simple URL
        """
        if YoutubeDlModel.PLAYLIST_TAG in link:
            print("C'est une playlist:")
            print(link)
            for audio in Playlist(link).videos:
                print(audio.embed_url)
                audio.streams.get_audio_only().download(output_path=output_path)

        else:
            print("C'est un simple lien")
            print(link)
            YouTube(link).streams.get_audio_only().download(
                output_path=output_path)

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

            for link in filtered_list:
                YoutubeDlModel.download_audio(link, output_path)

    @staticmethod
    def download_video(link, output_path):
        """
        Choose the right audio method based on a youtube playlist or simple URL
        """
        if YoutubeDlModel.PLAYLIST_TAG in link:
            print("C'est une playlist:")
            print(link)
            for video in Playlist(link).videos:
                print(video.embed_url)
                video.streams.filter(progressive=True, file_extension='mp4').order_by(
                    'resolution').desc().first().download(output_path=output_path)

        else:
            print("C'est un simple lien")
            print(link)
            YouTube(link).streams.filter(progressive=True).order_by(
                'resolution').desc().first().download(output_path=output_path)

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
            path_to_download = filedialog.askdirectory()
            for link in filtered_list:
                print(link)
                YoutubeDlModel.download_video(link, path_to_download)
