import os
from pytube import YouTube
def download_youtube_video(url, video_output_path = 'videos', video_output_file_name='downloadedVideo'):
    try:
      yt = YouTube(url)

      # Get the highest resolution video stream
      video = yt.streams.get_highest_resolution()

      if not os.path.exists(video_output_path):
        os.makedirs(video_output_path)
      
      video.download(video_output_path, filename=video_output_file_name)
      # Save the title and description to a file
      with open(os.path.join(video_output_path,video_output_file_name+'_info.txt'), 'w', encoding='utf-8') as f:
          f.write('Title: {}\n'.format(yt.title))
          f.write('Description: {}\n'.format(yt.description))
      return yt.title, yt.description
    except Exception as e:
        print(f"Error: the video is unavaliable")
    

    # audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    # audio_stream.download(output_path=audio_output_path, filename=audio_output_file_name)