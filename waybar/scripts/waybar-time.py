#!/usr/bin/env python

import json
import datetime
import calendar

data = {}

# Get current time and date
now = datetime.datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year

# Format the output
formatted_time = now.strftime(" %H:%M   %a, %d %b")
data['text'] = formatted_time

# Generate the calendar structure
cal = calendar.Calendar()
month_days = cal.monthdayscalendar(current_year, current_month)
data['tooltip'] = f'<b>{now.strftime("%B")},</b> <span color="grey">{current_year}</span>\n\n<span color="red"><b>Mo Tu We Th Fr Sa Su</b></span>\n'

# Get last day of previous month
prev_month_last_day = (datetime.datetime(current_year, current_month, 1) - datetime.timedelta(days=1)).day
next_month_day = 1

for week_index, week in enumerate(month_days):
    week_data = ''
    past_month_day = prev_month_last_day - week.count(0) + 1  # Start past month days

    for day in week:
        if day == 0:
            if week_index == 0:
                week_data += f'<span color="grey">{past_month_day:02d}</span>'
                past_month_day += 1
            else:
                week_data += f'<span color="grey">{next_month_day:02d}</span>'
                next_month_day += 1
        else:
            if day == current_day:  # Highlight current day in red
                week_data += f'<span color="red"><b>{day:02d}</b></span>'
            else:  # others days remain normal
                week_data += f"{day:02d}"
        week_data += ' '

    data['tooltip'] += week_data.strip()
    if week_index < len(month_days) - 1:
        data['tooltip'] += '\n'

# Output JSON
print(data['tooltip'])
print(json.dumps(data))
