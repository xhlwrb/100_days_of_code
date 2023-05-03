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
driver.get("https://www.pythonanywhere.com/user/xhlwrb/tasks_tab/")

# log in
username = driver.find_element(By.NAME, "auth-username")
username.send_keys("xhlwrb")
password = driver.find_element(By.NAME, "auth-password")
password.send_keys("wrb941230")
log_in = driver.find_element(By.ID, "id_next")
log_in.click()

# task
task = driver.find_element(By.ID, "id_tasks_link")
task.click()

# extend expiry
# extend = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.extend_scheduled_task.task_action")
# extend = driver.find_element(By.XPATH, '//*[@id="id_scheduled_tasks_table"]/div/div/table/tbody/tr/td[6]/button[4]')
time.sleep(5)
extend = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.extend_scheduled_task.task_action")

extend.click()

print(extend.text)

driver.quit()
