import requests


def download_file(url: str, file: str):
    r = requests.get(url)

    with open(file, "wb") as f:

        f.write(r.content)
