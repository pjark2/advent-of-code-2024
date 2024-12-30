#!/usr/bin/env python

import sys

def get_data(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    return data

def get_range(data):
    return [len(data), len(data[0])]

def word_is_valid(coords_list, data):
    data_range = get_range(data)
    for coord in coords_list:
        if coord[0] not in range(data_range[0]) or coord[1] not in range(data_range[1]):
            return False
    return True

def find_matches(coord, data):
    matches_from_word = 0
    x,y = coord
    north = [[x,y], [x-1,y], [x-2,y], [x-3,y]]
    east = [[x,y], [x,y+1], [x,y+2], [x,y+3]]
    south = [[x,y], [x+1,y], [x+2,y], [x+3,y]]
    west = [[x,y], [x,y-1], [x,y-2], [x,y-3]]
    northeast = [[x,y], [x-1,y+1], [x-2,y+2], [x-3,y+3]]
    southeast = [[x,y], [x+1,y-1], [x+2,y-2], [x+3,y-3]]
    southwest = [[x,y], [x+1,y+1], [x+2,y+2], [x+3,y+3]]
    northwest = [[x,y], [x-1,y-1], [x-2,y-2], [x-3,y-3]]
    word_coord_lists = [north, east, south, west, northeast, southeast, southwest, northwest]
    for word_coords in word_coord_lists:
        if word_is_valid(word_coords, data):
            word = ""
            for word_coord in word_coords:
                word += data[word_coord[0]][word_coord[1]]
            if word == "XMAS":
                matches_from_word += 1
    return matches_from_word

def calculate_all_matches(data):
    total_matches = 0
    for line_index, line in enumerate(data):
        for char_index, char in enumerate(line):
            total_matches += find_matches([line_index, char_index], data)
    return total_matches

def search_around_coord(coord, data):
    x,y = coord
    ne_letter = [[x-1,y+1]]
    se_letter = [[x+1,y+1]]
    sw_letter = [[x+1,y-1]]
    nw_letter = [[x-1,y-1]]
    letters_to_check = [ne_letter, se_letter, sw_letter, nw_letter]
    letters_found = ["", "", "", ""]
    ms_found = 0
    ss_found = 0
    for letter_index, letter_coord in enumerate(letters_to_check):
        if word_is_valid(letter_coord, data):
            char_found = data[letter_coord[0][0]][letter_coord[0][1]]
            if char_found == "M":
                ms_found += 1
            elif char_found == "S":
                ss_found += 1
            letters_found[letter_index] = char_found
    
    if ms_found == 2 and ss_found == 2:
        if letters_found[0] != letters_found[2] and letters_found[1] != letters_found[3]:
            return 1
    return 0

def find_all_xmas2(data):
    total_matches = 0
    for line_index, line in enumerate(data):
        for char_index, char in enumerate(line):
            if char == "A":
                total_matches += search_around_coord([line_index, char_index], data)
    return total_matches

data = get_data(sys.argv[1])
total_matches = calculate_all_matches(data)
print("Part 1: %d" % total_matches)
total_matches2 = find_all_xmas2(data)
print("Part 2: %d" % total_matches2)
