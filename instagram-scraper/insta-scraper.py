
# REF:
# https://www.youtube.com/watch?v=L2CxFhkZrss
import requests
from bs4 import BeautifulSoup

instagram_url = "https://www.instagram.com"
profile_url = "ezomola"
response = requests.get(f"{instagram_url}/{profile_url}")
print(response.status_code)
if response.ok:
    html = response.text
    bs_html = BeautifulSoup(html)
    # print(response.text)
    # print(scripts[5:])
    # scripts = bs_html.select('script[type="application/json"]')
    # scripts = bs_html.select("script")
    print(bs_html)
    # print(scripts)
    print(len(scripts))