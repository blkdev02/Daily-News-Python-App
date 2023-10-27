import smtplib, ssl, os

def send_email(message):
    host = os.getenv("EMAIL_HOST")
    port = os.getenv("EMAIL_PORT")
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)




# if the above does not work try below

# context = ssl.create_default_context()
 
# with smtplib.SMTP(smtp_server,port) as server:
#     server.starttls(context=context)
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)