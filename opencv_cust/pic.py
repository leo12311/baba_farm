import cv2
from PIL import ImageGrab
import numpy as np
def find_pic(img_rgb,target_img,threshold):
    # 所有操作在灰度版中进⾏
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, target_img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        return (pt[0], pt[1])
    return None
