import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(canny):
    height = canny.shape[0]
    mask = np.zeros_like(canny)

    triangle = np.array([[
    (200, height),
    (550, 250),
    (1100, height),]])

    cv2.fillPoly(mask, triangle, 255)
    return mask

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny = canny(lane_image)

cv2.imshow("result", region_of_interest(canny))
cv2.waitKey(0)
