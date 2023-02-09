import requests
import smtplib

MY_EMAIL = "100daysg@gmail.com"
MY_PASSWORD = "gfjzvlmufwfzjkla"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def telegram_bot_sendtext(self, bot_message):
        bot_token = "6093731261:AAH_sXfvkElXekEfEfttw-w7h3rp93Rw1t4"
        bot_chatID = "5738351415"
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message

        response = requests.get(send_text)

        return response.json()

    def send_emails(self, customer_data, email_message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for each_customer in customer_data:

                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=each_customer["email"],
                                    msg=email_message)

