import sys
import numpy as np
import cv2 
import random
import matplotlib.pyplot  as plt
import glob
import pytesseract as tes
from PIL import Image


class TemplateDetector:

    def __init__(self, template, method="SIFT"):
        self.method = method
        if self.method == "AKAZE":
            self.feature_extractor = cv2.AKAZE_create()
        else:
            self.feature_extractor = cv2.xfeatures2d.SIFT_create()
        self.template = template
        self.template_keypoints, self.template_desc = self.feature_extractor.detectAndCompute(template,None)

    def detect(self, query_image):
        h,w = query_image.shape
        image_original = query_image
        image = query_image
        kp2, des2 = self.feature_extractor.detectAndCompute(image,None)
        if self.method == "AKAZE":
            flann = cv2.BFMatcher(cv2.NORM_HAMMING)
        else:
            flann = cv2.BFMatcher()
        matches = flann.knnMatch(self.template_desc, des2, k=2)


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
        depth = int(3 * (min(w,h)/800))
        detected_rect = cv2.polylines(image,[np.int32(dst)],True,255,depth, cv2.LINE_AA)

        result_warp = cv2.warpPerspective(image_original, np.linalg.inv(M), (w, h))
        result = {}
        result["warp"] = result_warp
        result["detected_rect"] = detected_rect
        return result


