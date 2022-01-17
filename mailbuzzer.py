import time
import RPi.GPIO as GPIO
from imapclient import IMAPClient

HOSTNAME = 'imap.gmail.com'
MAILBOX = 'Inbox'
MAIL_CHECK_FREQ = 10        # set mail check frequency in seconds

# add credentials
USERNAME = ''
PASSWORD = ''

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)

def mail_check():
    # login to mailserver
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)

    # select our MAILBOX and looked for unread messages
    unseen = server.folder_status(MAILBOX, ['UNSEEN'])

    # number of unread messages
    # print to console to determine NEWMAIL_OFFSET
    newmail_count = (unseen[b'UNSEEN'])
    print('%d unseen messages' % newmail_count)

    if newmail_count > 0:
       GPIO.output(22,1)
    else:
        GPIO.output(22,0)

    time.sleep(MAIL_CHECK_FREQ)

while True:
    mail_check()
