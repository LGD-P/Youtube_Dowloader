from pytube import YouTube
from tkinter import filedialog


class YoutubeDlModel:

    @staticmethod
    def select_path_and_download_audio(link):
        """This function allows the user to select a path
        from explorer then download Youtube link to
        chosen path.
        Returns:
            .mp4: Audio from youtube link as .mp4
        """
        path = filedialog.askdirectory()
        return YouTube(link).streams.get_audio_only().download(path)

    @staticmethod
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
            path_to_download = filedialog.askdirectory()
            for url in filtered_list:
                print(url)
                YouTube(url).streams.get_audio_only().download(
                    path_to_download)

    @staticmethod
    def select_path_and_download_video(link):
        """This function allows the user to select a path
        from explorer then download Youtube link to
        chosen path.
        Returns:
            .mp4: Audio from youtube link as .mp4
        """
        path = filedialog.askdirectory()
        return YouTube(link).streams.filter(progressive=True)\
            .get_highest_resolution().download(path)

    @staticmethod
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
            for url in filtered_list:
                print(url)
                YouTube(url).streams.filter(progressive=True).get_highest_resolution().download(
                    path_to_download)
