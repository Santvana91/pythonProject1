from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver = webdriver.edge(service=Service(EdgeChromiumDriverManager().install()))
