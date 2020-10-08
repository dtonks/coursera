#!/bin/bash

meeting_info=$(zenity --forms \
    --title 'Meeting' --text 'Reminder informtion' \
    --add-calendar 'Date' --add-entry 'Title' \
    --add-entry 'Emails' \
    --forms-date-format='%Y-%m-%d' \
    2>/dev/null)

if [[ -n '$meeting_info' ]]; then
    python3 send_reminders.py "$meeting_info"
fi
