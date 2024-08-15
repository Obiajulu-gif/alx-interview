#!/usr/bin/python3
"""
Log Parsing
"""
import sys
import re
from typing import Dict, Pattern, Tuple

# Initialize total file size and a dictionary to count status codes
total_file_size: int = 0
status_code_count: Dict[str, int] = {
    str(code): 0 for code in [
        200,
        301,
        400,
        401,
        403,
        404,
        405,
        500]}

# Compile a regular expression to match the log format
log_pattern: Pattern = re.compile(
    r'\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

line_count: int = 0
try:
    for line in sys.stdin:
        # Use regex to find matches
        match: re.Match = log_pattern.search(line)
        if match:
            status_code, file_size = match.groups()
            total_file_size += int(file_size)
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            line_count += 1

        # After every 10 lines or at a keyboard interruption, print statistics
        if line_count % 10 == 0 or KeyboardInterrupt:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_code_count.keys(), key=int):
                if status_code_count[code] > 0:
                    print("{}: {}".format(code, status_code_count[code]))

except KeyboardInterrupt:
    # Print statistics upon keyboard interruption
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_count.keys(), key=int):
        if status_code_count[code] > 0:
            print("{}: {}".format(code, status_code_count[code]))
    sys.exit(0)
