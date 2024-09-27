# CSCI 778 - 2024 FA - E. Troudt
# cwrr.py: the Classic Weighted Round Robin Algorithm
# Portions based on Wikipedia pseudocode: https://en.wikipedia.org/wiki/Weighted_round_robin
#
# the collections library is helpful, in particular the deque
# 	https://docs.python.org/3/library/collections.html#collections.deque
#	deque - "deck" - can act as a stack or a queue.
#
# not using the built-in queue class because of lack of "peek" functionality
# 	https://docs.python.org/3/library/queue.html

import collections as dq
import Packet as p

Q_COUNT = 3
q1 = dq.deque()
q2 = dq.deque()
q3 = dq.deque()

queues = [ q1, q2, q3 ]
weight = [  5,  2,  3 ] # list, Python doesn't have "arrays".

print ( "-----Initialized-----" )
print ( "Queue 1 initialized with " + str( len( q1 ) ) + " elements.\n", end="" )
print ( "Queue 2 initialized with " + str( len( q2 ) ) + " elements.\n", end="" )
print ( "Queue 3 initialized with " + str( len( q3 ) ) + " elements.\n", end="" )
	# reminding you that you can format strings different ways

# Fill queues
for x in range( ord('A'), ord('G')+1 ):	# queue 1
	pkt = p.Packet( chr(x), 1, 1 )		# need to use chr, if you use str you get "65".
	q1.append( pkt )

for x in range( ord('U'), ord('W')+1 ):	# queue 2
	pkt = p.Packet( chr(x), 1, 1 )		# need to use +1 in control because < not <=.
	q2.append( pkt )

for x in range( ord('X'), ord('Y')+1 ):	# queue 3
	pkt = p.Packet( chr(x), 1, 1 )
	q3.append( pkt )

print ( "\n\n-----Filled-----" )
print ( f"Queue 1 established with { len( q1 ) } elements.")
print ( f"Queue 2 established with { len( q2 ) } elements.")
print ( f"Queue 3 established with { len( q3 ) } elements.")
	# using the f-string construct


# for testing purposes
print ( "\n\n-----First two elements, first queue-----" )
print ( q1[0] )		# peek
print ( q1[0].name )
print ( q1[1] )		# peek
print ( q1[1].name )
#q1.popleft()		# deque is either stack or queue
#			# adds to the right, so for queue need to pop left.
#			# for stack, simply pop.
#print ( len ( q1 ) )
#print ( q1[0] )	# peek
#print ( q1[0].name )
print ( "\n\n" )


# the algorithm calls for an infinite loop, but for the demo we should
# stop after all of the elements have been exhausted.
elements = len( q1 ) + len( q2 ) + len( q3 )

# this code is based on the pseudocode from Wikipedia
# 	https://en.wikipedia.org/wiki/Weighted_round_robin
while elements > 0 :
	# visit each queue
	for i in range ( 0, Q_COUNT ) :
		count = 0
		# remove appropriate amount in each queue
		while ( len( queues[i] ) > 0 ) and ( count < weight[i] ) :
			print( f"Sending { queues[i][0] } with name { queues[i][0].name } from queue {i}." )
			queues[i].popleft()	# removes it.
			count    += 1
			elements -= 1
