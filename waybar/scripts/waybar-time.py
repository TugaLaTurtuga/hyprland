#!/usr/bin/env python

import json
from datetime import datetime, timedelta, date
import calendar

data = {}

# Get current time and date
now = datetime.now()

# Format the output
formatted_time = now.strftime(" %H:%M   %a, %d %b")
data['text'] = formatted_time

# Generate an HTML calendar
def generate_calendar(year, month):
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)

    # HTML calendar structure
    html = '<table border="1" style="border-collapse: collapse; text-align: center;">'
    html += '<tr><th colspan="7">' + now.strftime('%B %Y') + '</th></tr>'
    html += '<tr><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr>'

    for week in month_days:
        html += '<tr>'
        for day in week:
            if day == 0:
                html += '<td></td>'
            else:
                cell_style = 'background: #ddd;' if day == now.day else ''
                html += f'<td style="{cell_style}">{day}</td>'
        html += '</tr>'

    html += '</table>'
    return html

# Store calendar as HTML
data['tooltip'] = generate_calendar(now.year, now.month)

# Output JSON
print(json.dumps(data))
