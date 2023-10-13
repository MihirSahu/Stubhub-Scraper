# Stubuhb Scraper

- Just trying to get some Olivia Rodrigo tickets on a budget
- Hosted on my server, use cron to run the script periodically, and use [ntfy](https://github.com/binwiederhier/ntfy) to send notifications to my phone when the price drops below a specified value
- I wrote this script on my PC, I had to make a few modifications to run it on my Linux ARM64 server

## Setup
1. Install `selenium`, `requests`, `lxml`, `bs4` modules
2. Download the appropriate [Chromedriver](https://sites.google.com/chromium.org/driver/downloads) and place it in the present working directory
3. Run the script with Python