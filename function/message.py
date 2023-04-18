import discord
import datetime

def generate_notice_embed(title, contest):
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

    duration = contest["durationSeconds"]
    duration_days = duration // 86400
    duration = duration % 86400
    duration_hours = duration // 3600
    duration = duration % 3600
    duration_mins = duration // 60
    duration = duration % 60
    duration_secs = duration

    # generate embed message
    embed = discord.Embed(title = ':loudspeaker: ' + title, url = 'https://codeforces.com/contests')
    embed.add_field(name='標題', value=contest['name'], inline=False)
    embed.add_field(name='時間', value = start_format, inline=False)
    embed.add_field(name='id', value=contest['id'], inline=False)
    embed.add_field(name='距離現在', value=f'{interval_days} day, {interval_hours} hr, {interval_mins} min, {interval_secs} s', inline=False)
    if(duration_days != 0):
        embed.add_field(name='時長', value=f'{duration_days} day, {duration_hours} hr, {interval_mins} min, {interval_secs} s', inline=False)
    else:
        embed.add_field(name='時長', value=f'{duration_hours} hr, {duration_mins} min, {duration_secs} s', inline=False)
    
    return embed

def generate_list_embed(contests):
    contest_list = list()
    for k in contests.keys():
        now = contests[k]
        contest_list.append((now["startTimeSeconds"], now['id'], now['name']))
    contest_list.sort()
    embed = discord.Embed(title = ':loudspeaker: 近期競賽', url = 'https://codeforces.com/contests')
    for i in range(len(contest_list)):
        start_time = datetime.datetime.fromtimestamp(contest_list[i][0], datetime.timezone(datetime.timedelta(hours=8)))
        start_format = start_time.strftime('%Y/%m/%d %H:%M:%S')
        embed.add_field(name=f'{contest_list[i][1]}  ' + contest_list[i][2], value='開始時間  ' + start_format, inline=False)
    return embed
        