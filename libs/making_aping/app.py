# https://qiita.com/yuuuu3/items/6e4206fdc8c83747544b
import os
import subprocess

import cv2
import numpy as np
from isort import file

save_folde_ar_view = "upload"
# ffmpeg -i input.mp4 -vcodec png -r 10 image_%04d.png
class ApngMaker:
    def __init__(self, file, file_info_color):
        print("ファイルは、", file)
        print("カラー情報は", file_info_color)
        print("カラー情報は[0]", file_info_color[0])
        stream = file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)
        # 白色部分に対応するマスク画像を作る
        mask = np.all(
            img[:, :, :]
            == [
                int(file_info_color[2]),
                int(file_info_color[1]),
                int(file_info_color[0]),
            ],
            axis=-1,
        )
        # 元画像をBGR形式からBGRA形式に変換
        dst = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        # マスク画像をもとに、白色部分を透明
        dst[mask, 3] = 0
        # png画像として出力
        cv2.imwrite(os.path.join("upload", "photoframe.png"), dst)
