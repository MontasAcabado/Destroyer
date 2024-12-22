import discord
from random import randint

def setup(bot):

    propriedades = {"numerorandom": None,
                    "mensagem": None,
                    "numero": None,
                    "tentativas": 0}

    class Botoes(discord.ui.View):

        @discord.ui.button(label="Lower", style=discord.ButtonStyle.primary) 
        async def lower(self, button, interaction):
            await interaction.response.send_message("Clicaste no Lower") 
            decisao()

        @discord.ui.button(label="Higher", style=discord.ButtonStyle.primary) 
        async def higher(self, button, interaction):
            await interaction.response.send_message("Clicaste no Higher") 
            decisao()

        async def on_timeout(self):
            self.clear_items()
            await propriedades["mensagem"].edit(view=self)


    @bot.slash_command(name="numguess", description="Comeca a contar")
    async def numguess(ctx: discord.ApplicationContext, numero: int):
        await ctx.respond(f"Tentativa: {numero}", view=Botoes())

        propriedades["mensagem"] = await ctx.interaction.original_response()
        propriedades["numerorandom"] = randint(0, 100)
        propriedades["numero"] = numero


    def decisao():
        print(propriedades["tentativas"])
        print(propriedades)
        propriedades["tentativas"] += 1