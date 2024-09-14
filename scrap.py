import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# URL target
url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# Mengirim permintaan HTTP GET
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Mencari semua produk buku
products = soup.find_all("article", class_="product_pod")

# List untuk menyimpan data
names = []
prices = []
ratings = []

# Pola untuk rating
rating_pattern = re.compile("star-rating")

# Fungsi untuk mengkonversi rating teks ke angka
def get_rating(txt):
    mapper = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    return mapper.get(txt, 0)

# Loop melalui setiap produk dan ekstrak data
for product in products:
    # Nama buku
    name = product.h3.a['title']
    # Harga buku
    price = product.find('p', class_='price_color').text.strip('£')
    # Rating buku
    rating_class = product.find('p', class_=rating_pattern)['class']
    rating = get_rating(rating_class[1])

    # Menambahkan data ke list
    names.append(name)
    prices.append(price)
    ratings.append(rating)

# Membuat DataFrame
df = pd.DataFrame({
    'Name': names,
    'Price (£)': prices,
    'Rating': ratings
})

# Menyimpan DataFrame ke file CSV
df.to_csv('travel_books.csv', index=False)
