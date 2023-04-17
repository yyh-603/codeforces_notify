# CodeForces Notify

## 功能

競賽一天前及十分鐘前會發送訊息到指定頻道，提醒競賽時間。

## 各檔案說明

### main.py

主程式，執行機器人及發送訊息等功能。

### update.py

爬取競賽資訊，更新至contests.json

### contests.json

儲存競賽

競賽資訊範例如下
contests['id'] = contest
```json
"1813": {
        "id": 1813,
        "name": "ICPC 2023 Online Spring Challenge powered by Huawei",
        "type": "IOI",
        "phase": "BEFORE",
        "frozen": false,
        "durationSeconds": 1209600,
        "startTimeSeconds": 1681383600,
        "relativeTimeSeconds": -38355,
        "first_msg": true,
        "second_msg": false
    }
```

### message.py

產生Discord訊息

### channels.json

儲存每個要通知的頻道

### alive.py

程式來自 [這裡](https://ithelp.ithome.com.tw/m/articles/10273878?fbclid=IwAR29vAjutcjIbvTCseiXhufU6FkTbGrkz4X5YI1OuxufcJndRogpm4BzSJA)

用於使機器人隨時在線

---

2023/04/17 更新

1. 更改專案架構

2. 增加prefix_command
    (1) !list：列出當前競賽
    (2) !next：列出最近競賽