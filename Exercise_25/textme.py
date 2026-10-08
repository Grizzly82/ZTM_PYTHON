# pyright: reportMissingImports=false
import datetime


try:
    from twilio.rest import Client
except ImportError as exc:
    raise ImportError("Install the Twilio package with: pip install twilio") from exc


account_sid = 'AC1a00d63c63a863addae329d5bbf20801'
auth_token = 'c96cb435642790c393ff626e16431aeb'
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid='MGeed1ea179c4dc144a38e83025fef78d1',
  body='Ahoy 👋 ' + str(datetime.datetime.now()),
  to='+18777804236'
)
# Get current timestamp
current_timestamp = datetime.datetime.now()
print(message.sid + " sent successfully" + " at " + str(current_timestamp))