from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

API_TOKEN = '5969561500:AAEXVNTYISSVjDlv6Wostb_7-cuSwFp2cUY'

# Configure logging


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'boshlash'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom botga hush kelibsiz")



@dp.message_handler(Text(endswith=['salom','assalomu aleykum','Salom']))
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply('yaxshimisiz!')

@dp.message_handler(Text(endswith=['ha','yoq','albatta']))
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply('tanishsak boladimi! \n /Yes \n /No')


@dp.message_handler(Text(endswith=['Yes','Okay','No']))
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply('ismingizni yozib qoldiring!')

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply(f'{message.text} tanishganimdan hursandman')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
