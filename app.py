from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('5kQpaioC9HTymyysrMALpcb6IJ5nHTuRhFQPgSuohKDE7ab2TxxlDiV4ELBvZqMhLi5ET6xCQVX4wLI1ihPTxYPeLtGIGij++Eljyi3G8AdnnXCOWMMyibJzlC0K8HfeSFquGmtvVz9hMKoKMFzSmAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('566551dc7e730127a19e0943e13045f5')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    hi = "hi" or "測試你好" or "你好"
    r = "那個……請問你在說什麼？"

    if msg == hi:
        r = "朋友你好，我是測試機器人"
    elif msg == "你吃飽沒"
        r = "我吃飽了!因為我有剛剛你的支持!"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= r))


if __name__ == "__main__":
    app.run()