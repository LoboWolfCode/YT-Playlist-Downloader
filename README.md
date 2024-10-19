# YT-Playlist-Downloader
Download your entire YouTube playlist in seconds, in your preferred file format. It's as easy as a single command.

Primarily using the `yt-dlp` package, I've simplified the process of bulk downloading videos and songs in your preferred format.

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

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
