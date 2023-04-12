import os
def slide_video(filepath, filename, output_path):
  if not os.path.exists(output_path):
      os.makedirs(output_path)
  cmd = 'ffmpeg -i {}/{} -vf fps=1 {}/%04d.png'.format(filepath, filename, output_path)
  os.system(cmd)