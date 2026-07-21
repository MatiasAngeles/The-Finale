import discord
from discord.ext import commands
import bot_logic
import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=settings.COMMAND_PREFIX, intents=intents)


@bot.event
async def on_ready():
    """Bot joining event."""
    print(f"[{bot.user.name}] is here...")


@bot.event
async def on_message(message):
    """Monitors user messages and logs activity."""
    if message.author.bot:
        return

    bot_logic.registrar_actividad(
        user_id=str(message.author.id),
        username=message.author.name,
        accion="message",
    )

    await bot.process_commands(message)


@bot.command(name="meeting")
async def meeting(ctx):
    """Forces the 3 bots about their talk with the user."""
    user_id = str(ctx.author.id)
    username = ctx.author.name

    bot_logic.registrar_actividad(
        user_id=user_id, username=username, accion="command"
    )

    datos = bot_logic.obtener_datos_usuario(user_id)

    if not datos:
        await ctx.send("We couldn't get user data from backend...")
        return

    mensajes = datos.get("messages_sent", 0)
    comandos = datos.get("commands_used", 0)

    await ctx.send(
        f"We are checking **{username}** past...\n"
        "──────────────────────────────────"
    )

    opinion_social = bot_logic.evaluar_comportamiento_social(mensajes)
    await ctx.send(
        f"**AnnoyinBot:** I checked your {mensajes} total messages.\n"
        f"> *\"{opinion_social}\"*"
    )

    opinion_tecnica = bot_logic.evaluar_comportamiento_tecnico(comandos)
    await ctx.send(
        f"**HelpeRBoT:** You used {comandos} of them in total.\n"
        f"> *\"{opinion_tecnica}\"*"
    )

    opinion_analitica = bot_logic.evaluar_comportamiento_analitico(
        mensajes, comandos
    )
    await ctx.send(
        f"**ListBot:** Based on your helping...\n"
        f"> *\"{opinion_analitica}\"*"
    )


if __name__ == "__main__":
    bot.run(settings.THE_MEETING_BOT)
