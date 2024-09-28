# simpleFood.py: Illustrating how to use a JSON string.
#
# CSCI 77800 -- 2024 FA -- Edgar E. Troudt, Ph.D.

# Docs for JSON library: https://docs.python.org/3/library/json.html
import json


# the JSON code was taken directly from:
# 	https://foodish-api.com/api/images/burger
x = json.loads( '{"image":"https://foodish-api.com/images/burger/burger40.jpg"}' )
print ( x );
print ( x['image'] );
