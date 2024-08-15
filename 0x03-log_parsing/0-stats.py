#!/usr/bin/python3
"""
Log Parsing
"""
import sys
import re

total_file_size = 0
status_code_count = {
    str(code): 0 for code in [
        200,
        301,
        400,
        401,
        403,
        404,
        405,
        500]}


line_count = 0
try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()
        if len(parts) < 7:
            continue

        status_code = parts[7]
        file_size = int(parts[8])

        total_file_size += int(file_size)

        if status_code in status_code_count.keys():
            status_code_count[status_code] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print("{}: {}".format(code, status_code_count[code]))

except KeyboardInterrupt:
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print("{}: {}".format(code, status_code_count[code]))
    sys.exit(0)
