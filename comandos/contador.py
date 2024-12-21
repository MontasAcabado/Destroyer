import discord

def setup(bot):

    contador = {"valor": 1,
                "mensagem": None}

    class Botao1(discord.ui.View):

        @discord.ui.button(label="Clica-me!", style=discord.ButtonStyle.primary) 
        async def clicar_botao(self, button, interaction):
            contador["valor"] += 1
            await interaction.response.defer() 
            await contador["mensagem"].edit(f"Contador: {contador["valor"]}")

        async def on_timeout(self):
            self.clear_items()
            await contador["mensagem"].edit(view=self)


    @bot.slash_command(name="contar", description="Comeca a contar")
    async def contar(ctx: discord.ApplicationContext):
        await ctx.respond(f"Contador: {contador["valor"]}", view=Botao1())
        contador["mensagem"] = await ctx.interaction.original_response()