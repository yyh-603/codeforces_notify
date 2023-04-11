import update
import discord
import os
import asyncio
import json
import time
from alive import stay
from message import generate_embed

# bot settings
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
TOKEN = os.environ['CODEFORCES_NOTIFY_TOKEN']

# const. settings

FIRST_MESSAGE_TIME = 86400
SECOND_MESSAGE_TIME = 600

@bot.event
async def on_ready():
    # bot status
    game = discord.Game('CF燒雞中')
    await bot.change_presence(status = discord.Status.online, activity = game)
    
    # send message
    while not bot.is_closed():
        # from codeforces update contests
        update.update()
        
        # read contests
        with open('contests.json', 'r') as file:
            contests = file.read()
            contests = json.loads(contests)
            
        # read channels
        with open('channels.json', 'r') as file:
            channels = file.read()
            channels = json.loads(channels)
            
        # new_list append 'BEFORE' contests
        new_list = dict()
        
        for i in contests.keys():
            # contest start in one day
            if -FIRST_MESSAGE_TIME <= contests[i]['relativeTimeSeconds'] and contests[i]['first_msg'] == False:
                contests[i]['first_msg'] = True
                embed = generate_embed(contests[i])
                for obj in channels:
                    channel = bot.get_channel(obj['id'])
                    await channel.send(obj['notice'] + ' 競賽在一天後開始，記得註冊')
                    await channel.send(embed=embed)
                    await asyncio.sleep(10)
                    
            # contest start in 10 minutes
            elif -SECOND_MESSAGE_TIME <= contests[i]['relativeTimeSeconds'] and contests[i]['second_msg'] == False:
                contests[i]['second_msg'] = True
                embed = generate_embed(contests[i])
                for obj in channels:
                    channel = bot.get_channel(obj['id'])
                    await channel.send(obj['notice'] + ' 競賽在10分鐘後開始，記得註冊')
                    await channel.send(embed=embed)
                    await asyncio.sleep(10)
            # contest isn't start
            if contests[i]["relativeTimeSeconds"] <= 0:
                new_list[str(contests[i]['id'])] = contests[i]
                
        # erase contest NOT 'BEFORE'
        with open('contests.json', 'w+') as file:
            file.write(json.dumps(new_list, indent=4))
        print('---------------------------')
        time.sleep(30)

@bot.event
async def on_message(message):
    pass

stay()
bot.run(TOKEN)