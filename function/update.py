import json
import time
import traceback
import requests
from bs4 import BeautifulSoup

def update():
    try:
        # get information
        url = "https://codeforces.com/api/contest.list?"
        response = requests.get(url)
        
        contests = BeautifulSoup(response.text, 'html5lib')
        temp = contests.find('body').getText()
        #print(temp)

        contests = temp
        # json to list
        contests = json.loads(contests)
        contests = contests['result']

        # list to dict
        # contests['id'] = contest
        temp = dict()
        for contest in contests:
            temp[str(contest['id'])] = contest
        contests = temp

        with open('document/contests.json', 'r') as file:
            now = file.read()
            now = json.loads(now)
            
            # update now
            for id in now.keys(): # type(id) == str
                # update infomation
                first = now[id]['first_msg']
                second = now[id]['second_msg']
                now[id] = contests[id]
                now[id]['first_msg'] = first
                now[id]['second_msg'] = second

            # add contest
            for contest in contests.values():
                if contest['phase'] == 'BEFORE' and (str(contest['id']) not in now.keys()):
                    contest['first_msg'] = False
                    contest['second_msg'] = False
                    now[contest['id']] = contest
        # rewrite
        with open('document/contests.json', 'w+') as file:
            file.write(json.dumps(now, indent=4))
        
    except Exception as ERROR:
        print(ERROR)