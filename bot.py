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

    bot_logic.activity(
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

    bot_logic.activity(
        user_id=user_id, username=username, accion="command"
    )

    data = bot_logic.get_user_data(user_id)

    if not data:
        await ctx.send("We couldn't get user data from backend...")
        return

    message = data.get("messages_sent", 0)
    comands = data.get("commands_used", 0)

    await ctx.send(
        f"We are checking **{username}** past...\n"
        "──────────────────────────────────"
    )

    anno_nion = bot_logic.annoyed(message)
    await ctx.send(
        f"**1:** I checked your {message} total messages.\n"
        f"> *\"{anno_nion}\"*"
    )

    eco_opinion = bot_logic.ecosystem(comands)
    await ctx.send(
        f"**2:** You used {comands} of them in total.\n"
        f"> *\"{eco_opinion}\"*"
    )

    list_opinion = bot_logic.list(
        message, comands
    )
    await ctx.send(
        f"**3:** Based on your helping...\n"
        f"> *\"{list_opinion}\"*"
    )


if __name__ == "__main__":
    bot.run(settings.THE_MEETING_BOT)
