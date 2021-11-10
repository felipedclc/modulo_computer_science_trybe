import requests
# import time


url = "https://www.cloudflare.com/rate-limit-test/"
# url = "https://www.globo.com/"

for _ in range(12):  # mais de 10 aparece 429
    response = requests.get(url)
    print(response.status_code)
    # time.sleep(6)

try:
    # definindo o tempo máximo de espera para a requisição
    response = requests.get("http://httpbin.org/delay/10", timeout=2)
except requests.ReadTimeout:
    response = requests.get("http://httpbin.org/delay/10", timeout=15)
finally:
    print(response.status_code)
