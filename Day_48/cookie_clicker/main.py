from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# selenium driver
chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# cookie url
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# cookie button
cookie = driver.find_element(By.ID, "cookie")

# upgrade
upgrade_dict = {}
store = driver.find_element(By.ID, "store")
all_upgrades = store.find_elements(By.CSS_SELECTOR, "b")
for each_b in all_upgrades:
    try:
        temp = each_b.text.split(" - ")
        upgrade_dict[temp[0]] = float(temp[1].replace(',', ''))
    except IndexError:
        pass


def purchase_upgrade(upgrade_dict, cookie_owned):
    # find the upgrade
    most_expensive_value = 0
    for key in upgrade_dict:
        if most_expensive_value < upgrade_dict[key] <= cookie_owned:
            most_expensive_value = upgrade_dict[key]
            most_expensive_key = key
    # click the upgrade
    upgrade_button = driver.find_element(By.ID, f"buy{most_expensive_key}")
    upgrade_button.click()


# every 5 seconds, search for affordable upgrade and purchase the most expensive one
# set 2 start time
start_time = time.time()
new_start_time = start_time
while True:
    # click cookie button
    cookie.click()
    if time.time() - new_start_time >= 5:
        # after 5 seconds
        # get money
        money = driver.find_element(By.ID, "money")
        cookie_owned = float(money.text.replace(',', ''))
        # purchase most expensive upgrade
        purchase_upgrade(upgrade_dict, cookie_owned)
        # reset start time
        new_start_time = time.time()
    if time.time() - start_time >= 300:
        # after 5 minutes, stop and print CPS
        cps = driver.find_element(By.ID, "cps")
        print(cps.text)
        break

# driver.quit()
