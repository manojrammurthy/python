from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC26e0f5fa6ecd0e30edf9699751c94aea"
auth_token  = "b49994635e3dcdf910ae92d3b91e749f"
client = TwilioRestClient(account_sid, auth_token)
 
call = client.calls.create(#body="yenda rajeefa <3",
    to="+919844027600",    # Replace with your phone number
    from_="+15089212068",
    url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient") # Replace with your Twilio number
print call.sid