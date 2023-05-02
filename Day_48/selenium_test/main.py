from selenium import webdriver
from selenium.webdriver.common.by import By

upcoming_events = {}

# selenium driver
chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# python.org url
driver.get("https://www.python.org/")
# find menu
upcoming_events_widget = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]')
events_menu = upcoming_events_widget.find_element(By.CLASS_NAME, "menu")

# find events
event_list = events_menu.find_elements(By.TAG_NAME, "a")

# find dates
date_list = events_menu.find_elements(By.TAG_NAME, "time")

# add to dict in parallel
temp = {}
i = 0
for date, event in zip(date_list, event_list):
    upcoming_events[i] = {
        "time": date.text,
        "name": event.text,
    }
    i += 1

print(upcoming_events)


driver.quit()

