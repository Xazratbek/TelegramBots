import yt_dlp

# Replace 'YOUR_TWITCH_VIDEO_URL' with the URL of the Twitch video you want to download
video_url = 'https://m.twitch.tv/videos/1738752819'

# Set yt-dlp options
ydl_opts = {
    'format': 'best',  # Choose the best available quality
    'outtmpl': '%(title)s.%(ext)s',  # Output file name format
    'quiet': True,  # Suppress yt-dlp output
    'no_warnings': True,  # Suppress warnings
}

def download_twitch_video(video_url, ydl_opts):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    download_twitch_video(video_url, ydl_opts)
