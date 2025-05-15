from EmailAPI import send_status_email
from TwilioAPI import send_message
from AlertAPI import send_alert
table_data = [
        {
            "code": "T101 Bh5 Heater OFF FAULT",
            "description": "Insufficient Heat (element failed)",
            "state": "Fail",
            "last_failure": "07 April 2025, 04:00:00"
        }, 
        {
            "code": "T102 Bh5 Heater OFF FAULT",
            "description": "Insufficient Heat (element failed)",
            "state": "Pass",
            "last_failure": "No Failure"
        },
        {
           "code": "T103 Bh5 Heater OFF FAULT",
            "description": "Insufficient Heat (element failed)",
            "state": "NoStatus",
            "last_failure": "No Failure"
        },
    ]
emails = ["jaspartap.goomer@ontariotechu.net", "jaspartapgoomer@gmail.com"]
phone_numbers = ["+19052263054", "+19052263055"]
message = "System Status Report"
subject = "System Status Report"
send_alert(emails, phone_numbers, subject, message, table_data)