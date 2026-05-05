import requests
import subprocess


def crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subs = set()

    try:
        res = requests.get(url, timeout=10)
        data = res.json()

        for entry in data:
            names = entry.get("name_value", "")
            for sub in names.split("\n"):
                subs.add(sub.strip())
    except:
        pass

    return subs


def run_tool(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True).decode()
        return set(output.splitlines())
    except:
        return set()


def get_all_subdomains(domain):
    subs = set()

    print("[*] Running crt.sh...")
    subs |= crtsh(domain)

    print("[*] Running subfinder...")
    subs |= run_tool(f"subfinder -d {domain} -silent")

    print("[*] Running assetfinder...")
    subs |= run_tool(f"assetfinder --subs-only {domain}")

    print("[*] Running amass (passive)...")
    subs |= run_tool(f"amass enum -passive -d {domain}")

    return list(subs)
