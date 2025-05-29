# Web-Scraping

This project is for scrapping data from a web page for listing properties, to extract some info like title, price...etc and save these info a json format file to be then accessed by the API "/listing" that applis filters on the saved data.

**Objective**
Develop a two-stage solution that:
1. Extracts property listings (title, price, location, link) from online sources using Python.
2. Exposes the data via an API using Node.js and Express with filtering capabilities.

***Web scrapping module 1: Python Web Scraper**
**How to run**
Navigate to ./web_scrapping_module directory and run these commands
```pip install Beautifulsoup requests```
  ```python web_scrapper.py```
- Create a Python script that crawls all the pages property listing from website and extracts relevant property information.
**Requirements:**
Extract the following data:
1. title
2. price
3. location
4. link
Save the scraped data in a JSON file named listings.json.

- Output Format: json
  {
    "title": "3 Bedroom House in Suburbia",
    "price": 220000,
    "location": "XXX2",
    "link": "https://example.com/property/123"
  },

Tools/Tech:
Python 3.11
requests, BeautifulSoup, or any preferred scraping libraries

***Listing properties API 2: Node.js API Microservice**
**How to run**
Navigate to ./listing_properties_API directory and run this command 
```nom install Express```
  ```npm start```
  it should start on port 5001
Read from the listings.json file
Create the following endpoint:
bash
GET /api/listings
Support the following optional query parameters for filtering:
priceMin
priceMax
location
Example Usage:
GET /api/listings?priceMin=200000&priceMax=300000&location=S02
Expected Output:
A filtered list of matching property listings in JSON format.

Tools/Tech:
Node.js
Express.js
