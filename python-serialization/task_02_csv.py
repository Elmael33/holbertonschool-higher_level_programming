#!/usr/bin/python3
"""
This module contains the convert_csv_to_json function
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Converts data from a CSV file to JSON format and writes it to data.json.
    """
    my_list = []
    try:
        with open(csv_file, "r", encoding="utf-8") as myFile:
            csvReader = csv.DictReader(myFile)
            for rows in csvReader:
                my_list.append(rows)

        with open("data.json", "w", encoding="utf-8") as myFile:
            json.dump(my_list, myFile, indent=1)

        return True
    except (
            FileNotFoundError, csv.Error, AttributeError,
            EOFError, ImportError, IndexError
            ):
        return False
