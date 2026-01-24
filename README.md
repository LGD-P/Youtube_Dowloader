# Youtube download V2
 - Thanks to yt-dlp community ! ==> https://github.com/yt-dlp/yt-dlp 

_This project is an improvement of an older, one Youtube_Playlist_Downloader_

- Download Youtube audio or video:
  - from unique url
  - from list of url.txt
  - from Youtube playlist
- It's running with Python 3.12 using pip package manager

<p align='center'>
    <a href="https://www.python.org/downloads/release/python-3120/">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width=40/> 
    </a>
    <a href='https://pypi.org/project/yt-dlp/'>
        <img src="https://pypi-camo.freetls.fastly.net/3c2758eb3b3558e44faa489e5a2eca40f4371c78/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f79742d646c702f79742d646c702f6d61737465722f2e6769746875622f62616e6e65722e737667" width=180/>
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
- Simple confirmation message after download
- Manage error

 <p align='center'>
    <a >
        <img src="assets\frame0\error_message.png" width="50%"> 
    </a>
    
 </p>

## Technical changes:

- **Migration from pytube to yt-dlp with ffmpeg**: To avoid recurrent update problems and ensure better compatibility with YouTube changes, the project now uses yt-dlp as the main downloader library, combined with ffmpeg for audio/video processing. This provides more reliable downloads and supports a wider range of formats without frequent library updates.

- ⚠️⚠️⚠️ **FFmpeg integration**:  <strong>ffmpeg is not included in the distribution, download the full ffmpeg build from https://ffmpeg.org/download.html, unzip it, and place the entire `ffmpeg-8.0.1-full_build` directory in the current project folder. The application will automatically detect and use it for audio conversion and video processing.</strong>⚠️⚠️⚠️

- **Multilingual assets**: The assets folder contains versions of buttons and interface elements in both English and French to accommodate different users. The application automatically selects the appropriate language based on system settings or user preference.

## Install project:

### Clone project:

    git clone https://github.com/LGD-P/Youtube_Playlist_Downloader_V2.git

### Install Python dependencies:

    pip install -r requirement.txt

### Run project:

    python main.py

### Run the project with powershell : 

*just create a run.ps1 file*

```Powershell
cd "Path-to-your-dir-app"
python main.py
```
- *a simple right click & execute with powershell will run it*

### Run the project with batch command :

- *Just create a run.txt file*

```batch
@echo off
set "APP_DIR=Path-to-your-dir-app"
cd /d %APP_DIR%
start /min cmd /k "python main.py"
```
- *and then save it as run.bat and double click to run*



### You can auto-py-to-exe this project:

- *Use requirement.txt and pip env to compile*
- *Don't forget to add assets folder, ffmpeg directory, and additional files*

#### Using the provided config.json:

A pre-configured `config.json` file is included in the project root. This file contains all the necessary settings for auto-py-to-exe to compile the application into a standalone executable.

1. Open auto-py-to-exe.
2. Click on "Import Config From JSON" and select the `config.json` file from the project directory.
3. Replace all `<Path-to-your-project>` placeholders in the config with the actual absolute path to your project folder (e.g., `C:/Users/YourName/Desktop/Youtube_Dowloader`).
4. Click "Convert .py to .exe" to build the executable.

The config includes:
- **Datas**: Includes assets, ffmpeg directory, and necessary Python files.
- **Binaries**: Includes ffmpeg executables for audio/video processing.
- **Options**: Set to build a folder-based executable (not onefile) with console hidden, and other optimizations.

After compilation, you'll get a `main.exe` and `_internal` folder that can be packaged with Inno Setup or similar for distribution.

### Information : 


*This application 100% free and opensource, designed to facilitate the downloading of audio or video content from YouTube. However, users must be aware that the author's rights must be considered when using this app. It is important to respect copyright laws and the terms of service of YouTube and any other platform from which content is downloaded. The author disclaims any responsibility for unauthorized or improper use of this application. Users are encouraged to use this app responsibly and legally.*
