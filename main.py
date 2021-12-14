from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils import executor
from states import *
import markups as m
import time
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)
ORDER_DATA = {}

# -----------------------------------------START--------------------------------------------------
@dp.message_handler(commands=['start'], state=None)
async def start(message: types.Message):
    s.t1()
    await bot.send_message(message.from_user.id, "Привет!\nКакую ты хочешь пиццу?")
    ORDER_DATA[str(message.from_user.id)] = {}
    return await choose_size(message)


# -----------------------------------------message_handler--------------------------------------------------
@dp.message_handler()
async def waiting_yes(message: types.Message):
    if message.text in ('Большую', 'Маленькую'):
        s.t3()
        ORDER_DATA[str(message.from_user.id)]['size'] = message.text
        return await choose_pay_method(message)

    elif message.text in ('Наличными', 'Картой'):
        ORDER_DATA[str(message.from_user.id)]['pay'] = message.text
        return await repeating_order(message)

    elif message.text == 'Да':
        s.t5()
        return await finish(message)

    elif message.text == 'Нет':
        s.tn()
        await bot.send_message(message.from_user.id, 'Ну что же, давай по-новой')
        return await choose_size(message)


# -----------------------------------------SIZE---------------------------------------------------
async def choose_size(message: types.Message):
    s.t2()
    return await bot.send_message(message.from_user.id, 'Выбери размер',
                                  reply_markup=m.size_menu)


# -----------------------------------------PAY----------------------------------------------------
async def choose_pay_method(message: types.Message):
    s.t4()
    return await bot.send_message(message.from_user.id, 'Выбери способ оплаты',
                                  reply_markup=m.pay_menu)


# --------------------------REPEATING AND WAITING YES---------------------------------------------
async def repeating_order(message: types.Message):
    size = ORDER_DATA[str(message.from_user.id)]['size'].lower()
    pay = ORDER_DATA[str(message.from_user.id)]['pay'].lower()
    return await bot.send_message(message.from_user.id,
                                      f'Вы хотите {size} пиццу, оплата - {pay}?',
                                      reply_markup=m.finalMenu)


# -------------------------------------FINISH-----------------------------------------------------
@dp.message_handler()
async def finish(message: types.Message):
    s.t6()
    final_menu = ReplyKeyboardRemove()
    return await bot.send_message(message.from_user.id, 'Спасибо за заказ!', reply_markup=final_menu)


if __name__ == '__main__':
    executor.start_polling(dp)