import requests

BASE_URL = "http://preeventualist.org/lost/"


def open_page(page, query):
    response = requests.get(BASE_URL + page, params=query)
    response.raise_for_status()
    return response.text.split("--\n")


def search(word):
    return open_page("search", {"q": word})


def search_lost(word):
    return open_page("searchlost", {"q": word})


def search_found(word):
    return open_page("searchfound", {"q": word})


def add_found(your_name, item_lost, found_at, description):
    return open_page(
        "addfound",
        {
            "name": your_name,
            "item": item_lost,
            "at": found_at,
            "desc": description,
        },
    )


def add_lost(your_name, item_found, last_seen, description):
    return open_page(
        "addlost",
        {
            "name": your_name,
            "item": item_found,
            "seen": last_seen,
            "desc": description,
        },
    )