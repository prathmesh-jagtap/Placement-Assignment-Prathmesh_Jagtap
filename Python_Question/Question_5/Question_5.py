"""
Module Name: Question_5.py
Author: Prathmesh Jagtap
Created: May 18, 2023

Description: This script scrapes data from a website and stores it in an CSV file.

Usage:
    - Make sure the required libraries (e.g., requests, BeautifulSoup, pandas) are installed.
    - Run the script to initiate the data scraping process.
    - The scraped data will be saved in an CSV file named "output.xlsx" in the same directory.

Notes:
    - Ensure a stable internet connection for successful web scraping.
    - The website URL and the structure of the data may need to be adjusted based on specific requirements.
"""
from Python_Question.Question_3.Question_3 import DataScraper


url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
output_file = "TV Episodes API Data"
file_type = "excel"
EpisodeDataScrape = DataScraper(url, output_file, file_type)
EpisodeDataScrape.data_list = lambda: EpisodeDataScrape.Web_data()[
    "_embedded"]['episodes']
EpisodeDataScrape.save_data_to_file()
