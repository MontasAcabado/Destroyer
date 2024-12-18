from dotenv import load_dotenv
import discord
import os

load_dotenv()
token = str(os.getenv("TOKEN"))
bot = discord.Bot()

# -------- EVENTOS --------

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.mention}! Enjoy your stay here.")

# -------- COMANDOS --------

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond(f"Hey! {ctx.user}")
   


bot.run(os.getenv('TOKEN'))
