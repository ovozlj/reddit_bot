import praw
r = praw.Reddit(username = "No_Metal8219",
                password = "qwfpgjlu",
                client_id = "f5hqxxhMKk5Ci8bgh1SZFA",
                client_secret = "Q-idiMbzdYbV9iYveY4XU1vFLSHwjA",
                user_agent = "xiaoyang by /u/No_Metal8219")

messages = r.inbox.stream() # creates an iterable for your inbox and streams it
for message in messages: # iterates through your messages
  try:
    if message in r.inbox.mentions() and message in r.inbox.unread(): # if this messasge is a mention AND it is unread...
        message.reply("hello") # reply with this message
        message.mark_read() # mark message as read so your bot doesn't respond to it again...
  except praw.exceptions.APIException: # Reddit may have rate limits, this prevents your bot from dying due to rate limits
    print("probably a rate limit....")