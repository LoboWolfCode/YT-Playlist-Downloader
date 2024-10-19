import subprocess
import sys

def yt_avsl(url, output_path, file_type):
    # Construct the output template based on the file type
    output_template = f"{output_path}/%(title)s.%(ext)s" if output_path else "%(title)s.%(ext)s"
    command = [
        "python", "-m", "yt_dlp", 
        "-x",  # Extract audio
        "--audio-format", file_type,  # Specify the file type
        "-o", output_template, 
        url
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python yt_avsl.py <URL> <output_path> <file_type>")
    else:
        url = sys.argv[1]
        output_path = sys.argv[2]
        file_type = sys.argv[3]
        yt_avsl(url, output_path, file_type)