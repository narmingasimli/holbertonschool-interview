#!/usr/bin/python3
"""Prototype: def canUnlockAll(boxes)"""


def canUnlockAll(boxes):
    """Return code"""
    length = len(boxes)
    for i in range(1, length):
        flag = 0
        for j in range(length):
            if i in boxes[j] and i != j:
                flag = 1
        if flag == 0:
            return False
    return True
