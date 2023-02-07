"""
CS 211 Mini Project - Where's Waldo?
Author: Brian Gilmore
"""

Waldo = 'W'
Other = '.'

def all_row_exists_waldo(l):
    for row in l:
        if Waldo not in row:
            return False
    return True

def all_col_exists_waldo(l):
    if len(l) == 0 or len(l[0]) == 0:
        return True
    col_index = []
    for row in range(len(l)):
        for index, col in enumerate(l[row]):
            if Waldo not in col:
                continue
            else:
                col_index.append(index)
    sorted_indices = len(set(col_index))
    return len(l) == sorted_indices

def all_row_all_waldo(l):
    if len(l) == 0 or len(l[0]) == 0:
        return True
    for row in l:
        for col in row:
            if Waldo not in col:
                return False
    return True


def all_col_all_waldo(l):
    if len(l) == 0 or len(l[0]) == 0:
        return True
    for row in range(len(l)):
        for col in range(len(l[row])):
            if Waldo not in l[row][col]:
                return False
    return True

def exists_row_all_waldo(l):
    for r in l:
        if all(elem == Waldo for elem in r):
            return True
    return False

def exists_col_all_waldo(l):
    if len(l) == 0 or len(l[0]) == 0:
        return False
    for col in range(len(l[0])):
        count = 0
        for row in l:
            if row[col] == Waldo:
                count += 1
                if count == len(l):
                    return True
                else:
                    continue
    return False

def exists_row_exists_waldo(l):
    for row in l:
        if any(i == Waldo for i in row):
            return True
    return False

def exists_col_exists_waldo(l):
    if len(l) == 0 or len(l[0]) == 0:
        return False
    for col in range(len(l[0])):
        count = 0
        for row in l:
            if row[col] == Waldo:
                count += 1
                if count >= 1:
                    return True
                else:
                    continue
    return False



