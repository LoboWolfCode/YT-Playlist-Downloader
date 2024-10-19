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
