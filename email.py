import smtplib
import time
from email.mime.text import MIMEText
from .log import Logger

class EMail:
    def __init__(self, host, sender, password, logger=Logger()) -> None:
        self.host = host
        self.sender = sender
        self.password = password
        self.logger = logger

    def send(self, title, receivers, msg):
        message = MIMEText(msg,'plain','utf-8')
        message['Subject'] = title
        message['From'] = self.sender 
        message['To'] = receivers[0] 
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(self.host, port=25)
            smtpObj.login(self.sender, self.password) 
            smtpObj.sendmail(self.sender, receivers, message.as_string()) 
            smtpObj.quit() 
            self.logger.console('{} 邮件发送成功'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        except smtplib.SMTPException as e:
            self.logger.console(e)