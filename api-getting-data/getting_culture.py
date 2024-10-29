import requests
import json
import hashlib
import time

# Type your EUROPEANA API key below:
EUROPEANA_API_KEY = "videellegi "  # Replace with your actual Europeana API key

# Type your MARVEL API credentials below:
MARVEL_PUBLIC_KEY = "4474d30154e36d654646761cfbec905a"  # Replace with your actual Marvel public key
MARVEL_PRIVATE_KEY = "58adc2ae6b340003e2fe64e1a06d8a8ea026413a"  # Replace with your actual Marvel private key

# Function to generate Marvel API timestamp and hash
def get_marvel_auth():
    timestamp = str(int(time.time()))
    hash_value = hashlib.md5((timestamp + MARVEL_PRIVATE_KEY + MARVEL_PUBLIC_KEY).encode()).hexdigest()
    return timestamp, hash_value

# Get data from the Marvel API for a specific character
def get_marvel_character(character_name):
    timestamp, hash_value = get_marvel_auth()
    marvel_url = "https://gateway.marvel.com/v1/public/characters"
    params = {
        "name": character_name,
        "apikey": MARVEL_PUBLIC_KEY,
        "ts": timestamp,
        "hash": hash_value
    }
    response = requests.get(marvel_url, params=params)
    if response.status_code == 200:
        marvel_data = response.json()
        return marvel_data
    else:
        print("Failed to fetch data from Marvel API.")
        return None

# Get related sports data from the Europeana API
def get_europeana_sports_data(query):
    europeana_url = "https://api.europeana.eu/record/v2/search.json"
    params = {
        "query": query,
        "wskey": EUROPEANA_API_KEY,
        "rows": 1
    }
    response = requests.get(europeana_url, params=params)
    if response.status_code == 200:
        europeana_data = response.json()
        return europeana_data
    else:
        print("Failed to fetch data from Europeana.")
        return None

# Save combined data to a JSON file
def save_to_json(data, filename="marvel_europeana_data"):  # No .json extension
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
    print(f"Data saved to {filename}")

def main():
    print("Starting getting_culture.py")
    # Specify the character you want to look up in the Marvel API
    character_name = "Iron Man"  # Example character; you can change this

    # Fetch data from the Marvel API
    marvel_data = get_marvel_character(character_name)
    if not marvel_data or not marvel_data['data']['results']:
        print("No data returned for the specified Marvel character.")
        return

    # Display the character's name
    marvel_character = marvel_data['data']['results'][0]
    print(f"Marvel Character: {marvel_character['name']}")

    # Fetch Europeana data based on the selected character's name
    europeana_data = get_europeana_sports_data(character_name)
    if not europeana_data:
        print("No Europeana data returned.")
        return

    # Combine both datasets and save to a JSON file
    combined_data = {
        "Marvel Character": {
            "Name": marvel_character['name'],
            "Description": marvel_character.get('description', 'No description available.'),
            "Thumbnail": f"{marvel_character['thumbnail']['path']}.{marvel_character['thumbnail']['extension']}"
        },
        "Europeana Sports Data": europeana_data.get("items", [])
    }
    save_to_json(combined_data)

if __name__ == "__main__":
    main()

