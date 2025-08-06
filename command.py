import random
import datetime
import pytz
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# .env 로부터 토큰 불러오기
load_dotenv(dotenv_path='botToken.env')
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 유저 호출 횟수 저장
user_call_count = {}

# 한국 시간대
KST = pytz.timezone("Asia/Seoul")
last_reset_date = datetime.datetime.now(KST).date()

# 점심 메뉴 리스트
menus = [
    "제육볶음", "김치찌개", "해장국", "들기름막국수", "닭볶음탕", "중국집",
    "생선구이", "돈까스", "칼국수", "콩국수", "텐동", "우동", "분식",
    "물회", "회덮밥", "초밥", "대구탕", "매운탕"
]

# /lunch 명령어 핸들러
async def send_lunch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_reset_date

    user_id = update.effective_user.id
    now_kst = datetime.datetime.now(KST)
    today = now_kst.date()

    # 날짜 변경 시 카운트 초기화
    if today != last_reset_date:
        user_call_count.clear()
        last_reset_date = today

    count = user_call_count.get(user_id, 0) + 1
    user_call_count[user_id] = count

    # 호출 로그 출력
    print(f"id: {user_id}, count: {count}")

    if count <= 3:
        menu = random.choice(menus)
        reply = f"오늘 점심은 {menu} 어떠신가요?"
    else:
        reply = "본인 드시고 싶은거 드십쇼"

    await update.message.reply_text(reply)

# 실행 함수
def main():
    print("===============telegram bot initialized==================")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("lunch", send_lunch))
    app.run_polling()

if __name__ == "__main__":
    main()
