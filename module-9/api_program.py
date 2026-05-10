#Megan Mosier
#CSD-325 Module 9
#API Program

import requests

API_URL = "https://catfact.ninja/facts?limit=6"

#Step 1: Test the Connection
print("=" * 60)
print("Step 1: Testing Connection to Cat Facts API")
print("=" * 60)

response = requests.get(API_URL)
print(f"URL:          {API_URL}")
print(f"Status Code: {response.status_code}")

#Step 2L Raw unformatted response
print()
print("=" * 60)
print("Step 2: Raw Response (no formatting)")
print("=" * 60)
print()
print(response.text)

#step 3: Formatted response
print()
print("=" * 60)
print("Step 3: Formatted Response")
print("=" * 60)

data = response.json()
facts = data['data']

print(f"Total facts available: {data['total']}")
print(f"Facts retrieved: {len(facts)}")
print()
print(f"{'#':<4} {'Cat Fact'}")
print("-" * 60)

for i, item in enumerate(facts, start=1):
    print(f"{i:<4} {item['fact']}")
    

