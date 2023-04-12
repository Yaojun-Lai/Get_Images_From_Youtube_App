import os
from pytube import YouTube
def download_youtube_video(url, output_file_name):
    yt = YouTube(url)

    # Get the highest resolution video stream
    video = yt.streams.get_highest_resolution()

    if not os.path.exists('videos'):
      os.makedirs('videos')
    # Download the video with a custom file name
    
    video.download('videos', filename=output_file_name)
# print('Please input the url:')
# youtube_url = input()
# # youtube_url="https://www.youtube.com/watch?v=TQ2K1XTCusc"

# # Optionally, provide a save path if you want to save the video to a specific location
# download_youtube_video(youtube_url, 'test')