#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    else:
        for x, y in sorted(a_dictionary.items()):
            print(f"{x}: {y}")
