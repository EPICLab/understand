# Sample Understand Python API program
#
# Synopsis: Outputs a text callbytree for selected functions
#
# Categories: Graphic, Project Report, Entity Report
#
#Languages: Ada, Fortran, C
#
# Written by Jason Quinn
#
# 1/21/21

import understand
import sys
import re
import argparse
import os

# Usage:
parser = argparse.ArgumentParser()
parser.add_argument("db", help="Specify Understand database")
parser.add_argument("-txt", help="""(optional) if txt is specified, each \
        separate tree will be printed to a .txt file. Please insert \
        desired path or '.' (for the current directory) for text files. \
        EX. /example/example1/""")
parser.add_argument("-maxlevel", help="""(optional) only print the first level depths\
        of calls. (0 equals no limit)""")
args = parser.parse_args()

def callbyTree(func, depth):
        
    # Checks if depth has passed maxlevel
    if maxLevel != 0 and depth > int(maxLevel):
        return

    # Prints or writes a '| ' for every level deep the call is
    depthString = ('| ' * depth) + func.longname()
    if txt:
        txtFile.write(depthString + '\n')
    else:
        print(depthString)

    # Returns after printing if the function has already been seen
    if func.uniquename() in seen.keys():
        return

    else:
        # Marks function as seen then gathers the call references
        seen[func.uniquename()] = True
        callbys = func.refs("callby ~inactive, use ptr ~inactive", "function ~unknown ~unresolved, c object ~unknown ~unresolved", True)

        # Iterates through all calls and increases the depth by one
        for callby in callbys:
            callbyTree(callby.ent(), depth + 1)
    

if __name__ == '__main__':
    # Open Database
    db = understand.open(args.db)

    # Checks and sets maxlevel
    if args.maxlevel:
        maxLevel = args.maxlevel
    else:
        maxLevel = 0

    path = ''
    if args.txt:
        txt = True

        path = args.txt
        if path == '.' or path == '/.' or path == '/./' or path == './':
            path = ''
    else:
        txt = False

    funcs = db.ents("function ~unresolved ~unknown, procedure ~unresolved ~unknown, subroutine ~unresolved ~unknown")
    count = 0
    
    # Iterate through all functions
    for func in funcs:
        seen = {}

        # Call the callTree function for all root functions
        callbys = func.refs("callby ~inactive, use ptr ~inactive")
        if callbys:
            funcString = f'{path}{func.longname()}_callbytree.txt'

            # Create directory if given path does not exist
            if txt:
                if path != '':
                    os.makedirs(os.path.dirname(funcString), exist_ok=True)
                txtFile = open(funcString, "a")
            callbyTree(func, 0)

            # Close text file
            if txt:
                txtFile.close()
