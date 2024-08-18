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
#respuesta user
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("Excelente, entonces estamos listos para iniciar con este plan.")  
        else:
            await ctx.send("No hay ningun problema ¡iniciemos entonces con tu primer plan!")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

    await ctx.send("Primero que todo,¿Que es un plan alimentario?")
    await ctx.send("Un plan alimentario es una estrategia o esquema que detalla qué tipos y cantidades de alimentos se deben consumir a lo largo de un período determinado, generalmente con el objetivo de promover la salud, alcanzar metas nutricionales específicas, o manejar condiciones de salud. Este plan se basa en las necesidades individuales, como la edad, sexo, nivel de actividad física, y cualquier condición médica, asegurando un equilibrio adecuado de nutrientes esenciales como proteínas, carbohidratos, grasas, vitaminas, y minerales.")
    await ctx.send("¿Quieres saber que alimentos se encuentran en un buen plan alimentario? Responde 'si' o 'no' ")
    response1 = await bot.wait_for('message', check=check)

    if response1:
        if response1.content in ['sí', 'si']:
            await ctx.send("Proteínas: Carnes magras, pescado, huevos, legumbres, tofu.")
            await ctx.send("Carbohidratos complejos: Arroz integral, quinoa, avena, papas, batatas.")
            await ctx.send("Grasas saludables: Aceite de oliva, aguacate, nueces, semillas.")
            await ctx.send("Frutas y verduras: Variadas y de todos los colores, para obtener diferentes nutrientes y antioxidantes.")
            await ctx.send("Lácteos o alternativas: Yogur, leche, quesos bajos en grasa, bebidas vegetales fortificadas.")
            await ctx.send("Y por ultimo, pero no menos importante, Hidratación: Agua, infusiones sin azúcar.")
        elif response1.content in ['no']:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

bot.run("token bot")
