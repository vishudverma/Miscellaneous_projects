"""
The recommended use case of pytube is deprecated so resolving to the use of `yt-dlp` for this project.
"""

import os
import tkinter as tk
from tkinter import filedialog

import yt_dlp  # pyright: ignore


def download_video(url: str, save_path=os.getcwd()):
    ydl_opts = {
        # 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        # Simple options for progressive mp4 (video+audio together):
        "format": "best[ext=mp4]",
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # pyright: ignore
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def open_file_dialogue():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialogue()

    if save_dir:
        print("Started download")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
