#!/usr/bin/env python

import sys
import re

def get_numbers_from_line(line):
    numbers_strings = re.findall(r"\d+", line)
    numbers = [int(number) for number in numbers_strings]
    return numbers

def create_lists(data):
    left = list()
    right = list()
    for line in data:
        numbers = get_numbers_from_line(line)
        left.append(numbers[0])
        right.append(numbers[1])
    return left, right

### quicksort taken from g4g
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def find_distances(left, right):
    assert(len(left) == len(right))
    distances = list()
    for index in range(len(left)):
        distances.append(abs(left[index] - right[index]))
    return distances

def count_occurences(left, right):
    counted_occurences = list()
    for number in left:
        occurences = 0
        for other_number in right:
            if number == other_number: 
                occurences += 1
        counted_occurences.append(occurences)
    return counted_occurences

def calculate_simularity_score(left, occurences):
    simularity_score = 0
    for index in range(len(left)):
        simularity_score += left[index] * occurences[index]
    return simularity_score

with open(sys.argv[1], "r") as f:
    data = [line.strip() for line in f.readlines()]

left, right = create_lists(data)
left = quicksort(left)
right = quicksort(right)
distances = find_distances(left, right)
print("Part 1: %d" % sum(distances))

occurences = count_occurences(left, right)
simularity_score = calculate_simularity_score(left, occurences)
print("Part 2: %d" % simularity_score)