from twilio.rest import Client

account_sid = 'AC94f869e62dd339724d617dc20d691fc1'
auth_token = '96a164a0ad7b10cc195f35aa001c0e52'

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12565810961',
  body='Hello! How would you rate the cleaning services this week?\n'
       '1. VERY GOOD\n'
       '2. GOOD\n'
       '3. NOT SURE\n'
       '4. POOR\n'
       '5. VERY POOR',
  to='+254726526801'
  # to='+254792451723'
)

print(message.sid)
ks
