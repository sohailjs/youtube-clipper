import subprocess

def clip_youtube_video(url, start_time, end_time, output_file="clip.mp4"):
    # Get the direct streaming URL (best quality video+audio)
    stream_url = (
        subprocess.check_output(["yt-dlp.exe", "-f", "best", "-g", url])
    )

    # Calculate duration from start & end timestamps (HH:MM:SS)
    def time_to_seconds(t):
        h, m, s = map(int, t.split(":"))
        return h * 3600 + m * 60 + s

    duration = str(time_to_seconds(end_time) - time_to_seconds(start_time))

    # Run ffmpeg clip command
    command = [
        "ffmpeg",
        "-ss", start_time,
        "-i", stream_url,
        "-t", duration,
        "-c", "copy",  # no re-encoding -> fast, keep HD
        "-y",          # overwrite file
        output_file
    ]

    subprocess.run(command)
    print("🎉 Clip saved to:", output_file)


if __name__ == "__main__":
    youtube_url = input("Enter YouTube Video URL: ")
    start = input("Start time (HH:MM:SS): ")
    end = input("End time (HH:MM:SS): ")

    clip_youtube_video(youtube_url, start, end)
