# pip install pyshorteners

import pyshorteners
import pyshorteners.shorteners

long_url = input("Enter the URL:")

type_tiny = pyshorteners.Shortener()

short_url = type_tiny.tinyurl.short(long_url)

print(f"The shortened URL is : {short_url}")