import lxml
import requests
import pprint
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Lenovo-Ideapad-Touchscreen-i3-1005G1-Processor/dp/B08B6F1NNR/ref=sr_1_1?fst=as%3Aoff&pd_rd_r=936db33c-4742-4ec1-b551-b32607d06cb8&pd_rd_w=8DdX1&pd_rd_wg=dBFsA&pf_rd_p=5b7fc375-ab40-4cc0-8c62-01d4de8b648d&pf_rd_r=8370DJFENEBBT4QPTMV2&qid=1682862233&rnid=16225007011&s=computers-intl-ship&sr=1-1"
google_email = "100daysg@gmail.com"
google_password = "gfjzvlmufwfzjkla"
yahoo_email = "yh100days@yahoo.com"
laptop_standard_price = 400


def scrap_price(url):
    response = requests.get(url,
                            headers={
                                "User-Agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) '
                                              'AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                                "Accept-Language": "en-US, en;q=0.5",
                            })
    response.raise_for_status()
    contents = response.text

    soup = BeautifulSoup(contents, "lxml")
    price_with_mark = soup.find(name="span", class_="a-offscreen")

    if not price_with_mark:
        return None
    else:
        price_text = price_with_mark.getText()
        price_value = float(price_text[1:])
        return price_value


def brut_force_until_get_price():
    while True:
        robot_test_success = scrap_price(url)
        if robot_test_success:
            print("success")
            return robot_test_success
        else:
            print("try")


# scrap laptop price from amazon
laptop_active_price = brut_force_until_get_price()
# if lower than standard
if laptop_active_price <= laptop_standard_price:
    # send email
    print("Under standard price! Sending email...")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=google_email, password=google_password)
        connection.sendmail(from_addr=google_email,
                            to_addrs=yahoo_email,
                            msg=f"Subject:Amazon Price Alert!\n\nLaptop is now ${laptop_active_price}\n{url}")


