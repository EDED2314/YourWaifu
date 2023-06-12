import asyncio
from typing import Any, Coroutine
import discord
from discord.ext.commands import Context
from discord.ext import commands
from discord.ext.commands.context import Context
from dotenv import load_dotenv
import os

load_dotenv()


class Waifu(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all(), command_prefix="waifu.")
        self.game = discord.Game("selfie.io")

    async def on_ready(self):
        await self.change_presence(status=discord.Status.idle, activity=self.game)

        print("Logged on as", self.user)
        print(bot.user.id)

    async def on_message(self, msg: discord.Message):
        await self.process_commands(msg)
        if msg.author.bot:
            return

        if self.user not in msg.mentions:
            return
        await msg.channel.send("hi")

        content = str(msg.content).strip(f"<@{self.user.id}>")

        print(content)

    async def on_command_error(self, context: Context, exception):
        print(context.author)
        print(exception)
        return await super().on_command_error(context, exception)


async def load_extensions(bot):
    await bot.load_extension(f"cogs.sync")


bot = Waifu()


@bot.tree.command()
async def help(interaction: discord.Interaction):
    """Help"""  # Description when viewing / commands
    await interaction.response.send_message("hello")


async def main():
    async with bot:
        await load_extensions(bot)
        await bot.start(os.getenv("TOKEN"))


if __name__ == "__main__":
    asyncio.run(main())
