import imaplib
from Logger import get_logger, log
import time
from datetime import datetime

def check_email(user, product, letters):
    mail = imaplib.IMAP4_SSL('mail.satprof.pro')
    mail.login('signserver@satprof.pro', '5KwYXoqD')
    mail.select("inbox")
    t1 = datetime.now()
    typ, data = __wait_message(mail, t1, letters)
    data1 = data
    letters_in_box = len(data[0].split())
    try:
        if letters == 0:
            assert(letters_in_box == letters), 'Mailbox contain %s letters but should contain %s' % (letters_in_box, letters)
            return 1
        else:
            assert (letters_in_box == letters), 'Mailbox contain %s letters but should contain %s' % (letters_in_box, letters)
            for num in data[0].split():
                typ, data = mail.fetch(num, '(RFC822)')
                a = data[0][1]
                assert ('Hello,' in data[0][1]), 'ERROR, miss, "Hello'
                assert ('Sign operation was executed for product "%s"' % product), 'ERROR, miss, Sign operation was executed for product'
                assert ('Status: APPROVED, READY' in data[0][1]), 'ERROR, miss, Status: APPROVED, READ'
                assert ('Current email-list for product "%s":' % product in data[0][1]), 'ERROR, miss, Current email-list for product'
                assert ('User: %s, email: correct' % user in data[0][1]), 'ERROR, miss, User'
                assert ('Kind regards,' in data[0][1]), 'ERROR, miss, Kind regards'
                mail.store(num, '+FLAGS', '\\Deleted')
            return 1
    except Exception as E:
        for num in data1[0].split():
            mail.store(num, '+FLAGS', '\\Deleted')
            print(1)
        log(E)
        return 0
    finally:
        mail.close()
        mail.logout()

def __wait_message(mail, t1, letters):
    try:
        while (datetime.now() - t1).seconds <= 15:
            time.sleep(1)
            typ, data = mail.search(None, 'ALL')
            if len(data[0].split()) == letters:
                return (typ, data)
    except Exception as E:
        log(E)
        return 0
def clean_email():
    time.sleep(1)
    mail = imaplib.IMAP4_SSL('mail.satprof.pro')
    mail.login('signserver@satprof.pro', '5KwYXoqD')
    mail.select("inbox")
    typ, data = mail.search(None, 'ALL')
    letters_in_box = len(data[0].split())
    for num in data[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')
    mail.close()
    mail.logout()
    return "Mail box contain %s letters" % letters_in_box