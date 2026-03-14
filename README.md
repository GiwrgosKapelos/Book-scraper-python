# 📚 Book Scraper to Excel/CSV

A Python-based web scraper that extracts book data from `books.toscrape.com`. It collects titles, prices, and ratings across multiple pages and exports them into clean, structured formats.

## ✨ Features

- **Multi-page Scraping:** Iterates through the first 5 pages of the catalog.
- **Data Transformation:**
  - Converts text ratings (e.g., "Three") into numeric values (3).
  - Cleans price strings and converts them to floats for analysis.
- **Dual Export:** Saves data in both **CSV** (UTF-8) and **Excel (.xlsx)** formats.
- **Ethical Scraping:** Includes a 1-second delay between requests to respect server resources.

## 🛠️ Technologies Used

- [Python 3.x](https://www.python.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) (Parsing HTML)
- [Pandas](https://pandas.pydata.org/) (Data Manipulation)
- [Requests](https://requests.readthedocs.io/) (HTTP Requests)
- [Openpyxl](https://openpyxl.readthedocs.io/) (Excel Engine)

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/book-scraper-python.git](https://github.com/YOUR_USERNAME/book-scraper-python.git)
   cd book-scraper-python
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script:**
   ```bash
   python scraper.py
   ```

## 📊 Sample Output

The generated files will contain the following columns:
| Title | Price | Rating |
| :--- | :--- | :--- |
| A Light in the Attic | 51.77 | 3 |
| Tipping the Velvet | 53.74 | 1 |

---

Disclaimer: This project is for educational purposes only.
