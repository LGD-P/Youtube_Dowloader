# Youtube download V2
 - Thanks to pytube community ! ==> https://github.com/pytube/pytube 

_This project is an improvement of an older, one Youtube_Playlist_Downloader_

- Download Youtube audio or video:
  - from unique url
  - from list of url.txt
  - from Youtube playlist
- It's running with Python 3.11 using Poetry package manager

<p align='center'>
    <a href="https://www.python.org/downloads/release/python-3110/">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width=40/> 
    </a>
    <a href='https://python-poetry.org/'>
        <img src="https://python-poetry.org/images/logo-origami.svg" width=30/>
    </a>
 </p>

## Graphic improvement:

- Complete graphic redesign.
- Thanks to ==> https://github.com/ParthJadhav/Tkinter-Designer, which greatly simplified my life for placing the elements of my app. A project to visit and test without hesitation !!!\*


<p align='center'>
    <img src="assets\frame0\audio_look.png" width=300>
    <img src="assets\frame0\video_look.png" width=300>
</p>

## New features:

- Switch between Audio and Video downloading
- Youtube Playlist are now supported 
- More file format supported for your own lists : 
    * ".txt", ".odt", ".ods", ".docx", ".xlsx"
    * Do not give headers to your  ".ods" & ".xlsx" table 
- Recap TreeView of file downloaded
- Manage error

 <p align='center'>
    <a >
        <img src="assets\frame0\error_message.png" width="50%"> 
    </a>
    
 </p>

## Install project:

### Clone project:

    git clone https://github.com/LGD-P/Youtube_Playlist_Downloader_V2.git

### Install Poetry dependency management:

    pip install poetry

### Active virtual environnement in your project:

    poetry shell

### Install dependencies:

    poetry install

### Run project in you IDE:

    python main.py

### Run the project with powershell : 

*just create a run.ps1 file*

```Powershell
cd "Path-to-your-dir-app"
poetry run python main.py
```
- *a simple right click & execute with powershell will run it*

### Run the project with batch command :

- *Just create a run.txt file*

```batch
@echo off
set "APP_DIR=Path-to-your-dir-app"
cd /d %APP_DIR%
start /min cmd /k "poetry run python main.py"
```
- *and then save it as run.bat and double click to run*



### You can auto-py-to-exe this project:

- *Prefer requirement.txt and pip env than pyproject.toml and poetry to compile*
- *Don't forget to add assets folder and additional files*



### Information : 


*This application 100% free and opensource, designed to facilitate the downloading of audio or video content from YouTube. However, users must be aware that the author's rights must be considered when using this app. It is important to respect copyright laws and the terms of service of YouTube and any other platform from which content is downloaded. The author disclaims any responsibility for unauthorized or improper use of this application. Users are encouraged to use this app responsibly and legally.*
