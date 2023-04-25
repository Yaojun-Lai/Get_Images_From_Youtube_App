from .downloadYoutube import download_youtube_video
from .slideVideo import slide_video

def whole_process(url):
    print('Downloading video ...')
    title, description = download_youtube_video(url)
    print('Succesfully downloaded video, begin sliding it')
    slide_video('videos','downloadedVideo', 'images')
    print('Succesfully slided video')
    return title, description
