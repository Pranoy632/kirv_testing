import email
import imaplib
import ctypes
import getpass

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
#usr = input("pls enter email")
#pwd = getpass.getpass("pls enter password")
mail.login('amztest18@gmail.com', 'amz@test')
mail.select("INBOX")


class EmailCheck(object):

    def email_check(self):
        try:
            mail.select("INBOX")
            (retcode, message) = mail.search(None, '(UNSEEN)')
            if retcode == 'OK':
                for num in message[0].split():
                    typ, data = mail.fetch(num, '(RFC822)')
                    for response_part in data:
                        if isinstance(response_part, tuple):
                            # print(response_part)
                            original = email.message_from_bytes(
                                response_part[1])
                            print(original['From'])
                            data = original['Subject']
                            print(data)
                            typ, data = mail.store(num, '+FLAGS', '\\Seen')
        except Exception as e:
            print("Email:", str(e))
