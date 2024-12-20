import discord

def setup(bot):

    @bot.slash_command(name="bestadmin", description="baest")
    async def bestadmin(ctx: discord.ApplicationContext):
        await ctx.respond("não é o Monteiro!")
