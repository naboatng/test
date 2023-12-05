import requests
from bs4 import BeautifulSoup

def scrape_airbnb_prices(url):


    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # # Save the HTML to a file for inspection (optional)
        # with open("airbnb_page.html", "w", encoding="utf-8") as file:
        #     file.write(str(soup))

        # Find elements containing the price information
        price_tags = soup.find_all('div', class_='_i5duul')
        prices = [tag.get_text() for tag in price_tags]

        return prices
    else:
        print('Failed to fetch data')

# Replace this URL with the Airbnb search URL of your choice
airbnb_url = "https://www.airbnb.com/s/Dubai-~-United-Arab-Emirates/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-01-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Dubai%20-%20United%20Arab%20Emirates&place_id=ChIJRcbZaklDXz4RYlEphFBu5r0&date_picker_type=calendar&checkin=2023-12-14&checkout=2023-12-20&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=6&adults=1"

prices = scrape_airbnb_prices(airbnb_url)
if prices:
    for idx, price in enumerate(prices, start=1):
        print(f"Listing {idx} price: {price}")
