# ManyHats Clipper

ManyHats Clipper is used to download clips from websites. It uses yt-dlp, so this tool should support whatever that library supports. Input the URL, and the start and end timestamps, and the tool should download it.

This is a CLI tool, with plans to connect to a frontend interface.

# Usage
```
usage: main.py [-h] [-start START] [-end END] [-max MAX_HEIGHT] url

ManyHats Clipper - Make clips of videos from websites

positional arguments:
  url                   Link to the video

options:
  -h, --help            show this help message and exit
  -start START, --start START
                        Starting timestamp of the video
  -end END, --end END   Ending timestamp of the video
  -max MAX_HEIGHT, --max_height MAX_HEIGHT
                        Set the resolution of the downloaded clip (example, 720, 1080, 480)
```
