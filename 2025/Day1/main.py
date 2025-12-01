from pathlib import Path
import os

filepath = Path('.')
filename = 'input.txt'

with open(os.path.join(filepath, filename)) as f:
    lines = [line.strip() for line in f.readlines()]


def point_dial(current, next_operation, method, min_threshold=0, max_threshold=99):
    if next_operation[0] == 'R':
        current += int(next_operation[1:])
    else:
        current -= int(next_operation[1:])
    if method == 'p2':
        return current
    if current > max_threshold:
        i = int(abs(current)/100)
        current = current - (i*100)
    if current < min_threshold:
        i = max(1, int(abs(current)/100))
        current = (i*100)-abs(current)
    return current


def get_zero_pass(old, next_operation):
    # old = current
    current = point_dial(old, next_operation, method='p2')
    lst = list(range(min(current, old), max(current, old)+1))
    my_max_val = int(max([abs(i) for i in lst])/100)
    if old != 0:
        my_max_val += lst.count(0)
    my_min_val = int(min([abs(i) for i in lst])/100)
    val = my_max_val-my_min_val
    return val


def get_door_password(lines, method, start_pos=50):
    psw = 0
    current_pos = start_pos
    for line in lines:
        old_pos = current_pos
        current_pos = point_dial(current_pos, line, method='p1')
        if method == 'p1':
            if current_pos == 0:
                psw += 1
        elif method == 'p2':
            psw += get_zero_pass(old_pos, line)
    return psw


print('Open door p1 password: ', get_door_password(lines, method='p1'))
print('Open door p2 password: ', get_door_password(lines, method='p2'))
