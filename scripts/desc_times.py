#!/usr/bin/env python
"""Script to quickly scan time across different locations on a particular date
for meetings.
"""
from datetime import datetime
import pytz
from datetime import tzinfo


def desc_time(hour=8, minute=0, day=1, month=11, year=2017, tzinfo=None):
    if tzinfo is None:
        tzinfo='US/Pacific'
    dt = datetime(year, month, day, hour, minute, 0, 0, tzinfo)
    collabtzs = tuple(('US/Pacific', 'America/Phoenix', 'US/Central', 'US/Eastern', 'Europe/Belfast',
                  'Europe/London', 'Europe/Paris', 'Europe/Stockholm'))
    lst = []
    for tz in collabtzs:
        lst.append(":".join(list((tz, dt.astimezone(pytz.timezone(tz)).strftime('%m-%d %H%M')))))
    return '\n'.join(lst)

if __name__=='__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='script for times of DESC SN collaborators')
    parser.add_argument('--tzinfo', default='US/Pacific', help='timezone string')
    parser.add_argument('--hour', type=int, default=8, help='time in hours 0-24')
    parser.add_argument('--minute', type=int, default=0, help='time in mins 0-60')
    parser.add_argument('--month', type=int, default=11, help='month number')
    parser.add_argument('--day', type=int, default=1, help='day')
    parser.add_argument('--year', type=int, default=2017, help='date in year')

    args = parser.parse_args()
    print(args)

    tstamps = desc_time(tzinfo=pytz.timezone(args.tzinfo), year=args.year, month=args.month,
                         day=args.day, hour=args.hour, minute=args.minute)
    print(tstamps)
