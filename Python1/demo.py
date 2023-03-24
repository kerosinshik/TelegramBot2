import lib
import sys
import requests

print(lib.even(3))

print(sys.path)

result = requests.get('https://www.google.com/')

print(result.content)