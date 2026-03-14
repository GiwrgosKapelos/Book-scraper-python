import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# --- CONFIGURATION ---
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

all_books = []
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# --- MAIN SCRAPING LOOP ---
for page in range(1, 6):
    print(f"Scraping page {page}...")
    current_url = base_url.format(page)

    try:
        response = requests.get(current_url, timeout=10)
        response.raise_for_status()  # Automatically raises an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price_raw = book.find('p', class_='price_color').text

        star_tag = book.find('p', class_='star-rating')
        rating_word = star_tag.get('class')[1]
        rating_number = rating_map.get(rating_word, 0)

        all_books.append({
            'Title': title,
            'Price': price_raw,
            'Rating': rating_number
        })

    time.sleep(1)

# --- DATA PROCESSING ---
df = pd.DataFrame(all_books)

# Clean Price: Remove non-numeric characters and convert to float
df['Price'] = df['Price'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# --- EXPORT ---

# 1. Export to CSV (Standard)
df.to_csv('all_books_results.csv', index=False, encoding='utf-8-sig')

# 2. Export to Excel (Requires openpyxl)
# Excel files handle formatting and data types better than CSVs
excel_file = 'all_books_results.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

print("-" * 30)
print(f"Success! Processed {len(df)} books.")
print(f"Files saved: 'all_books_results.csv' and '{excel_file}'")
