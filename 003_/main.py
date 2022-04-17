import cv2 as cv
import time
import keyboard
import os
from windowcapture import WindowCapture
from vision import Vision

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture("Ikov")
taking_pictures = False

# load the trained model
cow_cascade = cv.CascadeClassifier("cascade/cascade.xml")
cow_vision = Vision(None)  # initalize with no image to match


while True:
    # get screenshot
    screenshot = wincap.get_screenshot()
    # get rectangles from the vision algorithm
    rectangles = cow_cascade.detectMultiScale(screenshot)
    detection_img = cow_vision.draw_rectangles(screenshot, rectangles)
    cv.imshow("Detection", detection_img)

    loop_time = time.time()
    key = cv.waitKey(1)

    # press q to exit program
    if keyboard.is_pressed("q"):
        cv.destroyAllWindows()
        break

    if taking_pictures:
        if keyboard.is_pressed("f"):
            screenshot = wincap.get_screenshot()
            cv.imwrite(f"positive/{loop_time}.jpg", screenshot)
            time.sleep(1)
        elif keyboard.is_pressed("d"):
            screenshot = wincap.get_screenshot()
            cv.imwrite(f"negative/{loop_time}.jpg", screenshot)
            time.sleep(1)
