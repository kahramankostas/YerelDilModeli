import requests

API_URL = "http://127.0.0.1:5000/api/chat"

user_input = input("Yerel Model'e ne sormak istersin? ")

payload = {
    "text": user_input
}

try:
    response = requests.post(API_URL, json=payload, timeout=10)

    if response.status_code == 200:
        data = response.json()
        print("\nYerel Model'in cevabı:")
        print(data.get("response", "Yanıt bulunamadı."))
    else:
        print("API Hatası:", response.status_code)
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Bağlantı hatası:", str(e))