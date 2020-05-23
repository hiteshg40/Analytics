import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def initialize_app(config):
    return SimpleEmail(config)

class SimpleEmail:
    def __init__(self, config):
        self.Email = config["Email"]
        self.Pwd = config["Pwd"]

    def send_email(self,data,recepient_email):
        s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        s.login(self.Email, self.Pwd)
        
        msg = MIMEMultipart()       # create a message
        # setup the parameters of the message
        msg['From']=self.Email
        msg['To']=recepient_email
        msg['Subject']="List of restaurants"
        message = "Hello , Please find the top 10 restaurants. \n" + data
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg
        return "Details sent"