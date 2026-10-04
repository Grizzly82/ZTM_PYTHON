import hashlib
import requests
import sys


def request_api_data(prefix):
    """Request data from HIBP API using the first 5 chars of the SHA1 hash."""
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}. Try again.")

    return res


def read_response(response):
    """Parse API response into (hash_suffix, count) pairs."""
    return (line.split(':') for line in response.text.splitlines())


def get_password_leaks_count(hashes, hash_to_check):
    """Return number of times the password hash appears in breaches."""
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0


def pawned_api_check(password):
    """Check if password has been exposed in data breaches."""
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]

    response = request_api_data(first5)
    hashes = read_response(response)

    return get_password_leaks_count(hashes, tail)


def main():
    user_password = input("Enter your password to check if it has been compromised: ")

    count = pawned_api_check(user_password)

    print("\n*******************************************************************\n")

    if count:
        print(f"⚠️ Your password has been compromised **{count} times**.")
        print("You should change your password immediately.")
    else:
        print("✅ Your password has NOT been found in known breaches.")

    print("\n*******************************************************************\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
