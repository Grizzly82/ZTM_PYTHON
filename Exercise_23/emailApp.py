import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Cris'
email['to'] = 'Cris.Vizcaino@gmail.com'

email['subject'] = 'Hello from Python'
#email.set_content('This is a test email sent from Python.')
email.set_content(html.substitute(name='TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Cris.Vizcaino@gmail.com', 'password')  # Replace 'password' with your actual email password or app password
    smtp.send_message(email)
    print('Email sent successfully!')