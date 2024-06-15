from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, ApplicationBuilder

# Ваш токен від BotFather
TOKEN = '7065619833:AAF4R02qdkbDUnob7MZ-AUvxCxmTXH0uhTU'


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привіт! Я ваш бот.')

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Коля - 4149499393336498\n'
                                    'Владік - 5375414108754739\n'
                                    'Оксана - 4441114467237879\n'
                                    'Ваня - 4441114422324457')

async def all_command(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id == 726841637: #vanyk
        await update.message.reply_text(f'@M0001P1 @kkksenisss @liking_11')
    elif user_id == 774684968: #Kolia
        await update.message.reply_text(f'@Sqrt000000 @kkksenisss @liking_11')
    elif user_id == 774833269: # Vlad
        await update.message.reply_text(f'@M0001P1 @kkksenisss @Sqrt000000!')
    elif user_id == 543647642: #Oksana
        await update.message.reply_text(f'@M0001P1 @Sqrt000000 @liking_11')
    
        

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("card", help_command))
    application.add_handler(CommandHandler("all", all_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, all_command))

    application.run_polling()

if __name__ == '__main__':
    main()