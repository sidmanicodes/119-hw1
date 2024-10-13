"""
Part 1: Data Processing Fundamentals

This part is a series of basic exercises about data processing
fundamentals using Pandas.

"""

"""
A. Differences between data sources

This part will explore how data sources differ, and how we can
mitigate this and understand the implications.

We will build a simple pipeline to determine the
10 largest and smallest countries in the world by population,
and then to get the total of these 10 countries in each case.

To do that, we will get the data in three different ways.

Write three functions that get the input data for your pipeline
from three different sources.

1. From Our World in Data:
    https://ourworldindata.org/grapher/population

2. From someone's provided dataset on GitHub:
    https://github.com/datasets/population?tab=readme-ov-file

3. By scraping data from Wikipedia:
    Please use the following link:
    https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1249043677

For the first and second one, you may download the input as a CSV.

For the third one, you will write a function which scrapes the data from
the Wikipedia table.
"""

def get_country_populations():
    # Scrape data from online
    raise NotImplementedError

# Method 1: download a CSV file from
# https://ourworldindata.org/grapher/population

import pandas as pd

def get_population_data():
    # Load the data from population.csv into a pandas DataFrame
    # Pandas documentation:
    # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
    df = pd.read_csv("population.csv")

    # Sort the data by population
    # print(df.head())
    # print(df.keys())
    df = df.sort_values("Population (historical)", ascending=False)

    # Filter for the most recent year
    df = df[df["Year"] == 2023]

    # print(df)

    # Return the data
    return df

# Method 2: download data from GitHub

# Search on GitHub: https://github.com/search?q=country%20population&type=repositories
# https://github.com/datasets/population

def get_github_data():
    # Load the data from GitHub
    url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
    df = pd.read_csv(url)

    # print(df.head())

    # Sort the data by population
    df = df.sort_values("Value", ascending=False)

    # Filter for the most recent year
    df = df[df["Year"] == 2021]

    # Return the data
    return df

# Method 3: scrape the data from wikipedia

WIKIPEDIA_PAGE_NAME = "List_of_countries_by_population_(United_Nations)"

import requests
from bs4 import BeautifulSoup

# Get the data from the Wikipedia page
def get_wikipedia_data():

    # Get the data from the Wikipedia page
    response = requests.get(f"https://en.wikipedia.org/wiki/{WIKIPEDIA_PAGE_NAME}")
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table with the data
    table = soup.find("table", class_="wikitable")

    # Extract the data from the table
    data = []
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) == 0:
            continue

        # # Debug
        # print(cells)
        # print(cells[0].text.strip())
        # print(cells[1].text.strip())
        # print(cells[2].text.strip())
        # print(cells[3].text.strip())
        # # pause
        # import time
        # time.sleep(1)

        country = cells[0].text.strip()
        population = int(cells[2].text.strip().replace(",", ""))
        data.append((country, population))

    # Return the data
    return pd.DataFrame(data, columns=["Country", "Population"])

# Let's test our code

print(get_population_data())
print(get_github_data())
print(get_wikipedia_data())
