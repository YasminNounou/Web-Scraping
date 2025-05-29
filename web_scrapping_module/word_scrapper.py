import requests
from bs4 import BeautifulSoup
import json
import time
import os
from web_scrapper_constants import BASE_URL_REPOSSESSED as base_url
from web_scrapper_constants import HEADERS as headers

def extract_properties(soup):
    map_div = soup.find("div", id="map-properties")
    if not map_div:
        print("Could not find the #map-properties div.")
        exit()
    property_divs = map_div.find_all(lambda tag:
        tag.name == "div" and
        tag.find("a", class_="archive-properties-title-link") is not None, class_="w-full"
    )
    page_properties  = []

    for prop in property_divs:
        try:
            a_tag = prop.find("a", class_="archive-properties-title-link")
            title = a_tag.get_text(strip=True) if a_tag else "N/A"
            link = a_tag["href"] if a_tag and a_tag.has_attr("href") else "N/A"

            location_container = prop.find("div", class_="text-[#294052]")
            location = location_container.get_text(strip=True) if location_container else "N/A"

            price_tag = prop.find("div", class_="carlito-bold text-[1.75rem]")
            price = price_tag.get_text(strip=True) if price_tag else "N/A"

            if title != "N/A" and link != "N/A":
                page_properties.append({
                    "title": title,
                    "link": link,
                    "location": location,
                    "price": price
                })

        except Exception as e:
            print("Error processing one property:", e)
    
   
    return page_properties

def get_total_pages(soup):
    pagination = soup.find("div", id="map-pagination")
    if not pagination:
        return 1  # fallback if pagination not found

    page_links = pagination.find_all("a", class_="page-numbers")
    
    max_page = 1
    for link in page_links:
        try:
            page_num = int(link.get_text(strip=True))
            max_page = max(max_page, page_num)
        except Exception as e:
            # log error
            print(f"Error in getting page count with error {e}")
            continue  
    print(f"Total pages found: {max_page}")
    return max_page

if __name__ == "__main__":
    try:
        response = requests.get(base_url, headers=headers)
        time.sleep(1.5)   #add wait time 
        if response.status_code != 200:
            print(f"Failed to fetch page , status: {response.status_code}")
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"Error : {e}")
        

    for page in range(1, get_total_pages(soup) + 1):
            url = f"{base_url}/?page={page}/" if page > 1 else base_url
            print(f"Scraping page {page}...", url)
            # if page == 5:
            #     print("Skipping...")
            #     break
            response = requests.get(url, headers=headers)
            time.sleep(1.5)  #add wait time 
            if response.status_code != 200:
                print(f"Failed to fetch page {page}, status: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            props = extract_properties(soup)
            print(f"Found {len(props)} properties on page {page}")

            try:
                existing_properties = []
                if os.path.exists("listings.json"):
                    with open("properties.json", "r", encoding="utf-8") as fr:
                        try:
                            existing_properties = json.load(fr)
                        except json.JSONDecodeError:
                            existing_properties = []
                        existing_properties.extend(props)
                with open("properties.json", "w", encoding="utf-8") as f:
                    json.dump(existing_properties, f, indent=4, ensure_ascii=False)
        
            except (FileNotFoundError, json.JSONDecodeError):
                existing_properties = []
            # Add sleep time between requests
            time.sleep(5)

    
