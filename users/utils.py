import os
from twilio.rest import Client
from django.conf import settings


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC68f02d45719d067d1277ff52e010f96b"
auth_token = "027b92bc58a3f90f4c2ad8a1476ea10c"
client = Client(account_sid, auth_token)
def send_sms(user_code, number):
    message = client.messages \
                    .create(
                        body=f'le code activation de votre code Minlang est {user_code}' ,
                        from_='+17069548656',
                        to=f'{number}'
                    )

    print(message.sid)