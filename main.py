from dotenv import load_dotenv
import discord
import os

# comandos
from comandos.hello import setup as comando_hello
from comandos.projeto import setup as comando_projeto
from comandos.bestadmin import setup as comando_bestadmin
from comandos.contador import setup as comando_contador
# eventos
from eventos.on_ready import setup as evento_inicializa
from eventos.on_member_join import setup as evento_entra_membro
from eventos.sigma import setup as evento_sigma





# Vai buscar o token
load_dotenv()
token = str(os.getenv("TOKEN"))

# Cria o objeto bot
bot = discord.Bot()





# é necessário passar o objeto bot para os outros ficheiros poderem aceder o objeto 

# -------- EVENTOS --------

evento_inicializa(bot)
evento_entra_membro(bot)
evento_sigma(bot)


# -------- COMANDOS --------

comando_hello(bot)
comando_projeto(bot)
comando_bestadmin(bot)
comando_contador(bot)





# dá run
bot.run(os.getenv('TOKEN'))