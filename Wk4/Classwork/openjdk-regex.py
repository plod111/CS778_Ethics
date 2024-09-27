# openjdk-regex.py: Lists the versions of openjdk available from apt.
#
# 2024 FA - E. Troudt - CSCI 77800

#import os;
import subprocess;
import re

# just runs and prints to console; not useful here
# output = os.system( "apt list" )

# this output can be captured.
x = subprocess.check_output(['apt', 'list'])
x = str( x )
y = re.findall( r"openjdk-\d{2}", x )

print( y )
