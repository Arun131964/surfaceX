import subprocess


def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode().splitlines()
    except:
        return []


def get_urls(domain):
    urls = set()

    print(f"[*] Collecting URLs for {domain}...")

    urls.update(run(f"gau {domain} 2>/dev/null"))
    urls.update(run(f"waybackurls {domain} 2>/dev/null"))
    urls.update(run(f"katana -u https://{domain} -silent 2>/dev/null"))

    return list(urls)
