import csv
import requests
from bs4 import BeautifulSoup

# URL to scrape
# Replace with the desired URL
url = "https://www.yellowpages.com.au/find/real-estate-agents/qld"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the phone number element using appropriate HTML tags or attributes
# Replace with the actual tag and attribute of the phone number element
phone_number = soup.find("span", class_="jsx-1031170495")

# Extract the text from the phone number element
phone_number_text = phone_number.get_text(
    strip=True) if phone_number else "Phone number not found"

# Create a CSV file and write the extracted phone number
csv_file = "phone_numbers.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Phone Number"])
    writer.writerow([phone_number_text])

print("Phone number extracted and saved to", csv_file)
