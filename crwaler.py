import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input("Enter the url:").strip()
if not url:
    print("No URL provided.")
    sys.exit(1)

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.RequestException as exc:
    print(f"Error fetching {url}: {exc}")
    sys.exit(1)

soup = BeautifulSoup(response.text, 'html.parser')
forms = soup.find_all('form')

if not forms:
    print("No forms found on the page.")
    sys.exit(0)

for form in forms:
    token = False
    for input_tag in form.find_all('input', type='hidden'):
        name = input_tag.get('name', '').lower()
        if 'csrf' in name or 'token' in name or 'authenticity' in name:
            token = True
            break

    if not token:
        action = form.get('action', url)
        full_url = urljoin(url, action)
        method = form.get('method', 'GET').upper()
        print(f"Vulnerable: {full_url} with method {method}")
    else:
        print(f"Secure: {form.get('action', 'form')}")

