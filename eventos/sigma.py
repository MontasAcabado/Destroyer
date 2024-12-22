import discord

def setup(bot):

    @bot.event
    async def on_message(message):
        if message.author.id != 1318909983957585920:
            await message.channel.send("https://www.youtube.com/watch?v=frAhxXbLetk")