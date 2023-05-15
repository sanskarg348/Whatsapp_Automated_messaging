import time
import webbrowser as web
from re import fullmatch
from urllib.parse import quote
import pyautogui as pg


if __name__ == '__main__':
    phone_no = input()
    message = input()
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise "Invalid Phone Number."

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(4)
    pg.press("enter")
    time.sleep(2)
    pg.hotkey("command", "w")