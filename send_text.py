from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3578295e05d99fab9c1f172390777566"
auth_token  = "b7c22244fec840104ab70a00c3842336"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello Alexis! This is Geng's Macbook!",
    to="+16179016601",    # Replace with your phone number
    from_="+14242767453") # Replace with your Twilio number
print message.sid