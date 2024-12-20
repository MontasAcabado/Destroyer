import discord

def setup(bot):

    @bot.slash_command(name="projeto", description="Vai buscar o projeto à net")
    async def projeto(ctx: discord.ApplicationContext):
        await ctx.respond(f"Link do projeto [Projeto](https://github.com/MontasAcabado/Destroyer)")