import pyautogui
import win32gui
import cv2 as cv
import numpy as np
from collections import namedtuple


class WindowCapture:
    def __init__(self, window_name=None):
        if window_name is None:
            self.window_handle = win32gui.GetDesktopWindow()
        else:
            self.window_handle = win32gui.FindWindow(None, window_name)
            if not self.window_handle:
                raise Exception("Window not found: {}".format(window_name))

    def get_rectangle(self):
        return self.client_rect

    def get_screenshot(self):
        # bring up the window if minimized
        try:
            win32gui.SetForegroundWindow(self.window_handle)
        except win32gui.error as e:
            print(e)
        # calculate the window client size and area
        x, y, x1, y1 = win32gui.GetClientRect(self.window_handle)
        # convert the client-area coordinates of a specified point to screen coordinates
        x, y = win32gui.ClientToScreen(self.window_handle, (x, y))
        x1, y1 = win32gui.ClientToScreen(self.window_handle, (x1, y1))
        # calculate width and height of window
        width = x1 - x
        height = y1 - y
        # take a screenshot of the window
        screenshot_img = cv.cvtColor(np.array(pyautogui.screenshot(region=(x, y, width, height))), cv.COLOR_RGB2BGR)
        return screenshot_img