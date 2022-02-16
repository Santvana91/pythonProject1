import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.i

#open the FireFox browser
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#enter url and wait till page load
driver.get("https://www.selenium.dev/")
time.sleep(2)
#open browser stack
driver.get("https://www.browserstack.com/")
time.sleep(2)
driver.back()
title1= print(driver.title)

driver.forward()
title2= print(driver.title)
time.sleep(2)

driver.refresh()
title3= print(driver.title)