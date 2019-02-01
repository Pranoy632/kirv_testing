import email
import imaplib
import ctypes
import getpass
import json

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
#usr = input("pls enter email")
#pwd = getpass.getpass("pls enter password")
f = open("../../common/email_data.json", "r")
data = json.load(f)
mail.login(data["username"], data["password"])
mail.select("INBOX")

class EmailCheck(object):

    received_mail = None

    def email_check(self):
        try:
            mail.select("INBOX")
            (retcode, message) = mail.search(None, '(UNSEEN)')
            if retcode == 'OK':
                for num in message[0].split():
                    typ, data = mail.fetch(num, '(RFC822)')
                    for response_part in data:
                        if isinstance(response_part, tuple):
                            original = email.message_from_bytes(
                                response_part[1])
                            # print('<html>\n<body>' + original.get_payload(
                            # decode=True).decode("utf-8") + '\n' + '</body>\n'
                            # + '</html>')
                            # print(original['From'])
                            data = original['Subject']
                            # print(data)
                            received_mail = data
                            typ, data = mail.store(num, '+FLAGS', '\\Seen')
                            return received_mail
        except Exception as e:
            print("Email:", str(e))
