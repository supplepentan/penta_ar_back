import subprocess
from distutils.file_util import move_file

import cv2

save_folde_ar_view = "upload"
# ffmpeg -i input.mp4 -vcodec png -r 10 image_%04d.png
class Movie:
    def __init__(self, movie_file):
        print(type(movie_file))
        # cap = cv2.VideoCapture(movie_file)
