from twilio.rest import Client
 
 
account_sid = "ACC SID FROM CONSOLE"

auth_token = "AUTH_TOKEN FROM CONSOLE"

client = Client(account_sid,auth_token)

message = client.messages.create(
    to= "+reciving side number",
    from_ = "+sending side number",
    body= "Hello this is a Test!!!!")

print(message.sid)