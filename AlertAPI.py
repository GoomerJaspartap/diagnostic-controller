from EmailAPI import send_status_email
from TwilioAPI import send_message
def send_alert(emails, phone_numbers, subject, message, table_data):
    text = f"{message}\n\nStatus Alert:\n"
    for row in table_data:
        text += f"{row['code']} - {row['description']} {row['state']} {row['last_failure']}\n\n"
    for email in emails:
        send_status_email(email, subject, message, table_data, text)
        print(f"Email sent to {email}")
    for number in phone_numbers:
        sid = send_message(number, text)
        print(f"Message sent to {number} with SID: {sid}")