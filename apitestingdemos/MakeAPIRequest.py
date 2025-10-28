import requests

res = requests.get("https://www.google.com")
print(res)
print(res.cookies)
print(res.url)
print(res.status_code)
print(res.text)