from pytube import YouTube

yt = YouTube()
yt.url = "https://www.youtube.com/watch?v=27ob2G3GUCQ"
print("影片原始名稱：" + yt.filename)
yt.set_filename("小魔術一")
print("影片下載名稱：" + yt.filename)
print("所有影片格式：" + str(yt.get_videos()))
print("型態為 mp4 的影片：" + str(yt.filter("mp4")))
video = yt.get("mp4", "360p")
video.download("d:\\tem")
print("下載檔案存於 d:\\tem 資料夾，檔案名稱為「小魔術一.mp4」")
