#Megan Mosier
#CSD-325 Module 9

import requests
import json

#step 1: Testing Connection")
print("=" * 50)
print("Step 1: Testing Connection")
print("=" * 50)

response = requests.get('http://www.google.com')
print(f"Status Code: {response.status_code}")

#Step 2: Astronaut API - Raw Response
print()
print("=" * 50)
print("Step 2: Astronaut API - Raw Response")
print("=" * 50)

astro_url = "http://api.open-notify.org/astros.json"
response = requests.get(astro_url)
print(response.text)

#Step 3L Formatted Output
print()
print("=" * 50)
print("Step 3: Formatted Output")
print("=" * 50)

data = response.json()

print(f"Number of people in space: {data['number']}")
print()
print(f"{'Name':<30} {'Craft':<15}")
print("-" * 45)

for astronaut in data['people']:
    print(f"{astronaut['name']:<30} {astronaut['craft']:<15}")

