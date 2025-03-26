#!/usr/bin/env python

import json
from datetime import datetime
import calendar

data = {}

# Get current time and date
now = datetime.now()
current_day = now.day

# Format the output
formatted_time = now.strftime(" %Hh%M   %a, %d %b")
data['text'] = formatted_time

# Generate the calendar structure
cal = calendar.Calendar()
month_days = cal.monthdayscalendar(now.year, now.month)
data['tooltip'] = f'<b>{now.strftime('%B')}, {now.year} 🗓️</b>\n\n<span color="red"><b>Mo Tu We Th Fr Sa Su</b></span>\n'

for week_index, week in enumerate(month_days):
    week_data = ''
    for day in week:
        if day == 0:
            week_data += '   '  # Keep spacing for empty days
        else:
            if day == current_day:
                week_data += f'<span color="red"><b>{day:02d}</b></span>'  # Highlight current day in red
            else:
                week_data += f"{day:02d}"
            if day != week[6]:  # Avoid adding space at the end of the line
                week_data += ' '
    data['tooltip'] += week_data
    if week_index < len(month_days) - 1:
        data['tooltip'] += "\n"

# Output JSON
print(json.dumps(data))
