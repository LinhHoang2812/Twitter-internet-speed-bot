import selenium
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


TWITTER_MAIL = os.environ["EMAIL"]
TWITTER_PASSWORD = os.environ["PASSWORD"]
DOWNLOAD = 150
UPLOAD = 10


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

class InternetSpeedTwitterBot():
    def __init__(self):
        self.up= UPLOAD
        self.down= DOWNLOAD
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(5)
        cookies = self.driver.find_element(By.ID,"onetrust-accept-btn-handler")
        cookies.click()
        notif = self.driver.find_element(By.CSS_SELECTOR,".notification a")
        notif.click()
        go = self.driver.find_element(By.CSS_SELECTOR,".start-button a")
        go.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"down:{self.down}")
        self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"up:{self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        #main_window = self.driver.current_window_handle

        time.sleep(2)
        cookies = self.driver.find_elements(By.CSS_SELECTOR,".r-1r5su4o div")[1]
        cookies.click()

        sign_in = self.driver.find_element(By.CSS_SELECTOR,".r-2o02ov a")
        sign_in.click()

        time.sleep(2)
        email = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_MAIL)

        next = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next.click()


        try:

            time.sleep(2)
            password= self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)



        except ElementClickInterceptedException:

            time.sleep(3)
            user_name= self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            user_name.send_keys("IamAbot3105")

            next1 = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
            next1.click()

            password = self.driver.find_element(By.XPATH,
                                                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)



        finally:
            log_in = self.driver.find_element(By.XPATH,
                                              '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            log_in.click()

            self.driver.implicitly_wait(20)
            tweet_text = self.driver.find_element(By.CSS_SELECTOR,'.DraftEditor-root div div div')
            tweet_text.send_keys(f"My internet speed is {self.down}down/{self.up}up ")

            tweet_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
            tweet_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

