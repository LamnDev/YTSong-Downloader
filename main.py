import yt_dlp

yt_link = input("URL: ")

ydl_opts = {
  'format': 'mp3/bestaudio/best',
  'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
  }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  ydl.download(yt_link)