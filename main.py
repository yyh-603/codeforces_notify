import discord
import os
import asyncio
from function.alive import stay
from discord.ext import commands

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents = intents)

TOKEN = os.environ['CODEFORCES_NOTIFY_TOKEN']

@bot.event
async def on_ready():
    game = discord.Game('CF燒雞中')
    await bot.change_presence(status = discord.Status.online, activity = game)
    print('bot is ready.')


async def first_load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'loaded {extension} done')

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'unloaded {extension} done')

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'reloaded {extension} done')

async def main():
    async with bot:
        await first_load()
        await bot.start(TOKEN)

stay()
asyncio.run(main())