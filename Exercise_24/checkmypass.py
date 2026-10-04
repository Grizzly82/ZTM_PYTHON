import hashlib
import re

import requests
import sys




""" def convert_to_sha1(user_password):
    # Convert password to SHA1 hash
    sha1password = hashlib.sha1(user_password.encode('utf-8')).hexdigest().upper()
    return sha1password
 """

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again.")
    return res

def get_password_leaks_count(hashes, hash_to_check):
    # Check if the password hash exists in the API response
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def read_response(response):
    # Read the API response and return the hashes
    return (line.split(':') for line in response.text.splitlines())


def pawned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    hashes = read_response(response)
    return get_password_leaks_count(hashes, tail)

def main(args):
    user_password = input("Enter your password to check if it has been compromised: ")
    # converted_password = convert_to_sha1(user_password)
    # print(f"Your password in SHA1 format is: {converted_password}")
    
    check = pawned_api_check(user_password)
    print("*******************************************************************\n")
    if check:
        print(f"Your password has been compromised {check} times. You should change your password immediately.")
    else:
        print("Your password has not been compromised. You are safe!")
    
    print("\n*******************************************************************\n")
    return 'done'

if __name__ == '__main__':
    main(sys.argv[1:])