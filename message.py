import discord
import datetime

def generate_embed(contest):
    # start format
    start_time = datetime.datetime.fromtimestamp(contest["startTimeSeconds"], datetime.timezone(datetime.timedelta(hours=8)))
    start_format = start_time.strftime('%Y/%m/%d %H:%M:%S')

    # calculate interval time
    interval = -contest['relativeTimeSeconds']
    interval_days = interval // 86400
    interval = interval % 86400
    interval_hours = interval // 3600
    interval = interval % 3600
    interval_mins = interval // 60
    interval = interval % 60
    interval_secs = interval

    # generate embed message
    embed = discord.Embed(title = ':loudspeaker: 比賽通知', url = 'https://codeforces.com/contests')
    embed.add_field(name='標題', value=contest['name'], inline=False)
    embed.add_field(name='時間', value = start_format, inline=False)
    embed.add_field(name='id', value=contest['id'], inline=False)
    embed.add_field(name='距離現在', value='{} day, {} hr, {} min, {} s'.format(interval_days, interval_hours, interval_mins, interval_secs), inline=False)
    
    return embed