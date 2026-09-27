import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Load token from Railway environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables!")

bot = telebot.TeleBot(BOT_TOKEN)

# --- Keyboard Setup ---
def get_main_keyboard():
    """Creates a persistent reply keyboard for the bot."""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        KeyboardButton("🛍️ Discover Products"),
        KeyboardButton("⚙️ Explore Services"),
        KeyboardButton("🛠️ Useful Tools"),
        KeyboardButton("ℹ️ Help")
    ]
    markup.add(*buttons)
    return markup

# --- Command Handlers ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Handles /start and /help commands."""
    welcome_text = (
        f"👋 Welcome to **CommerceXBot**, {message.from_user.first_name}!\n\n"
        "I'm designed to make online commerce easier. Here’s what I can do:\n\n"
        "🔹 **Discover Products** - Find new items.\n"
        "🔹 **Explore Services** - Check out available services.\n"
        "🔹 **Useful Tools** - Access everyday digital commerce tools.\n\n"
        "Select an option from the menu below to get started."
    )
    bot.send_message(
        message.chat.id, 
        welcome_text, 
        parse_mode='Markdown', 
        reply_markup=get_main_keyboard()
    )

# --- Message Handlers for Menu Buttons ---
@bot.message_handler(func=lambda message: message.text == "🛍️ Discover Products")
def discover_products(message):
    bot.reply_to(message, "🔍 **Product Discovery**\n\nThis section will help you find products. (Feature coming soon!)", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "⚙️ Explore Services")
def explore_services(message):
    bot.reply_to(message, "⚙️ **Service Exploration**\n\nThis section will list available services. (Feature coming soon!)", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "🛠️ Useful Tools")
def useful_tools(message):
    bot.reply_to(message, "🛠️ **Useful Tools**\n\nThis section will provide handy digital commerce tools. (Feature coming soon!)", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "ℹ️ Help")
def help_command(message):
    send_welcome(message)

# --- Fallback Handler ---
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Handles any other text."""
    bot.reply_to(message, "I'm not sure what you mean. Please use the menu buttons or type /help.")

# --- Start Polling ---
if __name__ == '__main__':
    print("CommerceXBot is starting...")
    bot.infinity_polling()
