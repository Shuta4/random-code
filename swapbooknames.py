#!/usr/bin/python3

"""
Renames all files in directory and its subdirectories
swapping name parts separated by last ' - '.
Usage: program.py dirname
"""

import sys
import os

def swapname(name):
    if ' - ' not in name:
        return name
    nameparts = name.split(' - ')
    first = nameparts[-1]
    last = ' - '.join(nameparts[:len(nameparts) - 1])
    return ' - '.join([first, last])

def main():
    if len(sys.argv) < 2:
        raise Exception("Directory name is missing.")
    dirname = sys.argv[1]
    if not os.path.isdir(dirname):
        raise Exception(f"'{dirname}' is not a directory")

    for dirpath, dirnames, filenames in os.walk(dirname):
        for name in filenames:
            oname, ext = os.path.splitext(name)
            nname = swapname(oname)
            opath = os.path.join(dirpath, name)
            npath = os.path.join(dirpath, f"{nname}{ext}")
            if opath == npath:
                print(f"Skipping '{opath}'")
                continue

            print(f"'{opath}' -> '{npath}'")
            os.rename(opath, npath)


if __name__ == "__main__":
    main()
