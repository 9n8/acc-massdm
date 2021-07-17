import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('Your Message')
      print(f"messaged: {user.name}")
    except:
       print(f"couldn't message: {user.name}")

client.run('Your Token', bot=False)