import argparse
import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def get_bitlink(link, bitly_token):
    headers = {
        "Authorization": f"Bearer {bitly_token}",
    }
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    long_url = {
        "long_url": link
    }
    response = requests.post(url, json=long_url, headers=headers)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(bitlink, bitly_token):
    bitlink = urlparse(bitlink)
    headers = {
        "Authorization": f"Bearer {bitly_token}",
    }
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink.netloc}{bitlink.path}/clicks/summary"
    params = {
        "unit": "day",
        "units": -1
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(link, bitly_token):
    headers = {
        "Authorization": f"Bearer {bitly_token}",
    }
    link = urlparse(link)
    link = f"{link.netloc}{link.path}"
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}"
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv("BITLY_TOKEN")
    parser = argparse.ArgumentParser()
    parser.add_argument("site_link")
    input_links = parser.parse_args()
    link = input_links.site_link
    try:
        if is_bitlink(link, bitly_token):
            print("Количество переходов:", count_clicks(link, bitly_token))
        else:
            print("Битлинк:", get_bitlink(link, bitly_token))
    except requests.exceptions.HTTPError:
        print("Введите ссылку или битлинк")


if __name__ == "__main__":
    main()
