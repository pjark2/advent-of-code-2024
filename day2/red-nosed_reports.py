#!/usr/bin/env python

import sys, re

def adjacent_difference_ok(report):
    for index in range(len(report)-1):
        current_level = report[index]
        next_level = report[index + 1]
        difference = abs(next_level - current_level)
        if difference not in [1, 2, 3]:
            return False
    return True

def are_all_decreasing(report):
    for index in range(len(report)-1):
        current_level = report[index]
        next_level = report[index + 1]
        if next_level >= current_level:
            return False
    return True

def are_all_increasing(report):
    for index in range(len(report)-1):
        current_level = report[index]
        next_level = report[index + 1]
        if next_level <= current_level:
            return False
    return True

def get_reports_from_data(data):
    reports = list()
    for line in data:
        numbers_found = re.findall(r'\d+', line)
        numbers = [int(number_string) for number_string in numbers_found]
        reports.append(numbers)
    return reports

def determine_safe(reports):
    number_safe = 0
    for report in reports:
        if are_all_increasing(report) or are_all_decreasing(report):
            if adjacent_difference_ok(report):
                number_safe += 1
    return number_safe

with open(sys.argv[1], "r") as f:
    data = f.read().splitlines()

reports = get_reports_from_data(data)
number_of_safe_reports = determine_safe(reports)
print("Part 1: %d" % number_of_safe_reports)