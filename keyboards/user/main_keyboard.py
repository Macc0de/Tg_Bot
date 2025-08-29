from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


'''def get_main_buttons():
    return ReplyKeyboardMarkup(resize_keyboard=True).add("Цельсий", "Фаренгейт")'''


'''def get_cancel_button():
    return ReplyKeyboardMarkup(resize_keyboard=True).add("Отмена  ❌")'''


def get_buttons():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row("Авто ✅")
    keyboard.row("Вторник", "Среда", "Четверг")
    keyboard.row("Пятница", "Суббота")
    keyboard.row("Время пар 🕗")
    return keyboard

    #return ReplyKeyboardMarkup(resize_keyboard=True).add("Вторник", "Среда", "Четверг",
                                                         #"Пятница", "Суббота")
