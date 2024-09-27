# date-regex.py: A regular expressions example to find dates in a text file.
#
# This file is from the pre-2023 Hunter CSEd teaching team.
# Updated and augmented for CS778 - Fall 2024.
import re


def find_date(line):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
		# in Python: the r prefix in Python for a raw string.
		#	  here the \d does not convert "d" into an escaped character.
		# in Regex: \d matches a digit, {} specifies a range of repetition.
		# 	this matches 1 or 2 digits, a slash, and so on.
    result = re.findall(pattern,line)

    pattern=r'(October|Oct|November|Nov)( [0-9]{1,2}, [0-9]{4})'
		# ( ) specifies targets to pull out of a line.
		# here we a targetting a month and separately the day/year.
		#
		# Why does this not pick up the last line?
    result = result + re.findall(pattern,line)
    return result


f = open("notedates.dat")
for line in f.readlines():
    #print(line)
    result = find_date(line)
    if (len(result)>0):
        print(result)
