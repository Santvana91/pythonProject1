from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options =webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")
#print(driver.window_handles())
driver.set_window_size()