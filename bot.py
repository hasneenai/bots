import telebot
import speedtest

# ضع توكن البوت هنا مباشرة
BOT_TOKEN = "6669548638:AAHTn7VWenpMEqYHYHK6ULYPnWK0wvBfSY0"  # <-- استبدل هذا بتوكن البوت الحقيقي
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_speedtest(message):
    bot.reply_to(message, "🚀 جاري قياس سرعة الإنترنت... انتظر قليلاً")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Mbps
        upload_speed = st.upload() / 1_000_000      # Mbps
        ping = st.results.ping

        result = (
            f"✅ نتيجة اختبار السرعة:\n\n"
            f"📥 تحميل: {download_speed:.2f} Mbps\n"
            f"📤 رفع: {upload_speed:.2f} Mbps\n"
            f"📡 Ping: {ping} ms"
        )
        bot.send_message(message.chat.id, result)

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ حدث خطأ أثناء القياس: {e}")

print("🤖 Bot is running...")
bot.infinity_polling()
