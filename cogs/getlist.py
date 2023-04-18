from discord.ext import commands
from core.classes import Cog_Extension
import json
from function.message import generate_notice_embed
from function.message import generate_list_embed
import asyncio

class GetList(Cog_Extension):

    @commands.Cog.listener()
    async def on_ready(self):
        print('GetList is ready')

    @commands.command()
    async def recent(self, ctx):
        with open('document/contests.json', 'r') as file:
            contests = file.read()
            contests = json.loads(contests)
        channel = ctx.channel
        embed = generate_list_embed(contests)
        await channel.send(embed=embed)
        # for i in contests.keys():
        #     print(contests[i])
        #     embed = generate_notice_embed(contests[i])
        #     await channel.send(embed=embed)
        #     await asyncio.sleep(0.5)
            
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
        embed = generate_notice_embed('下個競賽', next_contest)
        await channel.send(embed=embed)

    @commands.command()
    async def id(self, ctx, extension):
        with open('document/contests.json', 'r') as file:
            contests = file.read()
            contests = json.loads(contests)
        channel = ctx.channel
        if extension in contests.keys():
            embed = generate_notice_embed('競賽資訊', contests[extension])
            await channel.send(embed=embed)
        else:
            await channel.send('此競賽不存在或已結束')
async def setup(bot):
    await bot.add_cog(GetList(bot))