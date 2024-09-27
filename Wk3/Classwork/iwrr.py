# CSCI 778 - 2024 FA - E. Troudt
# iwrr.py: the Interleaved Weighted Round Robin
# Portions based on Wikipedia pseudocode: https://en.wikipedia.org/wiki/Weighted_round_robin
#
# the collections library is helpful, in particular the deque
# https://docs.python.org/3/library/collections.html#collections.deque

import collections as dq
import Packet as p

Q_COUNT = 3
q1 = dq.deque()
q2 = dq.deque()
q3 = dq.deque()

queues = [ q1, q2, q3 ]
weight = [  5,  2,  3 ] # list, Python doesn't have "arrays".

# Fill queues.
for x in range( ord('A'), ord('G')+1 ): # queue 1
        pkt = p.Packet( chr(x), 1, 1 )          # need to use chr, if you use str you get "65".
        q1.append( pkt )

for x in range( ord('U'), ord('W')+1 ): # queue 2
        pkt = p.Packet( chr(x), 1, 1 )          # need to use +1 in control because < not <=.
        q2.append( pkt )

for x in range( ord('X'), ord('Y')+1 ): # queue 3
        pkt = p.Packet( chr(x), 1, 1 )
        q3.append( pkt )


# the algorithm calls for an infinite loop, but for the demo we should
# stop after all of the elements have been exhausted.
elements = len( q1 ) + len( q2 ) + len( q3 )

# this code is based on the pseudocode from Wikipedia
#       https://en.wikipedia.org/wiki/Weighted_round_robin
maximum = max( weight[0], weight[1], weight[2] )

while elements > 0 :
	for curr_wght in range ( 0, maximum ) :
		for i in range ( 0, Q_COUNT ) :
			if( len( queues[i] ) > 0 ) and ( weight[i] > curr_wght ) :
				print( f"Sending { queues[i][0] } with name { queues[i][0].name } from queue {i}." )
				queues[i].popleft()	# removes it.
				elements -= 1
