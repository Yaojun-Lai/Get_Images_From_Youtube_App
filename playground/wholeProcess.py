from .downloadYoutube import download_youtube_video
from .slideVideo import slide_video

def whole_process(url):
    download_youtube_video(url, 'test')
    slide_video('videos','test', 'images')

