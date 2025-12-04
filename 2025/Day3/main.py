from pathlib import Path
import os

filepath = Path('.')
filename = 'input.txt'

with open(os.path.join(filepath, filename)) as f:
    lines = [line.strip() for line in f.readlines()]


def run_p1(bank):
    battery = max(bank[:-1])
    battery_pos = bank[:-1].index(battery)
    return int(str(battery)+str(max(bank_list[battery_pos+1:])))


def run_p2(bank):
    val = []
    battery_pos = 0
    while len(val) != 12:
        i = len(bank)-(12-len(val))+1
        battery = max(bank[:i])
        battery_pos = bank[:i].index(battery)
        bank = bank[battery_pos+1:]
        val.append(str(battery))
    return int(''.join(val))


jolts_p1 = []
jolts_p2 = []
for line in lines:
    bank_list = [int(i) for i in line]
    jolts_p1.append(run_p1(bank_list))
    jolts_p2.append(run_p2(bank_list))
print('Total output joltage two batteries: ', sum(jolts_p1))
print('Total output joltage twelve batteries: ', sum(jolts_p2))
