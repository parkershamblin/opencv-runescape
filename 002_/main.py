import cv2 as cv
import numpy as np
import os
from windowcapture import WindowCapture

# change directory so we dont need to write the full path for every image
# each time we read them in with cv.imread()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# read images
needle_img = cv.imread("cow.png", cv.IMREAD_REDUCED_COLOR_2)
haystack_img = cv.imread("farm.png", cv.IMREAD_REDUCED_COLOR_2)

window = WindowCapture("Ikov")
window_capture = window.get_screenshot()
cv.imshow("Result", window_capture)
cv.waitKey()

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
cv.imshow("Result", result)
cv.waitKey()

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

needle_width, needle_height = needle_img.shape[1], needle_img.shape[0]

top_left = max_loc
bottom_right = (top_left[0] + needle_width, top_left[1] + needle_height)

cv.rectangle(haystack_img, top_left, bottom_right, (0, 0, 255), 2)

cv.imshow("Result", haystack_img)
cv.waitKey()

print(max_loc)
print(max_val)
