"""Reads Baby Name data from data.gov, and plots
frequency of given names by year"""


import csv
import glob
import pprint

import numpy as np
import matplotlib.pyplot as plt


def parse(raw_file, delimiter=","):
    """Parses a raw file with annual frequencies of
    baby names and returns a dict with (Name, Gender)
    pairs as the keys and frequencies as the values."""
    
    # Open file
    opened_file = open(raw_file)
    
    # Read file
    raw_data = csv.reader(opened_file, delimiter=delimiter)
    
    # Set up an empty dictionary
    parsed_data = {}
    
    # Iterate over each row of csv file, add 
    # (Name, Gender) -> Frequency to the dictionary
    for row in raw_data:
        parsed_data[(row[0], row[1])] = int(row[2])
    
    # Close file
    opened_file.close()

    return parsed_data


# Name parameter is actually a tuple with (Name, Gender)
def plot_name(name, data):
    """Given a name and the annual name data,
    plots the annual frequency of the name"""
    
    # Find the subset of data that applies to the given name.
    # If the name doesn't exist in a year's associated dict,
    # assume the frequency is 0.
    data = [data[i].get(name, 0) for i in range(len(data))]
    plt.plot(data, label=name[0])


def main():
    # Find all the files with 
    filenames = glob.glob('data/yob*.txt')
    data = []

    for f in filenames:
        parsed_data = parse(f)
        data.append(parsed_data)
    
    # Define the names we want to plot. These are actually
    # tuples with (Name, Gender) in order to handle names
    # that could be either gender.    
    names = [('Amy', 'F'), ('Amie', 'F'), ('Aimee', 'F'), ('Aimie', 'F')]

    for name in names:
        plot_name(name, data)
    
    # Set up the x-axis for the plot
    # Our annual data starts at year 1880
    years = tuple(range(1880, 1880+len(filenames)))
    years_labels = tuple([x for x in years if x % 10 == 0])
    years_ticks = tuple(range(len(years)))
    plt.xticks(years_ticks, years_labels)
    plt.legend()
    plt.show()    


if __name__ == '__main__':
    main()