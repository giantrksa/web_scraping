# Web Scraping Assignment

## Tujuan

Proyek ini bertujuan untuk mengekstrak data buku dari kategori "Travel" pada situs [Books to Scrape](https://books.toscrape.com/), menggunakan Python dan BeautifulSoup.

## Proses

- Mengirim permintaan HTTP GET ke halaman target.
- Mem-parsing konten HTML dengan BeautifulSoup.
- Mengekstrak nama buku, harga, dan rating.
- Menyimpan data yang diekstrak ke dalam file CSV.

## Hasil

File `travel_books.csv` berisi data buku-buku dalam kategori "Travel", termasuk:

- **Name**: Nama buku
- **Price (£)**: Harga buku
- **Rating**: Rating buku (1-5)

## Cara Menjalankan

1. Pastikan Python dan pustaka berikut sudah terinstall:
   - `requests`
   - `beautifulsoup4`
   - `pandas`

2. Jalankan script:

   ```bash
   python scrape_books.py
