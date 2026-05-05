import requests


def check_alive(subdomains):
    alive = []

    for sub in subdomains:
        for scheme in ["http://", "https://"]:
            try:
                url = scheme + sub
                requests.get(url, timeout=3)
                alive.append(url)
                break
            except:
                continue

    return alive
