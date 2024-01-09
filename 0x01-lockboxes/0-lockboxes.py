#!/usr/bin/python3
"""
Determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Args:
        boxes: a list of lists

    Returns:
        True if all boxes can be opened, False otherwise
    """
    if not boxes or len(boxes) == 0:
        return False

    keys = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in keys and 0 <= key < len(boxes):
                keys.add(key)
                stack.append(key)

    return len(keys) == len(boxes)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False

