# CSCI 778 - 2024 FA - E. Troudt
# PacketTest.py: demonstrates that our Packet object works.
#		 shows object file loading and usage.

import Packet as p

pack1 = p.Packet( "A", 4, 1 )
pack2 = p.Packet( name="B", time=4, len=1 )
pack3 = p.Packet( time=4, name="C", len=1 )
print( pack1.name )
print( pack2.name )
print( pack3.name )


# Remember that in Java we didn't know the names of the
# function parameters.  It didn't matter to the program.
# Here we can pass arguments out of order using the parameter
# name.
