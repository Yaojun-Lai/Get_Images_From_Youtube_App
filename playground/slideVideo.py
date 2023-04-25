import os
def slide_video(filepath='videos', filename='downloadedVideo', output_path='images'):
  if not os.path.exists(output_path):
      os.makedirs(output_path)
  cmd = 'ffmpeg -i {}/{} -vf fps=1 {}/%04d.png'.format(filepath, filename, output_path)
  os.system(cmd)