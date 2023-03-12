from pytube import YouTube
#pip install pytube

url = "https://youtu.be/6zf2dNLS-fs"

YouTube(url).streams.first().download()
