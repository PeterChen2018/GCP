from pytube import YouTube
yt = YouTube()
yt.url = "https://www.youtube.com/watch?v=27ob2G3GUCQ"
video = yt.get("mp4", "360p")
video.download("d:\\tem1")
