from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def getChrome():
    chromedriver_path = '/usr/lib/chromium/chromedriver'

    o = Options()

    o.binary_location = '/usr/bin/chromium-browser'
    o.add_argument('--headless')
    o.add_argument('--disable-gpu')
    o.add_argument('--no-sandbox')
    o.add_argument('--window-size=1200x600')
    o.add_argument('--disable-desktop-notifications')
    o.add_argument("--disable-extensions")

    return webdriver.Chrome(chromedriver_path, options=o)


def quit(driver):
    driver.quit()


def sleep(sec):
    time.sleep(sec)


def ss(driver):
    driver.save_screenshot('./test.png')
