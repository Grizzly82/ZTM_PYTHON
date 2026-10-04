import hashlib
import requests
import sys

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def request_api_data(prefix):
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url, timeout=5)
    if res.status_code != 200:
        raise RuntimeError(f"{RED}Error fetching: {res.status_code}{RESET}")
    return res

def read_response(response):
    return (line.split(':') for line in response.text.splitlines())

def get_password_leaks_count(hashes, hash_to_check):
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0

def pawned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5)
    hashes = read_response(response)
    return get_password_leaks_count(hashes, tail)

def main():
    print(f"{CYAN}=== Password Breach Checker ==={RESET}")
    user_password = input("Enter your password: ")

    if not user_password:
        print(f"{YELLOW}Password cannot be empty.{RESET}")
        return

    count = pawned_api_check(user_password)

    print(f"\n{CYAN}{'*' * 65}{RESET}\n")

    if count:
        print(f"{RED}⚠️  Your password has been compromised {count} times!{RESET}")
        print(f"{YELLOW}You should change it immediately.{RESET}")
    else:
        print(f"{GREEN}✔ Your password has NOT been found in known breaches.{RESET}")

    print(f"\n{CYAN}{'*' * 65}{RESET}\n")

if __name__ == '__main__':
    sys.exit(main())
