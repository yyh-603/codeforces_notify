from discord.ext import commands
from core.classes import Cog_Extension

class Ping(Cog_Extension):

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping is ready.')

    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.bot.latency * 1000)
        print(bot_latency)
        await ctx.send(f'Ping is {bot_latency} ms')

async def setup(bot):
    await bot.add_cog(Ping(bot))