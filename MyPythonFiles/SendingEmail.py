"""
What we need know to send email:
1. SMTP(Simple Mail Transfer Protocol) is the module that deals with sending email
2. import smtp
3. Connect to smtp server by finding your email provider smtp to find out: 1) domain name, 2) port information)
3.1. example for gmail
- Google smtp gmail
- Domain name: smtp.gmail.com
- port: 587

4.Make an SMTP objectL
4.1. example: smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
4.2. Check if the object is made by type:
example: type(smtpObj) should return: <class 'smtplib.SMTP>

5. Say hello to server
5.1. if the first item in the returned tuple is 250 then it was successful

"""
import smtp

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
type(smtpObj)

smtpObj.ehlo() #say hello to server

