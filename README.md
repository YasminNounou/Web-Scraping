# Web-Scraping

Project Overview: Hidden Property Deals Collection System
This project involves building a system to help a client discover hidden property deals by collecting and serving data from multiple online sources. The solution is divided into two key components:

**Objective**
Develop a two-stage solution that:
1. Extracts property listings (title, price, location, link) from online sources using Python.
2. Exposes the data via an API using Node.js and Express with filtering capabilities.

**Task Breakdown**
**Step 1: Python Web Scraper**
- Create a Python script that crawls one or more property listing websites and extracts relevant property information.
**Requirements:
**
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
    "location": "Manchester, UK",
    "link": "https://example.com/property/123"
  },

Tools/Tech:
Python 3.x
requests, BeautifulSoup, or any preferred scraping libraries

**Step 2: Node.js API Microservice
**
Goal:
Create a simple Express.js API that serves the scraped data.
**Requirements:
**
Read from the listings.json file
Create the following endpoint:
bash
GET /api/listings
Support the following optional query parameters for filtering:
minPrice
maxPrice
location
Example Usage:
GET /api/listings?minPrice=200000&maxPrice=300000&location=London
Expected Output:
A filtered list of matching property listings in JSON format.

Tools/Tech:
Node.js
Express.js

**Deliverables**
scraper.py — Python web scraping script
listings.json — Generated output file from the scraper
server.js — Node.js Express API server
README.md — documentation

Success Criteria
1. Scraper collects clean, structured data and writes to listings.json
2. API starts without errors and correctly reads from listings.json
3. API returns correct results and filters by price and location as expected
