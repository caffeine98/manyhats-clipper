import argparse

import clipper
import utils

def main():
    parser = argparse.ArgumentParser(description="ManyHats Clipper - Make clips of videos from websites")
    parser.add_argument("url", help="Link to the video")
    parser.add_argument("-start", "--start", help="Starting timestamp of the video. (For example, 30s, 23m51s, 2h30m59s)")
    parser.add_argument("-end", "--end", help="Ending timestamp of the video. (For example, 30s, 23m51s, 2h30m59s,)")
    parser.add_argument("-max", "--max_height", help="Set the resolution of the downloaded clip (example, 720, 1080, 480)", type=int)
    args = parser.parse_args()

    start_time, end_time = 0, float("inf")  # End time = float("inf") means end of the video

    if args.start is not None:
        start_time = utils.parse_time(args.start)
    if args.end is not None: 
        end_time = utils.parse_time(args.end)
    
    if end_time <= start_time:
        parser.error("End time must be after start time")

    video_url = args.url
    
    # Call Clipper
    clip = clipper.Clipper(url=video_url, start_time=start_time, end_time=end_time)
    options = clip.options(max_height = args.max_height)
    clip.download(options)

if __name__ == "__main__":
    main()