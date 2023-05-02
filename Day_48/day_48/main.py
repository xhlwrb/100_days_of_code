from selenium import webdriver
from selenium.webdriver.common.by import By

# selenium driver
chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# laptop url
driver.get("https://www.amazon.com/Lenovo-Ideapad-Touchscreen-i3-1005G1-Processor/dp/B08B6F1NNR/ref=sr_1_1?fst=as"
           "%3Aoff&pd_rd_r=936db33c-4742-4ec1-b551-b32607d06cb8&pd_rd_w=8DdX1&pd_rd_wg=dBFsA&pf_rd_p=5b7fc375-ab40"
           "-4cc0-8c62-01d4de8b648d&pf_rd_r=8370DJFENEBBT4QPTMV2&qid=1682862233&rnid=16225007011&s=computers-intl"
           "-ship&sr=1-1&th=1")
# find laptop price
price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print(price.get_attribute("innerHTML"))

# driver.close()

driver.quit()

