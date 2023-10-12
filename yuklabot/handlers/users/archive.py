# import yt_dlp

# # Replace 'YOUR_ARCHIVE_URL' with the URL of the Archive.org item you want to download
# archive_url = 'https://archive.org/details/cinema-hd-v-2-v-2.3.7.3'

# # Set yt-dlp options
# ydl_opts = {
#     'format': 'best',  # Choose the best available quality
#     'outtmpl': '%(title)s.%(ext)s',  # Output file name format
#     'quiet': True,  # Suppress yt-dlp output
#     'no_warnings': True,  # Suppress warnings
# }

# def download_archive_item(archive_url, ydl_opts):
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         try:
#             ydl.download([archive_url])
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#     download_archive_item(archive_url, ydl_opts)
