import discord

def setup(bot):

    @bot.event
    async def on_member_join(member):
        await member.send(f"Welcome to the server, {member.mention}! Enjoy your stay here.")
