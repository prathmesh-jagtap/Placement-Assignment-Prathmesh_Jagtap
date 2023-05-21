"""
Module Name: Question_3.py
Author: Prathmesh Jagtap
Created: May 18, 2023

Description: This script scrapes data from a website and stores it in an Excel file.

Usage:
    - Make sure the required libraries (e.g., requests, BeautifulSoup, pandas) are installed.
    - Run the script to initiate the data scraping process.
    - The scraped data will be saved in an Excel file named "output.xlsx" in the same directory.

Notes:
    - Ensure a stable internet connection for successful web scraping.
    - The website URL and the structure of the data may need to be adjusted based on specific requirements.
"""
# Liberaries required
import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime


class DataScraper:
    """
    A class for scraping data from a web URl and saving it to a file.
    """

    def __init__(self, url, output_file, file_type):
        """
        Initialize the DataScraper instance.

        Args:
            url (str): The URL of the web API to scrape data from.
            output_file (str): The name of the output file.
            file_type (str): The type of output file ('excel' or 'csv').
        """
        self.url = url
        self.output_file = output_file
        self.file_type = file_type

    def Web_data(self):
        """
        Scrape data from the provided URL.

        Returns:
            dict: The scraped data.
        """
        print(f"Data scraping started: {self.url}")
        response = requests.get(self.url)
        data = response.json()
        return data

    def data_list(self):
        """
        Extract the list of data from the scraped data.

        Returns:
            list: The list of data.
        """
        list_data = self.Web_data()
        return list_data["pokemon"]

    def scrape_data(self):
        """
        Scrape and process the data.

        Returns:
            list: The processed dataset.
        """
        try:
            data_list = self.data_list()

            # Prepare the dataset
            dataset = []
            for row in data_list:
                episodes_data = {}
                nested_keys = []
                for key, value in row.items():
                    if isinstance(value, list):
                        value = ', '.join(str(m) for m in value)
                    elif isinstance(value, str):
                        value = self.clean_html_tags(value)
                        value = self.convert_to_12_hour_format(value)
                    elif isinstance(value, dict):
                        nested_keys.append(key)
                        for k, v in value.items():
                            new_key = f"{k} {key}"
                            episodes_data[new_key] = v
                    episodes_data[key] = value

                # Remove nested dictionaries
                for rk in nested_keys:
                    episodes_data.pop(rk, None)

                dataset.append(episodes_data)
            return dataset

        except Exception as error:
            print(f"Error occurred: {error}")

    def convert_to_12_hour_format(self, value):
        """
        Convert a time value in 24-hour format to 12-hour format.

        Args:
            value (str): The time value to convert.

        Returns:
            str: The time value in 12-hour format, or the original value if not a valid time.
        """
        if not isinstance(value, str):
            return value

        # Regular expression pattern to match time in 24-hour format
        time_pattern = r'^([01]\d|2[0-3]):([0-5]\d)$'

        # Check if the value matches the time pattern
        if re.match(time_pattern, value):
            # Convert the value to a datetime object
            time_obj = datetime.strptime(value, '%H:%M')
            # Convert the time to a 12-hour format string
            time_12_hour_format = time_obj.strftime('%I:%M %p')
            return time_12_hour_format

        return value

    def clean_html_tags(self, text):
        """
        Check if a text contains HTML tags and remove them if present.

        Args:
            text (str): The input string to check for HTML tags and remove them.

        Returns:
            str: The text string with HTML tags removed, or the original text if no tags were found.
        """
        soup = BeautifulSoup(text, "html.parser")
        tags = soup.find_all()
        if len(tags) > 0:
            clean_text = soup.get_text(separator=" ")
            return clean_text.strip()
        return text

    def save_data_to_file(self):
        """
        Scrape the data, process it, and save it to a file.
        """
        dataset = self.scrape_data()
        # Convert the dataset to a DataFrame and save it to an Excel file
        output_dataset = pd.DataFrame(dataset)
        # Capitalize column names
        output_dataset.columns = output_dataset.columns.str.capitalize()

        if self.file_type == 'excel':
            output_dataset.to_excel(f"{self.output_file}.xlsx", index=False)
        elif self.file_type == 'csv':
            output_dataset.to_csv(f"{self.output_file}.csv", index=False)
        print("Output successfully saved!")


url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
output_file = "Pokemon Data"
file_type = "excel"

scraper = DataScraper(url, output_file, file_type)
scraper.save_data_to_file()
