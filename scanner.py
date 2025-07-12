import requests

def is_vulnerable(url):
    payload = "' OR '1'='1"
    try:
        r = requests.get(url + payload)
        if "error" in r.text.lower() or "sql" in r.text.lower():
            return True
        return False
    except requests.exceptions.RequestException:
        return False

def scan_from_file(file_path):
    with open(file_path, 'r') as f:
        urls = f.read().splitlines()

    for url in urls:
        print(f"\nScanning: {url}")
        if is_vulnerable(url):
            print(f"[!] Vulnerable to SQL Injection → {url}")
        else:
            print("[+] Not vulnerable")

if __name__ == "__main__":
    scan_from_file("test_sites.txt")
