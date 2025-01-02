import requests
import argparse
from colorama import Fore, init


def make_request(url):
    if isinstance(url, str):
        pass
    else:
        print(Fore.RED + f"{url}: is not a string it is of type({type(url)})")
        return
    req = requests.get(url)
    stat_col = Fore.RED
    if int(req.status_code) in range(199, 300):
        stat_col = Fore.GREEN
    print(f"{Fore.GREEN}url: {req.url} {stat_col}status_code: {req.status_code}")

    print(req.raw)


def search_username(username, url):
    if isinstance(username, str):
        pass
    else:
        print(Fore.RED + f"{username}: is not a string it is of type({type(username)})")
        return
    url += f"/{username}"
    make_request(url)


if __name__ == '__main__':
    init()
    parser = argparse.ArgumentParser()
    parser.add_argument("url")

    args = parser.parse_args()

    search_username("AlexTriedLife", args.url)
