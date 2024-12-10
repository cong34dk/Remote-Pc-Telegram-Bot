import telebot
import os
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton  
from commands import capture_screenshot, shutdown, restart, get_system_status, open_app

# Load biến môi trường từ file .env
load_dotenv()

# Lấy TELEGRAM Token từ biến môi trường
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN không được tìm thấy trong file .env")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Lệnh /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message, 
        "Chào bạn! Tôi là bot điều khiển máy tính.\nCác lệnh:\n"
        "/screenshot - Chụp màn hình\n"
        "/shutdown - Tắt máy tính\n"
        "/restart - Khởi động lại máy tính\n"
        "/status - Xem trạng thái hệ thống\n"
        "/openapp - Mở ứng dụng"
    )

# Lệnh chụp màn hình
@bot.message_handler(commands=["screenshot"])
def screenshot(message):
    screenshot_path = capture_screenshot()
    with open(screenshot_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)

# Lệnh tắt máy tính
@bot.message_handler(commands=["shutdown"])
def shutdown_pc(message):
    bot.reply_to(message, shutdown())

# Lệnh khởi động lại máy tính
@bot.message_handler(commands=["restart"])
def restart_pc(message):
    bot.reply_to(message, restart())

# Lệnh kiểm tra trạng thái hệ thống
@bot.message_handler(commands=["status"])
def status(message):
    bot.reply_to(message, get_system_status())

# # Lệnh mở ứng dụng
@bot.message_handler(commands=["openapp"])
def openapp_command(message):
    # Danh sách các app có thể mở
    apps = ["Notepad", "Calculator", "Chrome", "File Explorer"]

    # Tạo inline keyboard
    markup = InlineKeyboardMarkup()
    for app in apps:
        markup.add(InlineKeyboardButton(app, callback_data=f"open_{app}"))

    bot.reply_to(message, "Chọn ứng dụng bạn muốn mở:", reply_markup=markup)

# Xử lý khi người dùng chọn app
@bot.callback_query_handler(func=lambda call: call.data.startswith("open_"))
def handle_openapp_callback(call):
    app_name = call.data.split("_")[1]  # Lấy tên app từ callback_data
    response = open_app(app_name)  # Gọi hàm mở app
    bot.send_message(call.message.chat.id, response)  # Trả lời người dùng

# Chạy bot
try:
    print("Bot đang chạy...")
    bot.polling()
except Exception as e:
    print(f"Lỗi khi chạy bot: {e}")
