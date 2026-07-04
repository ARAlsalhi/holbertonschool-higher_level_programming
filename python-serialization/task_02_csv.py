#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON and save it in data.json."""
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except (FileNotFoundError, OSError):
        return False
