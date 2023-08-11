from pytube import Playlist
from pytube import YouTube, Playlist


URL = "https://www.youtube.com/watch?v=L-iepu3EtyE"
PLAYLIST_TEST = "https://www.youtube.com/playlist?list=PL-tdP6nrpQYtlJ6gYUeJvpdLd64O6MvoT"


def convert_duration(dur_in_sec):
    minutes = dur_in_sec // 60
    seconds = dur_in_sec % 60
    return f"{minutes} min {seconds} sec"


def collect_playlist_url_data_pattern(object_dl, url, n):
    object_dl.download()

    # Récupère les informations de la vidéo
    number = n
    title = YouTube(url).title
    duration = YouTube(url).length
    duration = convert_duration(duration)
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


def download_playlist_audio(link):
    """
    Choose the right audio method based on a youtube playlist or simple URL
    """
    PLAYLIST_TAG = "https://www.youtube.com/playlist?list="

    if PLAYLIST_TAG in link:
        print("Audio: C'est une playlist:")
        print(link)
        index = 0
        urls = []
        for audio in Playlist(link).videos:
            urls.append(audio.watch_url)

        datas = []
        for element in urls:
            index += 1
            element_to_append = collect_playlist_url_data_pattern(
                YouTube(element).streams.get_audio_only(), element, index)
            datas.append(element_to_append)

        return print(datas)


download_playlist_audio(PLAYLIST_TEST)
