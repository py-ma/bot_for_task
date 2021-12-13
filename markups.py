from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

big = KeyboardButton('Большую')
small = KeyboardButton('Маленькую')
size_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(big, small)

cash = KeyboardButton('Наличными')
card = KeyboardButton('Картой')
pay_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(cash, card)

btn_repeat = KeyboardButton('Давай!')
repeatMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_repeat)

yes = KeyboardButton('Да')
no = KeyboardButton('Нет')
finalMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(yes, no)