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

def is_safe(report):
    if are_all_increasing(report) or are_all_decreasing(report):
        if adjacent_difference_ok(report):
            return True
    return False

def determine_safe(reports):
    number_safe = 0
    unsafe_reports = list()
    for report in reports:
        if is_safe(report):
            number_safe += 1
        else:
            unsafe_reports.append(report)
    return number_safe, unsafe_reports

def problem_dampener(unsafe_reports):
    number_dampened = 0
    for report in unsafe_reports:
        for index in range(len(report)):
            report_dampened = report[:index] + report[(index+1):]
            if is_safe(report_dampened):
                number_dampened += 1
                break
    return number_dampened

with open(sys.argv[1], "r") as f:
    data = f.read().splitlines()

reports = get_reports_from_data(data)
number_of_safe_reports, unsafe_reports = determine_safe(reports)
print("Part 1: %d" % number_of_safe_reports)
number_dampened = problem_dampener(unsafe_reports)
print("Part 2: %d" % (number_of_safe_reports + number_dampened))