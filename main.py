import argparse
import os
from datetime import datetime

from modules.subdomain_enum import get_all_subdomains
from modules.alive_check import check_alive
from modules.url_fetch import get_urls
from modules.vuln_scan import find_params


def save(file, data):
    with open(file, "w") as f:
        for line in data:
            if line.strip():
                f.write(line.strip() + "\n")


def main():
    parser = argparse.ArgumentParser(description="Automated Recon Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    args = parser.parse_args()

    domain = args.domain

    # Create output folder (domain + timestamp)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = f"output/{domain}/{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    print(f"[+] Output directory: {output_dir}")

    # ----------------------------
    # Subdomain Enumeration
    # ----------------------------
    print("[+] Collecting subdomains...")
    subs = get_all_subdomains(domain)
    save(f"{output_dir}/subdomains.txt", subs)
    print(f"[+] Found {len(subs)} subdomains")

    # ----------------------------
    # Alive Check
    # ----------------------------
    print("[+] Checking alive domains...")
    alive = check_alive(subs)
    save(f"{output_dir}/alive.txt", alive)
    print(f"[+] Alive domains: {len(alive)}")

    # ----------------------------
    # URL Collection (FIXED)
    # ----------------------------
    print("[+] Fetching URLs...")
    urls = set()

    for live in alive:
        clean_domain = live.split("//")[-1]
        urls.update(get_urls(clean_domain))

    urls = list(urls)
    save(f"{output_dir}/urls.txt", urls)
    print(f"[+] URLs collected: {len(urls)}")

    # ----------------------------
    # Parameter Finding
    # ----------------------------
    print("[+] Finding parameters...")
    params = find_params(urls)
    save(f"{output_dir}/params.txt", params)
    print(f"[+] Potential params: {len(params)}")

    print("[✓] Recon Completed!")


if __name__ == "__main__":
    main()
