from .downloadYoutube import download_youtube_video
from .slideVideo import slide_video

def whole_process(url):
    title, description = download_youtube_video(url)
    slide_video('videos','downloadedVideo', 'images')
    return title, description
