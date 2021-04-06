import requests
import json
import pandas as pd
from datetime import datetime
from pytz import timezone


def get_total_xp(username):
    url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws"
    pair = {"player":username}

    page = requests.get(url, params = pair)

    hs = page.text.split("\n")
    hs = [word for line in hs for word in line.split(",")]
    hs = [float(i) for i in hs[:-1]]

    return(hs[2])
