"""
Module Name: Question_4.py
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

url = "https://data.nasa.gov/resource/y77d-th95.json"
output_file = "Meteorite Data"
file_type = 'csv'
MeteoriteDataScrape = DataScraper(url, output_file, file_type)
MeteoriteDataScrape.data_list = lambda: MeteoriteDataScrape.Web_data()
MeteoriteDataScrape.save_data_to_file()
