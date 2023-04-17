from discord.ext import commands
from core.classes import Cog_Extension
import json
from function.message import generate_embed
import asyncio

class GetList(Cog_Extension):

    @commands.Cog.listener()
    async def on_ready(self):
        print('GetList is ready')

    @commands.command()
    async def list(self, ctx):
        with open('document/contests.json', 'r') as file:
            contests = file.read()
            contests = json.loads(contests)
        channel = ctx.channel
        for i in contests.keys():
            print(contests[i])
            embed = generate_embed(contests[i])
            await channel.send(embed=embed)
            await asyncio.sleep(0.5)
            
    @commands.command()
    async def next(self, ctx):
        with open('document/contests.json', 'r') as file:
            contests = file.read()
            contests = json.loads(contests)
        channel = ctx.channel
        next_contest = {}
        next_contest['relativeTimeSeconds'] = -100000000000000000
        for i in contests.keys():
            if contests[i]['relativeTimeSeconds'] > next_contest['relativeTimeSeconds']:
                next_contest = contests[i]
        embed = generate_embed(next_contest)
        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GetList(bot))