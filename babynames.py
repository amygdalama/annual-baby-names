"""Reads Baby Name data from data.gov, and plots
frequency of given names by year"""


import csv
import glob
import pprint

import numpy as np
import matplotlib.pyplot as plt


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""
    
    # Open CSV file
    opened_file = open(raw_file)
    
    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    
    # Set up an empty list
    parsed_data = {}
    
    # Iterate over each row of csv file, zip together field -> value
    for row in csv_data:
        parsed_data[(row[0], row[1])] = int(row[2])
    
    # Close CSV file
    opened_file.close()

    return parsed_data


# Name parameter is actually a tuple with (Name, Gender)
def plot(name, data):
    """Given a name and the Baby Name data,
    plots the annual frequency of the name"""
    
    data = [data[i].get(name, 0) for i in range(len(data))]
    plt.plot(data, label=name[0])


def main():
    filenames = glob.glob('data/yob*.txt')
    data = []

    for f in filenames:
        parsed_data = parse(f, ',')
        data.append(parsed_data)
        
    names = [('Amy', 'F'), ('Amie', 'F'), ('Aimee', 'F'), ('Aimie', 'F')]

    for name in names:
        plot(name, data)

    years = tuple(range(1880, 1880+len(filenames)))
    years_labels = tuple([x for x in years if x % 10 == 0])
    years_ticks = tuple([x-1880 for x in years])
    plt.xticks(years_ticks, years_labels)
    plt.legend()
    plt.show()    


if __name__ == '__main__':
    main()