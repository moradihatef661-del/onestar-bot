import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8298497092:AAEDCwGLqdXXgz11FaJpgCGDwUpgYonUyFM"
ADMIN_ID = 5130532161

bot = telebot.TeleBot(TOKEN)

support_users = {}

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("⭐ استارز", "👑 پرمیوم")
    markup.add("📱 شماره مجازی", "⚙️ کانفیگ")
    markup.add("🏆 تورنمنت", "🛒 سبد خرید")
    markup.add("🆘 پشتیبانی")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    text = f"""
سلام {name} 👋
✨ به ربات وان استار خوش اومدی

از منوی زیر یکی از خدمات رو انتخاب کن 👇
"""
    bot.send_message(message.chat.id, text, reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "🆘 پشتیبانی")
def support(message):
    bot.send_message(message.chat.id, "✉️ مشکلت رو بنویس، پشتیبانی جواب میده")
    support_users[message.chat.id] = True

@bot.message_handler(func=lambda m: m.chat.id in support_users and m.chat.id != ADMIN_ID)
def send_to_admin(message):
    user_id = message.chat.id
    text = f"📩 پیام جدید از {user_id}:\n{message.text}"
    bot.send_message(ADMIN_ID, text)

@bot.message_handler(func=lambda m: m.chat.id == ADMIN_ID and m.reply_to_message)
def reply_to_user(message):
    try:
        user_id = int(message.reply_to_message.text.split()[4].replace(":", ""))
        bot.send_message(user_id, f"📨 پاسخ پشتیبانی:\n{message.text}")
    except:
        pass

@bot.message_handler(func=lambda m: True)
def other(message):
    bot.send_message(message.chat.id, "از منو انتخاب کن 👇", reply_markup=main_menu())

print("ربات روشن شد 🚀")
bot.infinity_polling()
