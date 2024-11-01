import requests #Import the requests library to handle HTTP requests

url = "https://official-joke-api.appspot.com/random_joke" # URL of the API that provides a random joke
json_data = requests.get(url).json()  # Make a GET request to the URL and convert the response to JSON format

# Initialize an array to hold the joke setup and punchline
arr = ["",""]
arr[0] = json_data["setup"]  #Store the joke setup in the first index of arr
arr[1] = json_data["punchline"] # Store the joke punchline in the second index of arr

def joke():
    return arr # Return the array containing the setup and punchline