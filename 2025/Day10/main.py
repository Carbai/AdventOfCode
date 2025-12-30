from pathlib import Path
import re

from collections import deque
import pulp

with Path('input10.txt').open() as f:
    lines=f.read().splitlines()

def parse_machine(line):
    parts = line.split()

    # indicator target
    diagram = parts[0][1:-1]
    target = 0
    for i, c in enumerate(diagram):
        if c == '#':
            target |= 1 << i

    # buttons
    buttons = []
    for p in parts[1:]:
        if p.startswith('{'):
            break
        indices = map(int, p[1:-1].split(','))
        mask = 0
        for i in indices:
            mask |= 1 << i
        buttons.append(mask)

    return target, buttons

def min_presses(buttons, target):
    q = deque([(0, 0, 0)])  # (xor, used_mask, presses)
    seen = set([(0, 0)])

    while q:
        cur, used, cnt = q.popleft()
        if cur == target:
            return cnt

        for i, b in enumerate(buttons):
            if used & (1 << i):
                continue
            nxt = cur ^ b
            nxt_used = used | (1 << i)
            if (nxt, nxt_used) not in seen:
                seen.add((nxt, nxt_used))
                q.append((nxt, nxt_used, cnt + 1))

    return 0

total = 0
for line in lines:
    target, buttons = parse_machine(line)
    total += min_presses(buttons, target)

print('Solution to part one:', total)  #517



def min_presses_joltage_solver(buttons, target):
    m = len(buttons)
    n = len(target)

    # Define problem
    prob = pulp.LpProblem("JoltageConfig", pulp.LpMinimize)

    # Variables: number of presses per button
    x = [
        pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer")
        for j in range(m)
    ]

    # Objective: minimize total presses
    prob += pulp.lpSum(x)

    # Constraints: match each counter exactly
    for i in range(n):
        prob += pulp.lpSum(
            x[j] for j in range(m) if i in buttons[j]
        ) == target[i]

    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    return int(pulp.value(prob.objective))


def read_machines(lines):
    machines = []

    for line in lines:
        # find all button definitions
        button_parts = re.findall(r'\((.*?)\)', line)
        buttons = []
        for b in button_parts:
            if b.strip() == "":
                buttons.append([])
            else:
                buttons.append(list(map(int, b.split(','))))

        # find target joltage requirements
        target_part = re.search(r'\{(.*?)\}', line).group(1)
        target = list(map(int, target_part.split(',')))

        machines.append((buttons, target))

    return machines
machines = read_machines(lines)
total = 0
for buttons, target in machines:
    total += min_presses_joltage_solver(buttons, target)

print('Solution to part two:', total)  

