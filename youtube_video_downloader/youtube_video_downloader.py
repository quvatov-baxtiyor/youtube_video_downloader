from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download(url,save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")
        highest_resolution =streams.get_highest_resolution()
        highest_resolution.download(output_path=save_path)
        print("Video Downloaded Successfully")
    except Exception as e:
        print(e)

# url = "https://youtu.be/kVgy1GSDHG8?si=vEmtOexQ7f1ccFRW"
# save_path = "C:/Users/TEXNO/OneDrive/Desktop"
#
# download(url,save_path)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder : {folder}")
    return folder



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter a Youtube video url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started downloading video...")
        download(video_url, save_dir)
    else:
        print("Please select a folder...")