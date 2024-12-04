#!/usr/bin/env python

import sys, re

def find_muls(data):
    muls = list()
    for line in data:
        muls_strings = re.findall(r'mul\(\d+,\d+\)', line)
        for muls_string in muls_strings:
            num_string = re.findall(r'\d+', muls_string)
            muls.append([int(num_string[0]), int(num_string[1])])
    return muls

def calculate_results(muls):
    total = 0
    for mul in muls:
        total += mul[0] * mul[1]
    return total

def extract_instructions(data):
    instructions = list()
    for line in data:
        ins_strings = re.findall(r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)", line)
        for ins_string in ins_strings:
            if ins_string in ["do()", "don't()"]:
                instructions.append(ins_string)
            else:
                num_string = re.findall(r'\d+', ins_string)
                instructions.append([int(num_string[0]), int(num_string[1])])
    return instructions

def do_instructions(instructions):
    total = 0
    doing = True
    for instruction in instructions:
        if doing and instruction not in ["do()", "don't()"]:
            total += instruction[0] * instruction[1]
        elif instruction == "do()":
            doing = True
        elif instruction == "don't()":
            doing = False
    return total

with open(sys.argv[1], "r") as f:
    data = f.read().splitlines()

muls = find_muls(data)
total = calculate_results(muls)
print("Part 1: %d" % total)

instructions = extract_instructions(data)
total2 = do_instructions(instructions)
print("Part 2: %d" % total2)