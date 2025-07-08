import requests
import datetime
import os

message = "ㅈㅇㅇㅊㅇㄴㄷ"

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)

# 현재 시간 문자열
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 결과 메시지 작성
if response.status_code == 200:
    log_message = f"[{now}] ✅ SEND MESSAGE SUCCESS  : '{message}'"
else:
    log_message = f"[{now}] ❌ SEND MESSAGE FAILED   : {response.text}"

# log.txt에 append (누적 기록)
with open("log.txt", "a", encoding="utf-8") as log_file:
    log_file.write(log_message + "\n")