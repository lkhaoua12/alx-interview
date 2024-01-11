#!/usr/bin/python3
""" A method that determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """  a method that determines if all the boxes can be opened. """

    boxes_keys = [0]

    for key in boxes_keys:
        for new_key in boxes[key]:
            if new_key < len(boxes) and new_key not in boxes_keys:
                boxes_keys.append(new_key)

    return len(boxes_keys) == len(boxes)
