#!/usr/bin/env python

import json

from datetime import datetime

data = {}


def format_time(time):
    return time.replace("00", "").zfill(2)

print(json.dumps(data))
