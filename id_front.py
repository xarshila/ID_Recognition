import cv2
from TemplateDetector import TemplateDetector
import matplotlib.pyplot  as plt
from ID_CONSTS import *
from TemplateReader import TemplateReader
import os
class IdFrontProcessor:

    def __init__(self):
        template = cv2.imread("./id-template-front.png", 0)
        self.template_detector = TemplateDetector(template)
        self.segment_consts = ID_FRONT_CONSTS

    def process(self, image, fields):
        if  not fields:
            fields = ["name_ge", "name_en", "last_name_ge", "last_name_en", "card_id", "person_id", "exp_date", "birth_date", "nation", "sex", "photo"]
        segments = {}
        for field in fields:
            segments[field] = self.segment_consts[field]
        detected = self.template_detector.detect(image)
        reader = TemplateReader(detected["warp"])
        result = reader.readSegments(segments)
        return result

   