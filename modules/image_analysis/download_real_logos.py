from icrawler.builtin import GoogleImageCrawler
import os

# --- Setup ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REAL_DIR = os.path.join(BASE_DIR, "images", "real")
os.makedirs(REAL_DIR, exist_ok=True)

# --- List of banks/companies ---
companies = ["SBI bank logo", "HDFC bank logo", "Kisan Vikas bank logo"]  # Add more

# --- Scraping ---
for company in companies:
    crawler = GoogleImageCrawler(storage={'root_dir': REAL_DIR})
    crawler.crawl(keyword=company, max_num=50)  # Download 50 images per company
