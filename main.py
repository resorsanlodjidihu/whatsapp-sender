import os
import requests
import json
import sys

# Məlumatları GitHub Secrets üzərindən təhlükəsiz çəkirik
ID_INSTANCE = os.getenv("GREEN_API_ID")
API_TOKEN_INSTANCE = os.getenv("GREEN_API_TOKEN")
CHAT_ID = os.getenv("DOSTUN_NUMRASI") 

if not ID_INSTANCE or not API_TOKEN_INSTANCE or not CHAT_ID:
    print("Xəta: GitHub Secrets ayarları əskikdir!")
    sys.exit(1)

# Sizin GitHub istifadəçi adınıza uyğun birbaşa video linki
VIDEO_URL = "https://githubusercontent.com" 
FILE_NAME = "shtibididom.mp4"
CAPTION = "Ştibididom dop dop yes yes! Gecən xeyrə, Səfər!"

# Videonun WhatsApp-da birbaşa görünməsi üçün sendMediaByUrl istifadə edirik
url = f"https://green-api.com{ID_INSTANCE}/sendMediaByUrl/{API_TOKEN_INSTANCE}"

payload = {
    "chatId": CHAT_ID,
    "urlFile": VIDEO_URL,
    "fileName": FILE_NAME,
    "caption": CAPTION
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print("Video (görünüşü ilə birlikdə) uğurla göndərildi!")
else:
    print(f"Göndəriş uğursuz oldu: {response.text}")
