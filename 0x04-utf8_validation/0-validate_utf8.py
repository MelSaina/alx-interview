#!/usr/bin/python3
"""
UTF8 validation module
"""
def validUTF8(data):
    """
    Validates if data consists of
    valid utf-8 encoded characters
    """
    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            if (num >> 7) == 0:
                num_bytes = 1
            elif (num >> 5) == 0b110:
                num_bytes = 2
            elif (num >> 4) == 0b1110:
                num_bytes = 3
            elif (num >> 3) == 0b11110:
                num_bytes = 4
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
