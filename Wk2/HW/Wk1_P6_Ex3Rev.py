""" Wk1 P6 Ex 3 Revision for command line
    BCornish, Sept 2024
"""

import sys

if len(sys.argv) > 1:
    print("Script name:", sys.argv[0])
    print("Arguments:", sys.argv[1:])
    arg1 = int(sys.argv[1])
    if type(arg1) == int:
        print(f"Number Immediately Prior = {arg1-1}")
        print(f"Number Immediately After = {arg1+1}")
    else:
        print("Not a number")
else:
    print("No argument provided.")
