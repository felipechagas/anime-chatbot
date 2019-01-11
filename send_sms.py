from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5bb1242b97d3880aadf4b407730cf3eb"
# Your Auth Token from twilio.com/console
auth_token  = "57278821b1d2e8861a6a9a9c5a3b1d84"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5585986110919", 
    from_="+18329090952",
    body="Hello from Python!")

print(message.sid)