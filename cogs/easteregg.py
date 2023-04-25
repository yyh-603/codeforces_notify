from core.classes import Cog_Extension
from discord.ext import commands

class EasterEgg(Cog_Extension):

    @commands.Cog.listener()
    async def on_ready(self):
        print('easteregg is ready')
        
    @commands.command()
    async def 小丑(self, ctx):
        await ctx.send(f"<@{563006366520967168}> 是小丑🤡")
        # 719096615465517058
    

async def setup(bot):
    await bot.add_cog(EasterEgg(bot))