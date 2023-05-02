from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# selenium driver
chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# # wikipedia url
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# articles_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # articles_count.click()
#
# content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# # content_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# sign up form url
driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Kathryn")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Wu")
email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("100daysg@gmail.com")
sign_up_button = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up_button.click()


driver.quit()
