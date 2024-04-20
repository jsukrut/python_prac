import requests

url = "https://openlibrary.org/search/authors.json?q=j k rowling"


def custom_get(url):
    if url:
        print(url)
        response = requests.get(url)
        if response.status_code ==200:
            print(response.json())
    else:
        print("Add URL")

requests.custom_get = custom_get
requests.custom_get(url)

