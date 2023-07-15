# Code for converting from mp4 type to mp3 type

import moviepy.editor
from pathlib import Path

video_file = Path('my_video_test.mp4') # getting the path to the video file

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')
