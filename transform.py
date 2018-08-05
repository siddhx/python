# transform.py
import sys


def matchinglines(pattern, path):
    with open(path) as handle:
        for line in handle:
            if pattern in line:
                yield line.rstrip('\n')


def parse_log_records(lines):
    for line in lines:
        level, message = line.split(": ", 1)
        yield {"level":level, "message":message}


pattern, path = sys.argv[1], sys.argv[2]
log_lines = matchinglines(pattern, path)

for line in parse_log_records(log_lines):
    print(line)