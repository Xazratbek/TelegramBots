# import yt_dlp

# # Create a yt-dlp instance
# ydl_opts = {
#     'format': 'bestaudio/best',
#     'outtmpl': '%(title)s.%(ext)s',
# }
# ydl = yt_dlp.YoutubeDL(ydl_opts)

# # Search for a track on YouTube
# track_name = 'Asl Wayne G\'animat'
# search_query = f'{track_name} official audio'
# search_results = ydl.extract_info(f'ytsearch:{search_query}', download=False)

# # Download the first result (best audio)
# if search_results['entries']:
#     first_result = search_results['entries'][0]
#     track_url = first_result['url']
#     ydl.download([track_url])
# else:
#     print("Track not found on YouTube.")
