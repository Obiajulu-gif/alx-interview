#!/usr/bin/python3
"""
Log Parsing
"""
import sys
import re

total_file_size = 0
status_code_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
pattern = re.compile(r'\S+ - \[\S+ \S+\] "\S+ \S+ \S+" (\d{3}) (\d+)')

line_count = 0
try:
    while (line := sys.stdin.readline().strip()):
        match = pattern.search(line)
        if match:
            status_code, file_size = match.groups()
            total_file_size += int(file_size)
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            line_count += 1

        if line_count % 10 == 0:
            print("File size: {}".format(line_count))
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print("{}: {}".format(code, status_code_count[code]))

            status_code_count = {code: 0 for code in status_code_count}
except KeyboardInterrupt:
    print("File size: {}".format(line_count))
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print("{}: {}".format(code, status_code_count[code]))
    sys.exit()
