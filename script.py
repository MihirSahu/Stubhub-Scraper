from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

# Set up the headless browser
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the website
one_ticket_url = 'https://www.stubhub.com/olivia-rodrigo-houston-tickets-2-27-2024/event/152301318/?quantity=1&priceOption=1%2C270%2C8999.1&listingId=&listingQty='
two_ticket_url = 'https://www.stubhub.com/olivia-rodrigo-houston-tickets-2-27-2024/event/152301318/?quantity=2&priceOption=1%2C270%2C8999.1&listingId=&listingQty='
driver.get(two_ticket_url)

# Get the page source and parse it with BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

stubhub_event_details_tag = soup.find(id='stubhub-event-detail-listings-grid')
event_details_tags = stubhub_event_details_tag.find_all(recursive=False)[0]
event_details_tags_2 = event_details_tags.find_all(recursive=False)[:-3]

sections_prices = []
restricted_sections = ['401', '402', '403', '404', '405', '406', '407', '408', '428', '429', '430', '431', '432', '433', '434', '101', '102', '103', '104', '105', '122', '123', '124', '125', '126']

for div in event_details_tags_2:
    try:
        text = div.find_all(recursive=False)[0].find_all(recursive=False)[0].find_all(recursive=False)[0].text
        section = text[text.find('Section') + 8:text.find('|') - 1]
        # Check that sections aren't sections 401-408, 428-434, 101-105, or 122-126
        if section in restricted_sections:
            continue
        price = text[text.find('$') + 1:text.find('each')]
        sections_prices.append([section, price])
        # print("Section " + section + " costs " + price + " each")
    except Exception as e:
        # print(e)
        continue

acceptable_prices_string = ''
for idx, section_price in enumerate(sections_prices):
    if int(section_price[1]) < 300:
        acceptable_prices_string += "Section " + section_price[0] + " is available for $" + section_price[1] + " each" + '\n'

requests.post('http://129.146.208.177/test', data=acceptable_prices_string)

# Quit the browser
driver.quit()