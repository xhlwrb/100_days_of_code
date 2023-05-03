from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

# selenium driver
chrome_driver_path = "C:\\Development\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

# linkedin url
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3555235454&f_LF=f_AL&geoId=102257491&keywords=python"
           "%20developer&location=London%2C%20England%2C%20United%20Kingdom")
# find log in button
log_in_button = driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis")
print(log_in_button.text)
# click log in button
log_in_button.click()

# find username and password input
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

# type in username and password
username_input.send_keys("yh100days@yahoo.com")
password_input.send_keys("wrb941230")

# log in button in second page
log_in_button_2 = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large.from__button--floating")
log_in_button_2.click()

# first job button
# first_job = driver.find_element(By.CSS_SELECTOR, '.ember-view.jobs-search-results__list-item.occludable-update.p0.relative.scaffold-layout__list-item')
first_job = driver.find_element(By.CSS_SELECTOR, '#main > div > div.scaffold-layout__list > div > ul > li')
first_job.click()

# save button
save_button = driver.find_element(By.CLASS_NAME, '.jobs-save-button')
# save the job
save_button.click()

# follow button
# follow_button = driver.find_element(By.CSS_SELECTOR, '.follow.artdeco-button.artdeco-button--secondary.ml5')
follow_button = driver.find_element(By.CLASS_NAME, '.follow')
# scroll to the follow button
scroll_origin = ScrollOrigin.from_element(save_button)
ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 1000)\
        .perform()
# follow the company
follow_button.click()

# driver.quit()

