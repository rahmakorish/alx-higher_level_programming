#!/usr/bin/python3
"""advanced tasks"""


def append_after(filename="", search_string="", new_string=""):
    """function"""
    with open(filename, "r", encoding='utf-8') as filex:
        line = []
        while 1:
            linex = filex.readline()
            if linex == "":
                break
            line.append(linex)
            if search_string in linex:
                line.append(new_string)
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(line)
