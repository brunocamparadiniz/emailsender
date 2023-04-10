import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Bruno Diniz'
email['to'] = 'brunocamparadiniz@yahoo.com'
email['subject'] = 'Test = you won the lottery'

email.set_content(html.substitute({'name': 'Bruno'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('brunocamparadiniz@gmail.com', 'yezdkjyfriosyqex')
    smtp.send_message(email)
    print('all good boss')
