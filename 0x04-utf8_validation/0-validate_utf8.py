#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    def is_start_of_utf8(byte):
        """ check if a byte starts with the correct number of leading '1's """
        return byte >> 6 == 0b10

    # Variable to keep track of the number of expected following bytes
    expected_following_bytes = 0

    # Iterate through each integer in the data set
    for num in data:
        # Check the most significant bits
        if expected_following_bytes == 0:
            # Check number of expected following bytes for the current char
            if num >> 7 == 0:
                # Single-byte character
                expected_following_bytes = 0
            elif num >> 5 == 0b110:
                # Two-byte character
                expected_following_bytes = 1
            elif num >> 4 == 0b1110:
                # Three-byte character
                expected_following_bytes = 2
            elif num >> 3 == 0b11110:
                # Four-byte character
                expected_following_bytes = 3
            else:
                # Invalid leading bits
                return False
        else:
            # Check if the current byte is a continuation byte
            if not is_start_of_utf8(num):
                return False
            expected_following_bytes -= 1

    # If all bytes are processed correctly,and no incomplete character are left
    return expected_following_bytes == 0
