# simpleFood2.py: Illustrating how to use a JSON string that is loaded dynamically from the web.
#			This also extracts elements from that JSON string.
#
# CSCI 77800 -- 2024 FA -- Edgar E. Troudt, Ph.D.


# Docs for JSON library: https://docs.python.org/3/library/json.html
import json

# Docs for URLLIB library: https://docs.python.org/3/library/urllib.html
import urllib.request

# connect to the website
web_data = urllib.request.urlopen( url="https://foodish-api.com/api/images/burger" )

# What happens if we do this instead?
# web_data = urllib.request.urlopen( url="https://foodish-api.com/api/images/nothing" )

# for illustration purposes -- what did we get back?
print ( f"Printing web_data        = {web_data}" )
print ( f"Printing web_data.msg    = {web_data.msg}" )
json_data = web_data.read()
print ( f"Printing web_data.read() = {json_data}" )

print ("\n\n----------\n\n")

# now that we have the JSON, process it
json_string = json.loads( json_data )
print ( f"Printing the json_string                = {json_string}" );
print ( f"Printing the keys of json_string        = {json_string.keys()}" );
print ( f"Printing the json_string['image'] field = {json_string['image']}" );
