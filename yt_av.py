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
