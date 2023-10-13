# Stubuhb Scraper

- Just trying to get some Olivia Rodrigo tickets on a budget
- Hosted on my server, use cron to run the script periodically, and use [ntfy](https://github.com/binwiederhier/ntfy) to send notifications to my phone when the price drops below a specified value

## Setup
1. Install `selenium`, `requests`, `lxml`, `bs4` modules
2. If on Ubuntu, install Chromedriver with `sudo apt-get update && sudo apt-get install chromium-driver`
3. Set up Cron to run the script every hour

## Resources
- https://github.com/ultrafunkamsterdam/undetected-chromedriver/issues/911#issuecomment-1601580457
- https://stackoverflow.com/a/76550727

Note: The script on this branch is edited specifically to be run on the Linux server