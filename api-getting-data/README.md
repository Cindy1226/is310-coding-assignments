# Getting Culture API Script

## Overview

This project features a Python script, `getting_culture.py`, designed to interact with both the [Marvel API](https://developer.marvel.com/) and the [Europeana 
API](https://www.europeana.eu/en/developers). The script retrieves data about a specific Marvel character and finds related cultural artifacts in the Europeana 
collection, demonstrating the use of APIs in gathering and combining data from diverse sources.

## APIs Used

### 1. Marvel API
- **Description**: The Marvel API provides access to a wealth of data related to Marvel characters, comics, events, and more. Users can fetch detailed information 
about characters, including their descriptions and images.
- **Why Chosen**: I chose the Marvel API for its rich dataset and the cultural significance of Marvel's universe, which is popular in contemporary media and 
storytelling.

### 2. Europeana API
- **Description**: The Europeana API offers access to millions of digitized items from European cultural heritage institutions. It allows users to search and 
retrieve metadata about various cultural artifacts and collections.
- **API Key**: A valid API key is required to access the Europeana API, which can be obtained by registering at the [Europeana Developer 
Portal](https://www.europeana.eu/en/developers).

## Features

- Fetches data from the Marvel API for a specified character (e.g., Iron Man).
- Searches for related cultural data in the Europeana API using the character's name.
- Combines the data from both APIs and saves the results in a JSON file.

## Requirements

- Python 3.x
- Requests library (install via `pip install requests`)
- hashlib library (included in the standard library)
- time library (included in the standard library)

