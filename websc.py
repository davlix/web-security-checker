import requests
from bs4 import BeautifulSoup
import re

def check_status_code(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        status_code = response.status_code

        if status_code == 200:
            print("Situs web aktif")
        else:
            print(f"Terjadi kesalahan, kode status: {status_code}")
    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat memeriksa status code:")
        print(e)

def check_security_headers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        headers = response.headers

        if 'strict-transport-security' in headers:
            print("HSTS header ditemukan")
            print(f"Nilai HSTS: {headers['strict-transport-security']}")
        else:
            print("HSTS header tidak ditemukan")

        if 'x-xss-protection' in headers:
            print("X-XSS-Protection header ditemukan")
            print(f"Nilai X-XSS-Protection: {headers['x-xss-protection']}")
        else:
            print("X-XSS-Protection header tidak ditemukan")
    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat memeriksa header keamanan:")
        print(e)

def check_robots_txt(url):
    try:
        robots_url = url + '/robots.txt'
        response = requests.get(robots_url)
        response.raise_for_status()

        if response.status_code == 200:
            print("File robots.txt ditemukan")
            print("Isi file robots.txt:")
            print(response.text)
        else:
            print("File robots.txt tidak ditemukan")
    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat memeriksa file robots.txt:")
        print(e)

# Fungsi untuk memeriksa adanya injeksi kode
def check_injection(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text

        if '<script>' in html:
            print("Potensi injeksi kode ditemukan")
        else:
            print("Tidak ditemukan potensi injeksi kode")

        # Contoh pemeriksaan injeksi SQL dengan menggunakan parameter binding/prepared statement
        sql_query = "SELECT * FROM users WHERE username = ?"
        username = "admin' OR '1'='1"
        results = execute_sql_query(sql_query, username)
        print("Hasil query SQL:", results)
    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat memeriksa potensi injeksi:")
        print(e)

def check_sensitive_files(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text

        sensitive_files = re.findall(r'\"((?:\.env|config|password|secret)[^\"\/]*)\"', html, re.IGNORECASE)
        
        if sensitive_files:
            print("File dan folder sensitif ditemukan:")
            for file in sensitive_files:
                print(file)
        else:
            print("Tidak ditemukan file dan folder sensitif")
    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat memeriksa file dan folder sensitif:")
        print(e)

def execute_sql_query(query, params):
    # Melakukan eksekusi query SQL dengan menggunakan parameter binding/prepared statement
    # Code untuk eksekusi query SQL di sini
    pass

def run_security_check():
    url = input("Masukkan URL yang ingin diperiksa: ")

    print("\nMemeriksa status code:")
    check_status_code(url)

    print("\nMemeriksa header keamanan:")
    check_security_headers(url)

    print("\nMemeriksa file robots.txt:")
    check_robots_txt(url)

    print("\nMemeriksa potensi injeksi:")
    check_injection(url)

    print("\nMemeriksa file dan folder sensitif:")
    check_sensitive_files(url)
run_security_check()
