import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/desecure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Hi AA, I'm Afiq",
#                      from_='+18454201095',
#                      to='+60124290640'
#                  )

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        from_='+18454201095',
                        to='+60135606129'
                    )

print(call.sid)
print(account_sid)

# export TWILIO_ACCOUNT_SID='AC0e734015c6d217cbde2f7cb3b749a670'
# export TWILIO_AUTH_TOKEN='312beff834e6dfb101e11758c6812b88'