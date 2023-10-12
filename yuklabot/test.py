import os
import subprocess
from pytube import YouTube
from PIL import Image
from io import BytesIO
import requests

def download_video(url):
    # Create a YouTube object
    yt = YouTube(url)

    # Display available video qualities to the user
    print("Available video qualities:")
    for i, stream in enumerate(yt.streams.filter(file_extension="mp4")):
        print(f"{i + 1}. {stream.resolution} - {stream.mime_type}")

    # Ask the user to select a quality
    choice = int(input("Enter the number of the desired video quality: ")) - 1

    # Download the selected video to the current working directory
    video = yt.streams.filter(file_extension="mp4")[choice]
    video.download()
    print("Video downloaded successfully!")

def download_audio(url):
    # Create a YouTube object
    yt = YouTube(url)

    # Download the audio to the current working directory
    audio = yt.streams.get_audio_only().download()
    print("Audio downloaded successfully!")

def download_thumbnail(url):
    # Create a YouTube object
    yt = YouTube(url)

    # Get the thumbnail URL
    thumbnail_url = yt.thumbnail_url

    # Download the thumbnail image to the current working directory
    response = requests.get(thumbnail_url)
    img = Image.open(BytesIO(response.content))
    img.save("thumbnail.jpg")
    print("Thumbnail downloaded successfully!")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")

    print("Options:")
    print("1. Download Video")
    print("2. Download Audio")
    print("3. Download Thumbnail")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        download_video(url)
    elif choice == 2:
        download_audio(url)
    elif choice == 3:
        download_thumbnail(url)
    else:
        print("Invalid choice. Please select a valid option (1, 2, or 3).")
