import hashlib
import requests
import tkinter as tk
from tkinter import ttk

def request_api_data(prefix):
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url, timeout=5)
    res.raise_for_status()
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

def check_password():
    password = entry.get()
    if not password:
        result_label.config(text="Password cannot be empty.", foreground="orange")
        return

    try:
        count = pawned_api_check(password)
        if count:
            result_label.config(
                text=f"⚠️ Password compromised {count} times!",
                foreground="red"
            )
        else:
            result_label.config(
                text="✔ Password not found in known breaches.",
                foreground="green"
            )
    except Exception as e:
        result_label.config(text=f"Error: {e}", foreground="red")

# GUI Setup
root = tk.Tk()
root.title("Password Breach Checker")
root.geometry("420x200")

title_label = ttk.Label(root, text="Password Breach Checker", font=("Arial", 16))
title_label.pack(pady=10)

entry = ttk.Entry(root, width=40, show="*")
entry.pack(pady=5)

check_button = ttk.Button(root, text="Check Password", command=check_password)
check_button.pack(pady=10)

result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
