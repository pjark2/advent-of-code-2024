#!/usr/bin/env python
import sys

def get_data(filename):
    with open(filename, "r") as file:
        rules = list()
        updates = list()
        READ_RULES = True
        for line in file:
            if line == "\n":
                READ_RULES = False
            else:
                if READ_RULES:
                    rules.append(line.rstrip())
                else:
                    updates.append(line.rstrip())
    data = [rules, updates]
    return data

def print_dict(dict):
    for key in dict:
        print("%s -> %s" % (key, dict[key]))

def consolidate_rules(og_rules):
    rules_dict = dict()
    for rule in og_rules:
        rule_nums = rule.split("|")
        num_first, num_second = rule_nums
        if num_first not in rules_dict.keys():
            rules_dict[num_first] = [num_second]
        else:
            rules_dict[num_first].append(num_second)
    return rules_dict

def parse_updates(og_updates):
    """
    str(1,2,3,4) -> [1, 2, 3, 4]
    """
    fixed_updates = list()
    for og_update in og_updates:
        fixed_updates.append([num for num in og_update.split(",")])
    return fixed_updates

def test_single_update(rules_dict, test_update):
    for index, num in enumerate(test_update):
        nums_after = test_update[index:]
        for num_after in nums_after:
            if num_after in rules_dict.keys() and num in rules_dict[num_after]:
                return False
    return True

def find_valid_updates(rules_dict, updates):
    valid_updates = list()
    for update in updates:
        if test_single_update(rules_dict, update):
            valid_updates.append(update)
    return valid_updates

def find_medians(valid_updates):
    medians = list()
    for valid_update in valid_updates:
        med_index = int(len(valid_update) / 2)
        medians.append(int(valid_update[med_index]))
    return medians

rules, updates = get_data(sys.argv[1])
rules_dict = consolidate_rules(rules)
fixed_updates = parse_updates(updates)
valid_updates = find_valid_updates(rules_dict, fixed_updates)
medians = find_medians(valid_updates)
print("Part 1: %d" % (sum(medians)))