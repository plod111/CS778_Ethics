# DynamicTyping.py: We don't need to declare any types!  (But these do still exist.)
#
# CSCI 77800 - 2024 FA - Edgar Troudt
#
# What do you notice about the comment style?

i = input( "First: "  )
j = input( "Second: " )

print( i + j )
input ( "--pause for dramatic effect--pt2--" )

print (type(i))

input ( "--pause for dramatic effect--pt3--" )
i = int(i) * 4  # conversion line - version A
#i = i * 4  # conversion line - version B

input ( "--pause for dramatic effect--pt4--" )
print (i)
print (type(i))

# What happens if you type a word into the first slot?
# What happens if I eliminate the int() function from the conversion line?  (Switch from version A to version B.)