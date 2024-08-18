import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix= '$', intents=intents)
@bot.command()
async def nutricion(ctx):
    await ctx.send(f"""Hola, soy el bot {bot.user}!""")
    await ctx.send(f'Primero te voy a hablar de la importancia de una buena nutricion en TU vida')
    await ctx.send(f'La nutrición es crucial para mantener la salud, proporcionar energía, apoyar el crecimiento y reparar tejidos, y prevenir enfermedades.')
    # Enviar una pregunta al usuario
    await ctx.send("Haz seguido un plan alimentario antes? Responde con 'sí' o 'no'.")

bot.run('token bot')
