from time import sleep
from selenium import webdriver
from secrets import password
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

chromedriver_path ='/mnt/c/Users/louis/Documents/GitHub/instagram_bot/chromedriver.exe'
class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(executable_path= chromedriver_path)
        self.username = username
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        sleep(2)
        username = driver.find_element_by_name("username")
        username.send_keys('ackland_louis')
        password = driver.find_element_by_name('password')
        password.send_keys('Ilike2poop')

