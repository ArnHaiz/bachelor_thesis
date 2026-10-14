import requests


def search(server, url):
    try:
        r = requests.get(url)
        if r.status_code == 200 or r.status_code == 206:
            print(r.status_code)
            return r.text
        else:
            handle_error(r)
            return None

    except ConnectionError:
        print(f"Error connecting to {server}.")
        return None

def handle_error(e):
    if e.status_code == 429:
        print('Error 429, attempted too many requests.')