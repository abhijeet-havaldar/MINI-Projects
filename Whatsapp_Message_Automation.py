from twilio.rest import Client
from datetime import datetime, timedelta
import time

account_sid = ''
auth_token = ''

client =Client(account_sid,auth_token)

def send_whatsapp_message(recipient_nummber, message_body):
    try:
        message = client.messages.create(
            from_ =  'whatsapp:+',
            body = message_body,
            to = f'whatsapp: {recipient_nummber}'  
                  
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print("An error occured")

name = input("Enter the recipient name =")
recipient_number = input("Enter the recipient Whatsapp number with country code (e.g +123652147863)")
message_body = input(f"enter the message you want to send to {name}:")

date_str = input('enter the date to send the message (YYYY-MM-DD):')
time_str = input('enter the time to send the message (HH:MM in 24hour format):')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is  in the past. Please enter a future date and time:')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    time.sleep(delay_seconds)

    send_whatsapp_message(recipient_number, message_body)