import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_emails):
    from_email = 'your-email@example.com'
    smtp_server = 'smtp.mailtrap.io'
    smtp_port = 2525
    smtp_username = 'your_username'
    smtp_password = 'your_password'
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(from_email, to_emails, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Kullanım:
send_email(
    subject="Network Automation Alert",
    body="Network device issue detected.",
    to_emails=["your-email@example.com"]
)
