# CSCI 778 - 2024 FA - E. Troudt
# drr.py: Deficit Round Robin
# Portions based on Wikipedia pseudocode: https://en.wikipedia.org/wiki/Deficit_round_robin
#
# the collections library is helpful, in particular the deque
# https://docs.python.org/3/library/collections.html#collections.deque

import collections as dq
import Packet as p

Q_COUNT = 3
q1 = dq.deque()
q2 = dq.deque()
q3 = dq.deque()

queues   = [ q1, q2, q3 ]
weight   = [  5,  2,  3 ] # list, Python doesn't have "arrays".
deficit  = [  0,  0,  0 ]

# Fill queues.
# queue 1
q1.append( p.Packet("A",1,1) )
q1.append( p.Packet("B",1,1) )
q1.append( p.Packet("C",1,1) )
q1.append( p.Packet("D",1,1) )
q1.append( p.Packet("E",1,3) )

# queue 2
q2.append( p.Packet("U",1,3) )
q2.append( p.Packet("V",1,3) )
q2.append( p.Packet("W",1,1) )

# queue 3
q3.append( p.Packet("X",1,2) )
q3.append( p.Packet("Y",1,3) )
q3.append( p.Packet("Z",1,1) )



# the algorithm calls for an infinite loop, but for the demo we should
# stop after all of the elements have been exhausted.
elements = len( q1 ) + len( q2 ) + len( q3 )

# this code is based on the pseudocode from Wikipedia
#       https://en.wikipedia.org/wiki/Deficit_round_robin
maximum = max( weight[0], weight[1], weight[2] )

while elements > 0 :
	for queue_select in range ( 0, Q_COUNT ) :
		if len( queues[queue_select] ) > 0 :	# is empty?
			deficit[queue_select] += weight[queue_select]
			while ( (len( queues[queue_select] ) > 0)  # not empty
				and queues[queue_select][0].len < deficit[queue_select] ) :

				deficit[queue_select] -= queues[queue_select][0].len
				print( f"Sending { queues[queue_select][0] } with name", end="" )
				print( f" { queues[queue_select][0].name } from queue {queue_select}." )
				queues[queue_select].popleft()	# removes it.
				elements -= 1
			if len( queues[queue_select] ) <= 0 : 	# is empty
				deficit[queue_select] = 0
