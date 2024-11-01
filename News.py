
from Api import * # Imports all the contents from the Api module (presumably including the api_key)
import requests # Imports the requests library for making HTTP requests

# API endpoint to fetch the top business headlines from the US
api_address = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey="+api_key

# Make a GET request to the API and parse the response as JSON
json_data = requests.get(api_address).json()

ar = [] # Initialize an empty list to store news headlines


def news():
    ar.clear() # Clear the list before appending new headlines
    for i in range(3): # Loop to get the top 3 articles

        # Get the title of the i-th article
        headline = json_data["articles"][i]["title"]

        # Append formatted headlines to the list ar
        ar.append("Number "+str(i+1)+': '  + headline+".")

    return ar

news() # Call the news function to populate the list ar
arr = news() # This calls the news function again and assigns the result to arr






