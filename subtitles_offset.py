#!/bin/python3

import sys
from datetime import datetime
from datetime import timedelta

out = []

# Return true if \c is a digit
def is_digit(c):
    int_c = ord(c)
    return int_c >= 48 and int_c <= 57

# Return true if \s is a number
def is_num(s):
    for c in s:
        if (not(is_digit(c))):
            return False
    return True

# Convert \date to a string with .rst format
def to_str(date):
    return "{0:02}:{1:02}:{2},{3:3.3}".format(
            date.hour, date.minute, date.second, str(date.microsecond))

with open(sys.argv[1], 'r', encoding='utf-8') as ifile:

    # Split file in lines
    lines = ifile.read().split('\n')

    # Time offset
    offset = timedelta(minutes=int(sys.argv[2]), seconds=int(sys.argv[3]))
    # Index offset
    while (len(lines[0]) > 0) and not(is_digit(lines[0][0])):
        lines[0] = lines[0][1:]
    offset_s = int(lines[0]) - 1;

    for line in lines:
        if (line[0:3] == "00:"):                    # Timestamps
            newline = ""

            # Add begin of subtitle
            begin_str = line[0:line.find(' ')]
            begin = datetime.strptime(begin_str, "%H:%M:%S,%f")
            newline += to_str(begin - offset)

            # Add the arrow
            newline += " --> "

            # Add end of subtitle
            end_str = line[line.rfind(' ') + 1:]
            end = datetime.strptime(end_str, "%H:%M:%S,%f")
            newline += to_str(end - offset)

            out.append(newline)
        elif (len(line) > 0 and is_num(line)):      # Index
            out.append(str(int(line) - offset_s))
        else:                                       # Subtitles
            out.append(line)

# Write output in .second file
with open(sys.argv[1] + ".second", "w") as ofile:
    for line in out:
        ofile.write(str(line) + '\n')
