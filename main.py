from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

address = "C:\chromedriver\chromedriver.exe"

email = ""
password = ""


class Insta:
    def __init__(self):
        self.service = Service(address)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.instagram.com/akshdeep727/")

    def login(self):
        sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(email)

        enter_password = self.driver.find_element(By.NAME, "password")
        enter_password.send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()

    def search(self):
        sleep(5)
        self.driver.get("https://www.instagram.com/abhijeet.prvt/")
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(5)
        pop_up = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)


open_insta = Insta()
open_insta.login()
open_insta.search()

