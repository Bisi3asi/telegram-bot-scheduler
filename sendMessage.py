import requests
import os

message = "ㅈㅇㅇㅊㅇㄴㄷ"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)
print("전송 완료" if response.status_code == 200 else f"에러: {response.text}")