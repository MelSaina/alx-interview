#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    split_line = line.split()
    if len(split_line) >= 9:
        try:
            file_size = int(split_line[-1])
            status_code = int(split_line[-2])
            total_size += file_size
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                if status_code not in status_codes:
                    status_codes[status_code] = 0
                status_codes[status_code] += 1
        except ValueError:
            pass
    return total_size, status_codes

if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            total_size, status_codes = parse_line(line, total_size, status_codes)

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

    print_stats(total_size, status_codes)