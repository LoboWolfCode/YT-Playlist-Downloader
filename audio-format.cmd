@echo off
doskey yt_mp3=python -m yt_dlp -x --audio-format xyz -i -o "LOCATION OF FOLDER YOU WANT TO DOWNLOAD MUSIC TO\%%(title)s.xyz" $* YT_URL

'--audio-format xyz' --> choose the exact file type from the specified youtube video
