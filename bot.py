import telebot
from flask import Flask, request, jsonify

# 🛑 HARD-CODED BOT CREDENTIALS (SECURITY RISK - DO NOT SHARE!)
TOKEN = "7879598325:AAFRhrWVUanbI3gxEb4W6Bm1GroQTudgZUQ"
CHAT_ID = "-1002262089486"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Flask Route to Keep the App Alive
@app.route("/")
def home():
    return "Bot is running! 🚀"

# Store user data from Telegram login
@app.route("/store_user_data", methods=["GET"])
def store_user_data():
    user_id = request.args.get("id")
    username = request.args.get("username")
    
    if user_id:
        bot.send_message(CHAT_ID, f"✅ Verified User: {username} (ID: {user_id})")
        return jsonify({"status": "success", "user": username})
    return jsonify({"status": "error", "message": "No user ID"})

# Bot command to send Web App button
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton(
        "🚀 Launch Web App", url="https://your-vercel-webapp.vercel.app"
    )
    markup.add(btn)
    bot.send_message(message.chat.id, "Click below to verify:", reply_markup=markup)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Render requires a running server
