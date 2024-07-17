from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Fungsi untuk memulai bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Halo! Saya adalah bot Anda.')

# Fungsi utama untuk menjalankan bot
def main() -> None:
    # Masukkan token API bot Anda di sini
    updater = Updater("6941029048:AAF7pY1UATX-C8idB9CHnsCr4naM8qmNiVE")

    dispatcher = updater.dispatcher

    # Daftarkan handler untuk perintah /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Mulai polling
    updater.start_polling()

    # Jalankan bot sampai diberhentikan
    updater.idle()

if __name__ == '__main__':
    main()
