from _multiprocessing import win32


def outlook():
    SERVER = "smtp.126.com"
    FROM = "yuantaixing@126.com"
    TO = ["1183195926@qq.com"]  # must be a list

    SUBJECT = "Subject"
    TEXT = "Your Text"

    # Prepare actual message
    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    import smtplib
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)
    server.quit()
if __name__ == '__main__':
    outlook()