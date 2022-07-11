import subprocess

save_folde_ar_view = "upload"
# ffmpeg -i input.mp4 -vcodec png -r 10 image_%04d.png
class ApngMaker:
    def __init__(self):
        cmd = [
            "ffmpeg," "-i",
            "input.mp4",
            "-vcodec",
            "png",
            "-r",
            "10",
            "image_%04d.png",
        ]
        print("movie_file")
        # cap = cv2.VideoCapture(movie_file)
