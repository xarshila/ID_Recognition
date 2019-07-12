import pytesseract as tes
import cv2
import numpy as np

class TesseractOcr:
    def __init__(self):
        pass

    def read(self, image, lang, meta):
        image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        config = ""
        v_start, v_end = meta["v_crop_start"], meta["v_crop_end"] 
        if "config" in meta:
            config = meta["config"]
        thresh = meta["threshold"] * np.average(image_gray[:,v_start : v_end])
        val, segment_img_thresh  = cv2.threshold(image_gray, thresh, 255,cv2.THRESH_BINARY)
        return tes.image_to_string(segment_img_thresh, lang = lang, config = config)

Ocr = TesseractOcr