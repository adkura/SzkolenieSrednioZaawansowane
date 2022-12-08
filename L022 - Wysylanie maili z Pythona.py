import functools
import smtplib


def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)


    try:
        server = smtplib.SMTP_SSL('poczta.interia.pl', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending email')
        return False



user = 'adkura@interia.pl'
password = '37krakow10'
mailFrom = 'adkura@interia.pl'
mailTo = ['adkura@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello!!!

This mail confirms that processing has finished without problems,

Have a nice day!'''

SendInfoEmailFromInteria = functools.partial(SendInfoEmail, user, password, mailSubject = 'Execution alert')



SendInfoEmailFromInteria(mailFrom = mailFrom, mailTo = mailTo, mailBody = mailBody)

#SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
