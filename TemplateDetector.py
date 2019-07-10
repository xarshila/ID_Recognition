import sys
import numpy as np
import cv2 
import random
import matplotlib.pyplot  as plt
import glob
import pytesseract as tes
from PIL import Image
from passporteye import read_mrz


class TemplateDetector:

    def __init__(self, template):
        self.akaze = cv2.AKAZE_create()
        self.template = template
        self.template_keypoints, self.template_desc = self.akaze.detectAndCompute(template,None)

    def detect(self, query_image):
        image_original = query_image
        image = query_image
        kp2, des2 = self.akaze.detectAndCompute(image,None)

        flann = cv2.BFMatcher(cv2.NORM_HAMMING)

        matches = flann.knnMatch(self.template_desc, des2, k=2)


        # store all the good matches as per Lowe's ratio test.
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)

        src_pts = np.float32([self.template_keypoints[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()
        
        h,w = self.template.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)
        detected_area = cv2.polylines(image,[np.int32(dst)],True,255,3, cv2.LINE_AA)



        result_warp = cv2.warpPerspective(image_original, np.linalg.inv(M), (w, h))
        result = {}
        result["warp"] = result_warp

        return result