# api-Search_NASA_photo.py: Displays a NASA photo/video by searching the NASA API.
#
# Modified from: 
# CSCI 77800 -- 2024 FA (updated) -- Edgar E. Troudt, Ph.D.
#
# B.Cornish Sep 2024


# Required Libraries
import json		# pip install json5
			#	JSON is a standard data transmission format for APIs.

import urllib		# pip install urllib3
			#	urllib reads from a particular web address.

import imutils		# pip install imutils
			#	grabs the image data and converts to a usable image.

import cv2		# pip install opencv-python
			#	allows for the graphical display of the image.


# use the NASA API database
#url = "https://api.nasa.gov/planetary/apod?api_key=Xztecw5EiPHCXhWTdft9YpHd0p49nl4WaAdwpAhc" # photo of the day
url = "https://images-api.nasa.gov/search?q=apollo%2011&description=moon%20landing&media_type=image&location=National%20Mall&keywords=engine" #?api_key=Xztecw5EiPHCXhWTdft9YpHd0p49nl4WaAdwpAhc"

response = urllib.request.urlopen(url)
data_json = json.loads(response.read())

print("-------------")
print("Using API key: Xztecw5EiPHCXhWTdft9YpHd0p49nl4WaAdwpAhc")

# print the raw JSON data just for display purposes
print("-------------")
print("Raw JSON data from NASA:")
print(data_json)
print("")


# The NASA Photo of the day URL
print("\n\n-------------")
print("Address of the FIRST Photo in search:")
image_url=data_json['collection']['items'][0]['links'][0]['href']
print(image_url)

# Download an image from the NASA website URL
img = imutils.url_to_image(image_url)
# Display the image and pause for ESC.
cv2.imshow(data_json['collection']['items'][0]['data'][0]['title'] + ' ' + data_json['collection']['items'][0]['data'][0]['date_created'], img)
cv2.waitKey(0)

'''
# To pull original image (full resolution) from NASA
nasa_ID = data_json['collection']['items'][0]['data'][0]['nasa_id'] # Get the NASA ID from the JSON data
print("\n\n-------------")
print("NASA ID: " + nasa_ID)
manifest_URL = "https://images-api.nasa.gov/asset/" + nasa_ID 
manifest_response = urllib.request.urlopen(manifest_URL) # Get the manifest data
manifest_data_json = json.loads(manifest_response.read()) # Load the manifest data into a JSON object
original_image_url = manifest_data_json['collection']['items'][0]['href']	# Get the original image URL
#print(manifest_data_json['collection']['items'][0])

# Download an image from the NASA website URL
img2 = imutils.url_to_image(original_image_url)
# Display the image and pause for ESC.
cv2.imshow(data_json['collection']['items'][0]['data'][0]['title'] + ' ' + data_json['collection']['items'][0]['data'][0]['date_created'], img2)
cv2.waitKey(0)
'''

cv2.destroyAllWindows()
