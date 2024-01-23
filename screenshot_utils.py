import os
import pyautogui
import re


def sanitize_filename(filename):
    filename = filename.replace(" ", "")
    filename = re.sub(r'[^a-zA-Z0-9_]', '', filename)
    return filename


def take_screenshot(product_code, product_name, date):
    try:
        screenshot_dir = 'screenshots'
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        sanitized_product_name = sanitize_filename(product_name)

        file_name = f"{product_code}_{sanitized_product_name}_{date}.png"
        screenshot_path = os.path.join(screenshot_dir, file_name)

        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)

        print(f"Screenshot salvo em: {screenshot_path}")
        return file_name

    except Exception as e:
        print(f"Erro ao tirar screenshot: {e}")
