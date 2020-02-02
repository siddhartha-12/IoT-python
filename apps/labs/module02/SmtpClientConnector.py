'''
Created on Jan 30, 2020

@author: Siddhartha
'''
from smtplib import SMTP, SMTP_SSL
from labs.common.ConfigUtil import ConfigUtil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SmtpClientConnector:
    
    def __init__(self):
        self.config = ConfigUtil()
        self.config.loadConfig("../../../config/ConnectedDevicesConfig.props")
    #method to create and send a mail
    def publishMessage(self, topic, data):
        host = self.config.getValue("smtp.cloud", "host")
        port = self.config.getValue("smtp.cloud", "port")
        fromAddr = self.config.getValue("smtp.cloud", "fromAddr")
        toAddr = self.config.getValue("smtp.cloud", "toAddr")
        authToken = self.config.getValue("smtp.cloud", "authToken")
        #Generating mail body
        msg =MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        body = str(data)
        msg.attach(MIMEText(body, 'plain'))
        msgText = msg.as_string()

        # send e-mail notification
        smtpServer = SMTP_SSL(host, port)
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()
        return True
    