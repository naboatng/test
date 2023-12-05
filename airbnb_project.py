from bs4 import BeautifulSoup
import requests

url = "https://www.airbnb.com/s/Dubai-~-United-Arab-Emirates/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-01-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Dubai%20-%20United%20Arab%20Emirates&place_id=ChIJRcbZaklDXz4RYlEphFBu5r0&date_picker_type=calendar&checkin=2023-12-14&checkout=2023-12-20&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=6&adults=1"
response = requests.get(url)


soup = BeautifulSoup(response.content,'lxml')
soup.select('[itemprop=itemListElement]')

for item in soup.select('[itemprop=itemListElement]'):
   # print(item)
   try:
     print(item.select('a')[0]['aria-labelledby'])
     print(item.select('a')[0]['href'])
     print(item.select('[class=_1y74zjx]'.strip('\n','')))

   except Exception as e:
    print('')
    print('________________')



