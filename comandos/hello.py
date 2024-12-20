import discord

def setup(bot):

    @bot.slash_command(name="hello", description="Say hello to the bot")
    async def hello(ctx: discord.ApplicationContext):
        await ctx.respond(f"Hey! {ctx.user}")
