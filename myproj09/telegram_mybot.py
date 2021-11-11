import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tasks

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    print("TELEGRAM_TOKEN 환경변수를 지정해주세요.", file=sys.stderr)
    sys.exit(1)  # 종료 상태값을 1로 지정하고, 프로그램 종료

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    """
    대화방이 처음 열리면, 자동으로 호출되는 함수.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="안녕. 나는 bot이야. 만나서 반가워.")

def echo(update, context):
    received_text: str = update.message.text
    reply_text = received_text

    if tasks.ya.check_available(received_text):
        response_text = tasks.ya.make_response(received_text)
    elif tasks.naver_search.check_available(received_text):
        response_text = tasks.naver_search.make_response(received_text)
    else:
        response_text = "지원하지 않는 명령입니다."

    # if received_text == "야":
    #     reply_text = "왜?"
    # elif received_text.startswith("네이버 검색:"):
    #     query = received_text[7:]
    #     post_list = tasks.naver_search(query)
    #     # TODO: 응답 문자열을 생성하셔야 합니다.
    #     reply_text = ""
    #     for post in post_list:
    #         reply_text += post["title"] + "\n"
    # else:
    #     reply_text = "지원하는 명령이니다."


    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response_text)

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(
    Filters.text & (~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)

updater.start_polling()

# bot = telegram.Bot(token)

# info = bot.getMe()
# pprint.pprint(info)

# resp = bot.getUpdates()
# # pprint.pprint(resp)

# chat_id = 209552441
# bot.sendMessage(chat_id=chat_id, text="안녕. 나는 봇이야")