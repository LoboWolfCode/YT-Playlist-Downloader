@echo off
doskey yt_mp3=python -m yt_dlp -x --audio-format mp3 -i -o "D:\Music\%%(title)s.mp3" $*