from aiogram import Bot,Dispatcher,executor,types
import random
import key
token= "910085890:AAFUfyg5RxHPAIWMD8DQBXf-OcLayvjDfu0"
bot=Bot(token)
dp=Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    key.bombPlace= random.randint(1, 9)
    key.start()
    await bot.send_message(text="Выберите ячейку",chat_id=message.from_user.id, reply_markup=key.kb)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def choice(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if int(code)==int(key.bombPlace):
        key.list_btn[int(code)-1].text = key.bomb
        await bot.send_message(text="Вы попали на бомбу", chat_id=callback_query.from_user.id, reply_markup=key.kb)
    else:
        key.list_btn[int(code)-1].text = key.cross
        await bot.send_message(text="Повезло", chat_id=callback_query.from_user.id, reply_markup=key.kb)




if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)