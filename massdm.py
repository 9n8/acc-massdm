import discord

token = input("Enter Token: ")
txt = input("Message: ")

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(txt)
      print(f"messaged: {user.name}")
    except:
       print(f"couldn't message: {user.name}")

client.run(token, bot=False)
