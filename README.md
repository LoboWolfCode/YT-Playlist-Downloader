# YT-Playlist-Downloader
## Overview
Download your entire YouTube playlist in seconds, in your preferred file format. It's as easy as a single command.

Primarily using the `yt-dlp` package, I've simplified the process of bulk downloading videos and songs in your preferred format.

## Features

- Downloads audio from YouTube videos.
- Saves audio files in your desired file format.
- Files are saved to a predefined directory.

## Content Table (Ctrl-f to get your desired use-case code)

* Python Script - Customizable Terminal
* Python Script - Customizable Python
* CMD Guide

# Python Script - Customizable Terminal
This version of the script gives you more flexibility at the cost of a longer string. If you frequently modify file types or directories, the increased flexibility of this script version might outweigh the longer string.

WILL ADD LATER

```python
   import subprocess
import sys

def download_video(url, output_path, file_type):
    # Construct the output template based on the file type
    output_template = f"{output_path}/%(title)s.%(ext)s" if output_path else "%(title)s.%(ext)s"
    command = [
        "python", "-m", "yt_dlp", 
        "-f", file_type, 
        "-o", output_template, 
        url
    ]
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <URL> <output_path> <file_type>")
    else:
        url = sys.argv[1]
        output_path = sys.argv[2]
        file_type = sys.argv[3]
        download_video(url, output_path, file_type)

   ```

# Python Script - Customizable Python
This version of the script gives you a template where you can then change the file type, directory, then save and forget about it. It's shorter than the *Customizable Terminal*, which is good if you plan to download the same file types to the same directory.

## Requirements

- Python 3.x
- `yt-dlp` module (a fork of `youtube-dl`)
- FFmpeg (for audio extraction)

### Installation

1. **Install Python**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install yt-dlp**: Open a command prompt and run the following command:
   ```bash
   pip install yt-dlp
   ```
3. **Install FFmpeg**: 
   - Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).
   - Follow the installation instructions for your operating system.
   - Ensure that FFmpeg is added to your system's PATH so it can be accessed from the command line.
  
     * ffmpeg-7.x-essentials_build --> bin --> *Copy the directory*
     * *Open*: Edit the System Environment Variables --> Environment Variables --> *Select* Path *Edit* --> *New* Ctrl-v the ffmpeg directory

## Usage

1. **Clone or Download the Script**: Save the `yt_av.py` script to your *Users* directory name.

```python
import subprocess
import sys

def yt_av(url):
    # Set a fixed output path and file type
    output_path = r"D:\Music\Ipod"  # Directory for saving files
    file_type = "mp3"  # Desired file type

    # Construct the output template
    output_template = f"{output_path}/%(title)s.{file_type}"
    command = [
        "python", "-m", "yt_dlp", 
        "-x",  # Extract audio
        "--audio-format", "mp3",  # Specify audio format
        "-o", output_template, 
        url
    ]
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python yt_av.py <URL>")
    else:
        url = sys.argv[1]
        yt_av(url)
```
2. **Run the Script**: Use the command line to navigate to the directory where the script is saved. Run the script with the following command:
   ```bash
   python yt_av.py <YouTube_URL>
   ```

   Replace `<YouTube_URL>` with the URL of the video you want to download.

### Example

To download audio from a specific YouTube video, use:
```bash
python yt_av.py https://www.youtube.com/watch?v=example
```

This command will save the audio as an MP3 file in the `D:\Music\Ipod` directory.

## Customization

- You can modify the output path or file format directly in the script:
  ```python
  output_path = r"D:\Music\Ipod"  # Change this to your desired directory
  file_type = "mp3"  # Change this to your desired file type
  ```
- You can also modify the file format to simply be whichever is the highest it can download:
 ```bash
  Change --audio-format to --audio-quality 0
  ``` 

# CMD Guide
Alternatively to downloading the Python script, you can follow this laborious process to get it working without it :)

WILL ADD LATER








## Troubleshooting (All Sections)

- If you encounter errors, ensure that:
   - Python, `yt-dlp`, and FFmpeg are properly installed.
  - You have a valid YouTube URL.
  - You have write permissions to the specified output directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Feel free to customize the README further based on your preferences or any additional features you may want to highlight!




___________________________________________________________________________________________________OLD
## Installation (Python Script)
*This asks Python to tell us its version*

* Download [Python](https://www.python.org/downloads/) and ensure that pip is also installed.
 
**Test that Python and pip got installed:**

Open CMD

*This asks Python to tell us its version*
```bash
python --version
```
*This invokes pip's default behavior when called, which is typically equivalent to a CMD 'help'*
```bash
python -m pip
```

### Download the Script

```python
import subprocess
import sys
import os

def download_audio(url):
    output_path = r"D:\Music\%(title)s.mp3"
    command = [
        "python", "-m", "yt_dlp", 
        "-x", 
        "--audio-format", "mp3", 
        "-i", 
        "-o", output_path, 
        url
    ]
    
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        download_audio(url)
```

[Script](download_audio.py)

## Installation (To Use in CMD)

* Download [Python](https://www.python.org/downloads/) and ensure that pip is also installed.
 
**Test that Python and pip got installed:**

Open CMD

*This asks Python to tell us its version*
```bash
python --version
```
*This invokes pip's default behavior when called, which is typically equivalent to a CMD 'help'*
```bash
python -m pip
```

* Install yt_dlp
*This uses Python's pip and installs the 'yt_dlp' package*
```bash
python -m pip install yt_dlp
```

**Test that yt_dlp got installed:**

Open CMD
*Again, this asks yt_dlp, through python, what its version it is*
```bash
python -m yt_dlp --version
```

* Download [ffmpeg](https://ffmpeg.org/download.html#build-windows). *This is used for converting, streaming, editing, filtering, and managing metadata of audio and video files.*

Windows --> Windows builds from gyan.dev --> (Release Builds: ffmpeg-release-essentials.zip)

**Test that ffmpeg got installed:**
-------------------------------------------------------------moremoremoremoremore


