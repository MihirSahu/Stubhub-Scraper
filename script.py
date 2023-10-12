from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

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

# Find all div elements in the HTML document
divs = soup.find_all('div', class_='sc-fMtJSh BovtL')

# Loop through the divs and do something with them
for div in divs:
    # Do something with the div
    print(div.text)

# Quit the browser
driver.quit()