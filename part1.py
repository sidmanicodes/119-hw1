"""
Part 1:
"""

"""
A. Determine the largest 10 countries in the world by population.

This part will ask you to get this data in three different ways.
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
