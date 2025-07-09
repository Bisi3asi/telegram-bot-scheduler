import requests
import datetime
import os
import pytz

dailyMessage = "ㅈㅇㅇㅊㅇㄴㄷ~"
fridayMessage = "ㅈㅇㄱㅇㅇㅇㄴㄷ~"

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# 로컬 시간대 설정
kst = pytz.timezone("Asia/Seoul")
now_kst = datetime.datetime.now(kst)

if now_kst.weekday() == 4:
    message = fridayMessage
else :
    message = dailyMessage

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}
response = requests.post(url, data=payload)

now_str = now_kst.strftime("%Y-%m-%d %H:%M:%S")

# 결과 메시지 작성
if response.status_code == 200:
    log_message = f"[{now_str}] ✅ SEND MESSAGE SUCCESS  : '{message}'"
else:
    log_message = f"[{now_str}] ❌ SEND MESSAGE FAILED   : {response.text}"

# log.txt에 append (누적 기록)
with open("log.txt", "a", encoding="utf-8") as log_file:
    log_file.write(log_message + "\n")