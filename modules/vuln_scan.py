def find_params(urls):
    vulnerable = []

    for url in urls:
        if "=" in url and not any(ext in url for ext in [".js", ".css", ".png", ".jpg", ".svg"]):
            vulnerable.append(url)

    return vulnerable
