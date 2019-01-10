import smtplib
import io

with io.open('/Users/parastooghalamchi/Dropbox/Unipart/Assessments/Unipart Participants/List of Participants.txt') as f:
    names = f.read()


emails = names.split('\n')
print(emails)
firstNames = []
for email in emails:
    firstName = email.split('.')[0]
    firstNames.append(firstName)

print(firstNames)
print(len(firstNames))


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = '''From: %s\nTo: %s\nSubject: %s\n\n%s
    ''' % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail to  {}'.format(recipient))
    except Exception as e:
        print(e)


for index in range(len(firstNames)):

    
    email = 'Dear {}, \nI am pleased to invite you to join us at Cambridge Digital Group on the 4th of December from 10am to 5pm to Unipart digital group workshop.\n1)	What do you achieve from the workshop? In this one day workshop you have the opportunity to: \nA) have a grasp of how to use coding in your work, and \nB)join the network of digital experts in Cambridge. This event follows up with dinner in a friendly group with digital team.\n2)	Who can attend the workshop? This workshop is designed for people who want to start learning Python to use it with expert supports within Unipart digital team.\n3)	What do you need to send us to be able to attend the workshop? You need to reply to this email with your telephone number and line manager\'s contact information\nfor us to arrange your attendance in the workshop by 6pm on Wednesday the 29th of Nov.\nDo not hesitate contacting me if you need any help. The map and the workshop schedule will be sent to you by Friday.\n\nBest,\n\nParastoo Ghalamchi, PhD.\nDigital Education Expert\nUnipart Digital Team'
    email = email.format(firstNames[index].capitalize())
    
    send_email('parastoo.ghalamchi@unipart.com', 'dmalpniuzpfkjrxw',emails[index],'Invitation to Cambridge digital workshop on 4th of Dec. from 9:30am to 5pm',email)

