from time import sleep
from selenium import webdriver
from secrets import password

class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
            
LouisBot = Instabot("lakshitdabas","asdf")