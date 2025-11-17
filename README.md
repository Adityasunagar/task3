# task3

News Headlines Scraper
Objective

Scrape top news headlines from a website and save them into a text file.

Tools Used

Python

requests for fetching webpage HTML

BeautifulSoup (bs4) for parsing headlines

How It Works

The script sends a request to a news website (default: BBC News).

It extracts all <h2> headline tags using BeautifulSoup.

All headlines are saved into headlines.txt.

Run the Script
 * python news_scrap.py
