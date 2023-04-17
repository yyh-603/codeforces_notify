from discord.ext import commands
from core.classes import Cog_Extension

class Hello(Cog_Extension):
    
    @commands.command()
    async def hello(self, ctx):
        print('Hello is ready.')
        await ctx.send(f"Hi! <@{ctx.author.id}>")
        
async def setup(bot):
    await bot.add_cog(Hello(bot))