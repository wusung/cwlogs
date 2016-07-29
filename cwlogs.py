#!/usr/bin/env python

from datetime import datetime

import argparse
import calendar
import dateutil.parser
import json
import os
import pprint
import subprocess

# Set up timezone to local
os.environ['TZ']='Asia/Taipei'
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-o', '--hour', help='Specify hor rage to limit the log')
parser.add_argument('-d', '--day', help='Specify day rage to limit the log')
parser.add_argument('-l', '--log', help='Specify aws log group name')
parser.add_argument('-p', '--prefix', help='Specify the default prefix of aws log group name. The default is ')
parser.add_argument('-n', '--no-color', help='Specify day rage to limit the log')
args = parser.parse_args()

## Set the necessary variables for aws log command
SINCE="1d ago"
LOGGROUPNAME="web-kkbox-contract.kkcontract"
PREFIX = 'web-kkbox-contract'

if args.hour:
    SINCE = args.hour + 'h ago'
elif args.day:
    SINCE = args.day + "d ago"
else:
    SINCE = "1d ago"

if args.log:
    LOGGROUPNAME = args.log

if args.prefix:
    PREFIX = args.prefix

def main():
    aws_args = []
    aws_args.append("awslogs get " + LOGGROUPNAME + " --start='%s' --no-color" % SINCE)

    proc = subprocess.Popen(aws_args, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    for line in out.splitlines():
        l = line.decode('utf-8')
        group_name = l.split(' ')[0]
        logger_name = l.split(' ')[1]
        content = l.split(' ')[2:]
        o = json.loads(' '.join(content))
        d = dateutil.parser.parse(o.get('time'))
        ts = calendar.timegm(d.utctimetuple()) 
        print("%s %s [%s] %s - %s %s" % (
              datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
              o.get('level'),
              o.get('thread'),
              o.get('hostname'),
              o.get('class'), 
          o.get('message')))

if __name__ == '__main__':
    main()

