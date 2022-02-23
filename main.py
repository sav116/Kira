# ----------------------
# -*- coding: utf-8 -*-
# Script by Artem.S.
# ---------------------

import requests
import os
import time

from config import KIRA_URL, KIRA_MONIKER, BOT_TOKEN, CHAT_ID


def is_active_validator_() -> bool:
    res = requests.get(KIRA_URL).json()
    for validator in res["validators"]:
        if validator['moniker'] == KIRA_MONIKER:
            return validator['status'] == 'ACTIVE'


def is_avail_space() -> bool:
    os.system('df -Th > /tmp/df.log')
    with open('tmp.txt') as f:
        for i in f.readlines():
            use = i.split()
            if '%' in use[5] and use[5][0].isdigit() and use[6] == '/':
                return int(use[5][:-1]) <= 90


def send_telegram(reason: str = None):
    token = BOT_TOKEN
    url = "https://api.telegram.org/bot"
    channel_id = CHAT_ID
    url += token
    method = url + "/sendMessage"

    text = 'Validator status is ACTIVE'

    if reason == 'space':
        text = 'Available free space on / less than 10%'

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")


if __name__ == "__main__":
    while True:
        time.sleep(60)
        if not is_avail_space():
            send_telegram(reason='space')
        if is_active_validator_():
            send_telegram(reason='status')
