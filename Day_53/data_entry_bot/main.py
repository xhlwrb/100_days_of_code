import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B" \
      "%22west%22%3A-122.56207503271484%2C%22east%22%3A-122.30458296728516%2C%22south%22%3A37.67400157794278%2C" \
      "%22north%22%3A37.876442746056846%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B" \
      "%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22" \
      "%3Atrue%7D"

response = requests.get(URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,de;q=0.7",
})
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

print(soup.prettify())

# data = json.loads(
#     soup.select_one("script[data-zrr-shared-data-key]")
#     .contents[0]
#     .strip("!<>-")
# )
# all_data = data['cat1']['searchResults']['listResults']
#
# print(all_data)

# price_list = []
# address_list = []
# url_list = []
#
# for i in range(len(all_data)):
#     try:
#         price = all_data[i]["units"][0]["price"]
#     except KeyError:
#         price = all_data[i]["price"]
#     address = all_data[i]["address"]
#     house_url = all_data[i]["detailUrl"]
#
#     if "http" not in house_url:
#         house_url = f"https://www.zillow.com{house_url}"
#
#     price_list.append(price)
#     address_list.append(address)
#     url_list.append(house_url)
#
# print(price_list)
# print(address_list)
# print(url_list)

price_list = ["111", "222"]
address_list = ["111", "222"]
url_list = ["111", "222"]

# selenium driver
chrome_driver_path = "C:\\Development\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.maximize_window()

# google sheet url
sheet_url = "https://docs.google.com/forms/d/1m_NgiCqUDu328lEIUQg8SQj4tUSk8s3VJooNSvUsHTc/viewform?edit_requested=true"
driver.get(sheet_url)

time.sleep(3)

first_tab_handle = driver.current_window_handle

for i in range(len(price_list)):
    time.sleep(3)

    # 1st textbox
    textbox_1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    # 2nd textbox
    textbox_2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    # 3rd textbox
    textbox_3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    # submit button
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    # write address
    textbox_1.send_keys(address_list[i])
    # write price
    textbox_2.send_keys(price_list[i])
    # write url
    textbox_3.send_keys(url_list[i])
    # submit
    submit_button.click()

    time.sleep(1)

    # write next button
    write_next = driver.find_element(By.LINK_TEXT, "Weitere Antwort senden")
    # write next
    write_next.click()

log_in = driver.find_element(By.XPATH, '//*[@id="SMMuxb"]/a[1]')
log_in.click()

time.sleep(3)

driver.switch_to.window(driver.window_handles[1])

gmail_textbox = driver.find_element(By.CSS_SELECTOR, ".whsOnd.zHQkBf")
gmail_textbox.send_keys("100daysg@gmail.com")

continue_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
continue_button.click()

create_sheet_button = driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div')
create_sheet_button.click()

sheet_name_textbox = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[56]/div/div[2]/span/div/div/span/div[1]/div/div/div[1]/div/div[1]/input')
sheet_name_textbox.send_keys("Zillow Sheet")

create_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[56]/div/div[2]/div[3]/div[2]')
create_button.click()

driver.close()

