import pytesseract as tes
import cv2
import numpy as np
import matplotlib.pyplot as plt
class TemplateReader:

    def __init__(self, template):
        self.template = template
        
    def readSegments(self, segments):
        result = {}
        for name in segments:
            segment = segments[name]
            segment_img = self.template[segment['y1'] : segment['y2'], segment['x1']  : segment['x2']]
            if "do_not_read" not in segment:
                segment_img_gray = cv2.cvtColor(segment_img,cv2.COLOR_BGR2GRAY)
                v_start, v_end = segments[name]["v_crop_start"], segments[name]["v_crop_end"]
                thresh = segment["threshold"] * np.average(segment_img_gray[:,v_start : v_end])
                val, segment_img_thresh  = cv2.threshold(segment_img_gray, thresh, 255,cv2.THRESH_BINARY)
                config = ""
                if "config" in segment:
                    config = segment["config"]
                segment_text = tes.image_to_string(segment_img_thresh, lang = segment["lang"], config = config)
                result[name] = segment_text
                
                #result[name+"_img"] = segment_img_thresh
                #plt.imshow(segment_img_thresh)
                #plt.show()
                
            else:
               result[name] = segment_img
     
        return result;