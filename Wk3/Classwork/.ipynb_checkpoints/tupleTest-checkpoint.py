# CSCI 77800 -- 2024 FA -- E. Troudt
# tupleTest.py: How are tuples useful?
#
# Examples inspired by Reddit question and answers:
# https://www.reddit.com/r/learnpython/comments/zuzdvr/what_are_some_use_cases_for_tuples_in_python/

import sys

def func1 ( x, y ):
	return x+1, y+1

tup_x = func1( 5, 6 )
tup_y = (7,8)

print ( "tup_x = ", end="" )
print ( tup_x )

print ( "tup_x[0] = ", end="" )
print ( tup_x[0] )
print ()

# tup_x[0] += 1		# what happens here?


# can be used as a dictionary key, source:
dict_z = { tup_x:"cat", tup_y:"dog" }

print ( "dict_z[tup_x] = ", end="" )
print ( dict_z[tup_x] )

print ( "dict_z[(7,8)] = ", end="" )
print ( dict_z[(7,8)] )
print ()


# Also memory efficiency.
print ( "Tuple byte size: ", end="" )
print ( sys.getsizeof( (0,1,2) ) ) # tuple

print ( "List byte size: ", end="" )
print ( sys.getsizeof( [0,1,2] ) ) # list
