import discord

def setup(bot):

    contador = {"valor": 1}

    class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
        @discord.ui.button(label="Clica-me!", style=discord.ButtonStyle.primary) 
        async def button_callback(self, button, interaction):
            await interaction.response.send_message("Clicaste no butão!")
            contador["valor"] += 1 

    @bot.slash_command(name="contar", description="Comeca a contar")
    async def contar(ctx: discord.ApplicationContext):
        await ctx.respond(f"Contador: {contador["valor"]}", view=MyView())   