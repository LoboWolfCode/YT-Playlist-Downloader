@echo off
doskey yt_mp3=python -m yt_dlp -x --audio-quality 0 -i -o "LOCATION OF FOLDER YOU WANT TO DOWNLOAD MUSIC TO\%%(title)s.xyz" $* YT_URL

'--audio-quality 0' --> choose the highest quality audio file from the specified youtube video
