from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
TWITTER_EMAIL = "yh100days@yahoo.com"
TWITTER_PASSWORD = "wrb100days"


class InternetSpeedTwitterBot:
    def __init__(self, path):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=path, chrome_options=self.chrome_options)
        self.driver.maximize_window()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # url
        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)

        # test speed
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test.test-mode-multi")
        go_button.click()
        time.sleep(40)

        # down
        download_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed")
        self.down = float(download_speed.text)
        print(f"down {self.down}")
        # up
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed")
        self.up = float(upload_speed.text)
        print(f"up {self.up}")

    def tweet_at_provider(self):
        # url
        self.driver.get("https://www.twitter.com")

        time.sleep(5)

        # log in button
        log_in_button = self.driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n.r-16y2uox")
        log_in_button.click()

        time.sleep(3)
        # yes log in button
        # yes_log_in_button = self.driver.find_element(By.CSS_SELECTOR, ".css-18t94o4.css-901oao.css-16my406.r-1cvl2hr.r-poiln3.r-bcqeeo.r-qvutc0")
        yes_log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]')
        yes_log_in_button.click()

        time.sleep(3)

        # email textbox
        email_textbox = self.driver.find_element(By.NAME, "text")
        email_textbox.send_keys("yh100days@yahoo.com")

        # continue button
        continue_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        continue_button.click()

        time.sleep(3)

        # username textbox
        username_textbox = self.driver.find_element(By.NAME, "text")
        username_textbox.send_keys("Bot4_100days")

        # continue 2 button
        continue_button_2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        continue_button_2.click()

        time.sleep(3)

        # password textbox
        password_textbox = self.driver.find_element(By.NAME, "password")
        password_textbox.send_keys("wrb100days")

        # log in 2 button
        log_in_button_2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        log_in_button_2.click()

        time.sleep(2)

        # type in tweet
        tweet = f"Internet speed too slow! Only {self.down}down/{self.up}up"
        tweet_textbox = self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        tweet_textbox.send_keys(tweet)

        # submit
        tweet_textbox.send_keys(Keys.CONTROL, Keys.ENTER)


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()



