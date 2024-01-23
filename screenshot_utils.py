import os
import pyautogui
import re


def sanitize_filename(filename):
    filename = filename.replace(" ", "")
    filename = re.sub(r'[^a-zA-Z0-9_]', '', filename)
    return filename

