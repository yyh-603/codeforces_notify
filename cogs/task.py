from core.classes import Cog_Extension
import asyncio
from function.update import update
import json
from function.message import generate_notice_embed
import time

FIRST_MESSAGE_TIME = 86400
SECOND_MESSAGE_TIME = 600

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(1088705957426638921)
            while not self.bot.is_closed():

                try:
                    # from codeforces update contests
                    update()
                    
                    # read contests
                    with open('document/contests.json', 'r') as file:
                        contests = file.read()
                        contests = json.loads(contests)
    
                    # read channels
                    with open('document/channels.json', 'r') as file:
                        channels = file.read()
                        channels = json.loads(channels)
                    
                    # new_list append 'BEFORE' contests
                    new_list = dict()
                    
                    for i in contests.keys():
                        # contest start in one day
                        if -FIRST_MESSAGE_TIME <= contests[i]['relativeTimeSeconds'] and contests[i]['first_msg'] == False:
                            contests[i]['first_msg'] = True
                            embed = generate_notice_embed('競賽通知', contests[i])
                            for obj in channels:
                                channel = self.bot.get_channel(obj['id'])
                                await channel.send(obj['notice'] + ' 競賽在一天後開始，記得註冊')
                                await channel.send(embed=embed)
                                # await asyncio.sleep(10)
                                
                        # contest start in 10 minutes
                        elif -SECOND_MESSAGE_TIME <= contests[i]['relativeTimeSeconds'] and contests[i]['second_msg'] == False:
                            contests[i]['second_msg'] = True
                            embed = generate_notice_embed('競賽通知', contests[i])
                            for obj in channels:
                                channel = self.bot.get_channel(obj['id'])
                                await channel.send(obj['notice'] + ' 競賽在10分鐘後開始，記得註冊')
                                await channel.send(embed=embed)
                                # await asyncio.sleep(10)
                        
                        # contest isn't start
                        if contests[i]["relativeTimeSeconds"] <= 0:
                            new_list[str(contests[i]['id'])] = contests[i]
                            
                    # erase contest NOT 'BEFORE'
                    with open('document/contests.json', 'w+') as file:
                        file.write(json.dumps(new_list, indent=4))
                    print("at " + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) + " uptade")
                    await asyncio.sleep(10)

                except Exception as ERROR:
                    print(ERROR)
    
        self.bg_task = self.bot.loop.create_task(interval())
    
async def setup(bot):
    await bot.add_cog(Task(bot))