import discord

def setup(bot):

    contador = {"valor": 1}

    @bot.slash_command(name="contar", description="Comeca a contar")
    async def contar(ctx: discord.ApplicationContext):
        await ctx.respond(f"Contador: {contador["valor"]}")
        contador["valor"] += 1    