# api-nasaphoto.py: Displays the NASA photo of the day by querying the NASA API.
#
# CSCI 77800 -- 2024 FA (updated) -- Edgar E. Troudt, Ph.D.

import json		# pip install json5
			#	JSON is a standard data transmission format for APIs.

import urllib		# pip install urllib3
			#	urllib reads from a particular web address.

import imutils		# pip install imutils
			#	grabs the image data and converts to a usable image.

import cv2		# pip install opencv-python
			#	allows for the graphical display of the image.


# use the NASA API database
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
	# you should get your own key -- the demo key has limited number of uses.
response = urllib.request.urlopen(url)
data_json = json.loads(response.read())

# print the raw JSON data just for display purposes
print("-------------")
print("Raw JSON data from NASA:")
print(data_json)
print("")

# The NASA Photo of the day URL
print("\n\n-------------")
print("Address of the NASA Photo of the day:")
print(data_json['url'])

# Download an image from the NASA website URL
img = imutils.url_to_image(data_json['url'])

# Display the image and pause for ESC.
cv2.imshow(data_json['title'] + ' ' + data_json['date'], img)
cv2.waitKey(0)
