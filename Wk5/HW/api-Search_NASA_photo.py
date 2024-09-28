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

print("\n-------------")
print("NASA Image ONLY Search")
print("Enter the (limited) search terms for the NASA image database.")
print("\n-------------")


# use the NASA API image database
url = "https://images-api.nasa.gov/search?&media_type=image" #q=apollo%2011&description=moon%20landing&media_type=image&location=National%20Mall&keywords=engine" #?api_key=Xztecw5EiPHCXhWTdft9YpHd0p49nl4WaAdwpAhc"

#text_search = input("Enter the FREE-TEXT search term(s) for the NASA image database: ")
#url += "&q=" + text_search

description_terms = input("Enter the DESCRIPTION search term(s) for the NASA image database: ")
description_terms = description_terms.replace(" ", "%20")
url += "&description=" + description_terms

#media_type = input("Enter the media type (image, video, audio) for the NASA image database: ")
#url += "&media_type=" + media_type

location_term = input("Enter the LOCATION search term for the NASA image database: ")
location_term = location_term.replace(" ", "%20")
url += "&location=" + location_term

keywords_terms = input("Enter the KEYWORD search term(s) for the NASA image database: ")
keywords_terms = keywords_terms.replace(" ", ",")
url += "&keywords=" + keywords_terms

print("API search URL: " + url)
print("-----OPENING--------")
response = urllib.request.urlopen(url)
data_json = json.loads(response.read())


# print the raw JSON data just for display purposes
#print("-------------")
#print("Raw JSON data from NASA:")
#print(data_json)
#print("")

# Check if any images were found - if not, exit
if data_json['collection']['metadata']['total_hits'] == 0:
	print("No images found.")
	exit()

total_hits = data_json['collection']['metadata']['total_hits']
print("\n-------------")
print("Total images found: " + str(total_hits))
print("\n-------------")

# Display the FIRST 5 NASA Photos matching the search criteria
firstImages = min(5, total_hits)
if total_hits > 5:
	print("Displaying the FIRST 5 images only.")
else:
	print("Displaying all images found.")
 
for i in range(0, min(firstImages, total_hits)):
	print("\n-------------")
	print("Opening image " + str(i+1) + " from search...")
	image_url=data_json['collection']['items'][i]['links'][0]['href']
	#print(image_url)

	# Download an image from the NASA website URL
	img = imutils.url_to_image(image_url)
	# Display the image and pause for ESC.
	cv2.imshow(data_json['collection']['items'][i]['data'][0]['title'] + ' ' + data_json['collection']['items'][i]['data'][0]['date_created'], img)
	cv2.waitKey(0)

'''
# Display FIRST NASA Photo matching the search criteria
print("\n\n-------------")
#print("Address of the FIRST Photo in search:")
image_url=data_json['collection']['items'][0]['links'][0]['href']
#print(image_url)

# Download an image from the NASA website URL
img = imutils.url_to_image(image_url)
# Display the image and pause for ESC.
cv2.imshow(data_json['collection']['items'][0]['data'][0]['title'] + ' ' + data_json['collection']['items'][0]['data'][0]['date_created'], img)
cv2.waitKey(0)
'''

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
