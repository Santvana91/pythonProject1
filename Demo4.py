import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#open the chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#enter url and wait till page load
driver.get("https://www.google.com/")
time.sleep(2)
#open new tab
driver.switch_to.new_window("tab")
driver.get("https://www.gmail.com/")
time.sleep(2)
driver.fullscreen_window()