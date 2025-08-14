#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    canUnlockAll add boxes
    """
    n = len(boxes)
    unlocked_boxes = {0}
    keys_to_check = list(boxes[0])

    while keys_to_check:
        key = keys_to_check.pop(0)

        if 0 <= key < n and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys_to_check.extend(boxes[key])

    return len(unlocked_boxes) == n
