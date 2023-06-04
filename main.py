from time import sleep
import requests
import urllib.request
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

URL = "https://www.python.org/"

service = Service(r"C:\\Users\\janns\\PycharmProjects\\chromedriver.exe")
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

driver.get(URL)

img = driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/h1/a/img')
src = img.get_attribute('src')
print(src)

urllib.request.urlretrieve(src, "python.png")
response = requests.get(src)
image_size = Image.open("python.png")
wdt, hgt = image_size.size
len(response.content)

print(f"\nImage Size: {wdt}x{hgt}")
print(f"Image Size: {len(response.content)} bytes")

driver.quit()
