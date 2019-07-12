import pytesseract as tes
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ocr.ocr import Ocr

class TemplateReader:

    def __init__(self, template, debug=False):
        self.debug = debug
        self.template = template
        self.ocr = Ocr()
        
    def readSegments(self, segments):
        result = {}
        if self.debug:
            result["field"] = {}
        for name in segments:
            segment = segments[name]
            segment_img = self.template[segment['y1'] : segment['y2'], segment['x1']  : segment['x2']]
            if "do_not_read" not in segment:
                segment_text = self.ocr.read(segment_img, segment["lang"], segment)
                result[name] = segment_text
                if self.debug:
                    result["field"][name] = segment_img
            else:
                if self.debug:
                    result[name] = segment_img
        return result;