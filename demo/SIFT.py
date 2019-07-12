import numpy as np
import cv2
import logging
from matplotlib import pyplot as plt
import sys

cap = cv2.VideoCapture(0)

sift = cv2.xfeatures2d.SIFT_create()
template = cv2.imread(sys.argv[1],0)
template_keypoints, template_desc = sift.detectAndCompute(template,None)


def pol_area(polygon):
    if not isinstance(polygon, np.ndarray) and polygon == None:
        return 0
    area =  polygon[len(polygon)-1][0][0]*polygon[0][0][1] - polygon[len(polygon)-1][0][1]*polygon[0][0][0]
    for i in range(1 , len(polygon)):
        area += polygon[i-1][0][0]*polygon[i][0][1] - polygon[i-1][0][1]*polygon[i][0][0]

    return abs(area/2)

rect = None
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kp2, des2 = sift.detectAndCompute(gray,None)
    flann = cv2.BFMatcher()

    matches = flann.knnMatch(template_desc, des2, k = 2)

    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.6*n.distance:
            good.append([m])

    match_img = cv2.drawMatchesKnn(template, template_keypoints, gray, kp2,  good, None, flags=10)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    src_pts = np.float32([template_keypoints[m[0].queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m[0].trainIdx].pt for m in good ]).reshape(-1,1,2)

    try:
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()
        
        h,w = template.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)
        diff1 = (dst[0][0][0] + dst[2][0][0]) - (dst[1][0][0] + dst[3][0][0])
        diff2 = (dst[0][0][1] + dst[2][0][1]) - (dst[1][0][1] + dst[3][0][1])
        if diff1 <= 10.0 and diff2 <= 10.0  and pol_area(dst) >= 500:
            rect = dst
        if len(good) >= 4:
            detected_area = cv2.polylines(np.copy(frame),[np.int32(rect)],True,255,3, cv2.LINE_AA)
        if len(sys.argv) >= 3:
            cv2.imshow('frame', detected_area)
        else:
            cv2.imshow('frame', match_img)
    except Exception:
        pass
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.imwrite("my_template_other.png", frame)
       break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()