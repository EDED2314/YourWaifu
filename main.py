import asyncio
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TOKEN")


class Waifu(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.game = discord.Game("selfie.io")

    async def on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=self.game)
        print("Logged on as", self.user)

    async def on_message(self, msg: discord.Message):
        if msg.author.bot:
            return

        if self.user not in msg.mentions:
            return
        await msg.channel.send("hi")

    # async def on_message(self, message):
    #     # don't respond to ourselves
    #     if message.author == self.user:
    #         return

    #     if message.content == "ping":
    #         await message.channel.send("pong")


client = Waifu()
client.run(token)
