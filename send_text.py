# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from datetime import datetime

def send_text_message(destination: str, message: str):

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure


    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message,
            from_='+18289701125',
            to=destination
        )

    print(message.sid)



    
    
    


def main():
    name = input('What is your name? \n')

    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    
    bmonth=int(input("Enter your birth month 1-Jan, 2-Feb.. : "))
    byear=int(input("Enter your birth year: "))
    year=int(year)
    month=int(month)
    

    if(byear<year):
        if(bmonth<month):
            x = str(year - byear)
            y = str(month - bmonth)
          
    else:
            x = str((year - byear) - 1)
            y = str(12 - (bmonth - month))
           
 
    
    send_text_message("+639193139490", 'Hello ' +name + '. Happy Birthday! You are '+x + 'years old' +' and ' +y + 'months!' )

if __name__ == "__main__":
    main()