from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# selenium driver
chrome_driver_path = "C:\\Development\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
driver.maximize_window()

# url
driver.get("https://tinder.com/")

# log in button
log_in_button = driver.find_element(By.XPATH, '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()

time.sleep(2)

# with facebook
with_facebook_button = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
with_facebook_button.click()

time.sleep(5)

# switch to new window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# email textbox
fb_email = driver.find_element(By.ID, "email")
fb_email.send_keys("100daysg@gmail.com")
# password textbox
fb_password = driver.find_element(By.ID, "pass")
fb_password.send_keys("wrb100daysg")
# log in button
fb_log_in_button = driver.find_element(By.NAME, "login")
fb_log_in_button.click()

time.sleep(5)

# continue log in
continue_button = driver.find_element(By.XPATH, '//*[@id="mount_0_0_kJ"]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div')
# continue_button = driver.find_element(By.CSS_SELECTOR, '.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3')
continue_button.click()

# driver.quit()
