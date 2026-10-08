# pyright: reportMissingImports=false
import datetime


try:
    from twilio.rest import Client
except ImportError as exc:
    raise ImportError("Install the Twilio package with: pip install twilio") from exc


account_sid = '[insert_your_account_sid_here]'
auth_token = '[insert_your_auth_token_here]'
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid='[insert_your_messaging_service_sid_here]',
  body='Ahoy 👋 ' + str(datetime.datetime.now()),
  to='+18777804236'
)
# Get current timestamp
current_timestamp = datetime.datetime.now()
print(message.sid + " sent successfully" + " at " + str(current_timestamp))