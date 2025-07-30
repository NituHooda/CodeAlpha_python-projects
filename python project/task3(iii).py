import requests
import re

url = input("Enter the full URL of the website: ").strip()

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad HTTP status
except Exception as e:
    print(f"❌ Failed to fetch the webpage: {e}")
    exit()

match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
if match:
    title = match.group(1)
    with open("web_title.txt", 'w') as f:
        f.write(f"Title: {title}")
    print(f"\n✅ Title extracted and saved: {title}")
else:
    print("❌ Could not find the <title> tag in the HTML.")

