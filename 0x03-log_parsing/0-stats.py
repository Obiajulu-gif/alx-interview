#!/usr/bin/python3
"""
Log Parsing
"""
import sys
import re

total_file_size = 0
status_code_count = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
pattern = re.compile(
    r'\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

line_count = 0
try:
    for line in sys.stdin:
        line = line.strip()
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
    for code in sorted(status_code_count.keys(), key=int):
        if status_code_count[code] > 0:
            print("{}: {}".format(code, status_code_count[code]))
    sys.exit()
