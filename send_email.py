import smtplib, ssl, os
from dotenv import load_dotenv

load_dotenv()
def send_email(message):
    sender = os.getenv("SENDER_GMAIL")
    password = os.getenv("MY_GMAIL_PASSWORD")

    receiver = os.getenv("RECEIVER_GMAIL")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465, context=context) as server:
        server.login(user=sender, password=password)
        server.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
        
if __name__=='__main__':
    send_email("Hello, how are you?")
