import shutil
from yt_dlp import YoutubeDL
from yt_dlp.utils import download_range_func

FFMPEG_PATH = shutil.which("ffmpeg")
if FFMPEG_PATH is None:
    raise Exception("ffmpeg is not installed, or the PATH cannot be found")

class Clipper():
    def __init__(self, url: str, start_time: float, end_time: float):
        self.url = url
        self.start_time = start_time
        self.end_time = end_time

    def options(self, max_height: int | None = None) -> dict:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "ffmpeg_location": FFMPEG_PATH,
            "outtmpl": "%(title).50s [%(id)s].%(ext)s",
            "windowsfilenames": True,
            "quiet": False,
            "noplaylist": True,
            "download_ranges": download_range_func(None, [(self.start_time, self.end_time)])    # float("inf") for end of video
        }

        if max_height is not None:
            ydl_opts["format_sort"] = [f"res:{max_height}"]

        return ydl_opts

    def download(self, options: dict):
        with YoutubeDL(options) as ydl:
            info = ydl.extract_info(url=self.url, download=False)
            info_title = info.get("title")
            info_url = info.get("webpage_url")
            info_duration = info.get("duration")
            print(f"Downloaded from url: {info_url}")
            print(f"Title: {info_title}, Duration: {info_duration}")
            ydl.download(url_list=[self.url])
