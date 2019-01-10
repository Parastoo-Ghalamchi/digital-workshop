"""
This program splits
a text at each line
"""

spam = '''
Dear Tom
I hope this email finds you well.
There is no Tom and there is no email.
Best,
Parastoo
'''

spam = spam.split('\n')
spam
print(spam)

