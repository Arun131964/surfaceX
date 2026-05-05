# 🔍 Automated Recon & Vulnerability Scanner

A Python-based reconnaissance and basic vulnerability scanning tool designed for bug bounty hunting and penetration testing.

## 🚀 Features

- 🔎 Subdomain Enumeration
  - crt.sh
  - subfinder
  - assetfinder
  - amass (passive)

- 🌐 Live Host Detection

- 🔗 URL Discovery
  - gau
  - waybackurls
  - katana (active crawling)

- 💣 Vulnerability Detection
  - Parameter discovery
  - Basic XSS testing

- 📁 Organized Output
  - Domain-wise + timestamp-based results

---

Installation
```bash
git clone https://github.com/YOUR_USERNAME/recon-tool.git
cd recon-tool
pip install -r requirements.txt


Install external tools:
```bash
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/tomnomnom/assetfinder@latest
go install github.com/lc/gau/v2/cmd/gau@latest
go install github.com/tomnomnom/waybackurls@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/owasp-amass/amass/v4/...@latest

