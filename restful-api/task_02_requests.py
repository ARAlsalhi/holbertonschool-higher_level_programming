#!/usr/bin/python3
"""Fetch posts from an API, print them, and save them as CSV."""

import csv
import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    response = requests.get(API_URL)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save selected fields into posts.csv."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()

        posts_data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["id", "title", "body"]

            writer = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(posts_data)
