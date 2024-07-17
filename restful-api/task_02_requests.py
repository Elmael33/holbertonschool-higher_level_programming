#!/usr/bin/env python3
"""Consuming and processing data from an API using Python"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print the titles."""
    response = requests.get = 'https://jsonplaceholder.typicode.com/posts'
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")

def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them to a CSV file."""
    response = requests.get = 'https://jsonplaceholder.typicode.com/posts'
    
    
    if response.status_code == 200:
        posts = response.json()
        
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
        
        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts")
