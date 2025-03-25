#!/usr/bin/env python

import json
from datetime import datetime
import calendar

data = {}

# Get current time and date
now = datetime.now()

# Format the output
formatted_time = now.strftime(" %Hh%M   %a, %d %b")
data['text'] = formatted_time

# Generate the calendar structure
cal = calendar.Calendar()
month_days = cal.monthdayscalendar(now.year, now.month)
data['tooltip'] = f"{now.strftime('%B')}, {now.year} 🗓️\n\nMo Tu We Th Fr Sa Su\n"

for week_index, week in enumerate(month_days):
    week_data = ''
    for day in week:
        if day == 0:
            week_data += '   '  # Keep spacing for empty days
        else:
            week_data += f"{day:02d} "  # Format days with two digits
    data['tooltip'] += week_data
    if week_index < len(month_days) - 1:
            data['tooltip'] += "\n"

# Output JSON
print(data['tooltip'])  # Print formatted calendar for debugging
print(json.dumps(data))  # Print JSON output
