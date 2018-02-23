from urllib import *
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
import urllib.request
import requests
from io import BytesIO
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from lxml import html
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def scraping(first_name="", last_name="", driver=None):

    url = "https://directory.ufl.edu/search/?f={}&l={}&e=&a=staff".format(first_name, last_name)
    if driver is None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='WebDriver/chromedriver.exe')
        driver.maximize_window()

    try:
        driver.get(url)
    except:
        phone_num = ""
        email = ""
        return [phone_num, email]

    try:
        phone_num = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "p.result-phone"))

        )
        phone_num = phone_num.text
    except:
        phone_num = ""

    try:
        email = driver.find_element_by_css_selector("p.result-email > span")
        email = email.text

    except:
        email = ""

    print(phone_num)
    print(email)

    driver.quit()

    return [phone_num, email]

scraping(first_name="ALLENE", last_name="AARON")
# scraping(first_name="ANTHONY", last_name="ABBATE")