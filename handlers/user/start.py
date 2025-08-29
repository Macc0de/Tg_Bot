# Обработка сообщений user'а
from config.loader import storage, dp
from keyboards.user import main_keyboard
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from datetime import datetime

# Декоратор для /start
'''@dp.message_handler(commands="start")
# message(название переменной): Message(тип данных - custom)
async def handler(message: Message):
    # await(вызов функции асинхронной и ждет ответа функции)
    await message.answer(">>>Здравствуйте, я бот. Могу отсылать картинки.")
    # user= (идентификация user id, след. действия пользователя будет state), state="" (Комментарий для себя)
    await storage.set_state(user=message.from_user.id, state="Control")'''

current_date = datetime.now()  # Дата
day = current_date.day
month = current_date.month

def define_numerator():
    if month == 9 and ((1 <= day <= 7) or (29 <= day <= 30)):
        return "Числитель"
    elif month == 10 and ((1 <= day <= 5) or (13 <= day <= 19) or (27 <= day <= 31)):
        return "Числитель"
    elif month == 11 and ((1 <= day <= 2) or (10 <= day <= 16) or (24 <= day <= 30)):
        return "Числитель"
    elif month == 12 and ((8 <= day <= 14) or (22 <= day <= 28)):
        return "Числитель"

    elif 9 <= month <= 12 or (month == 12 and day > 28):
        return "Знаменатель"
    else:  # Каникулы
        return None


@dp.message_handler(commands="start")
# message(название переменной): Message(тип данных - custom)
async def handler(message: Message):
    await message.answer("👋👋", reply_markup=main_keyboard.get_buttons())
    await storage.set_state(user=message.from_user.id, state="Control")


# Обработчик Control
@dp.message_handler(state="Control")
async def control(message: Message, state: FSMContext):
    # await state.set_state("Control") - Разные декораторы

    weekdays = {
        0: 'Понедельник',
        1: 'Вторник',
        2: 'Среда',
        3: 'Четверг',
        4: 'Пятница',
        5: 'Суббота',
        6: 'Воскресенье'
    }
    weekday = current_date.weekday()
    today_weekday = weekdays[weekday]

    if message.text == "Авто ✅":  # Сам определяет параметры
        await message.answer(f"{day:02d}.{month:02d} - {today_weekday}")  # Дата

        if define_numerator() is None:
            await message.answer_animation("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGJxbmNweXhndXlrZHVhZ3Q"
                                           "1bnJqMTE3em5mbW5penlrbXNpb21jeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/"
                                           "cmruux5yjyy2VNdyt3/giphy.gif", caption="Каникулы... 🎉 🌅")
        elif weekday in [0, 6]:
            await message.answer_animation("https://cs4.pikabu.ru/post_img/2014/02/28/"
                                           "9/1393598295_1283013917.gif", caption="Сегодня отдыхаем 😎")
        elif today_weekday == "Вторник":
            await message.answer("1. (Пр)Методы оптимизации: Легков 301\n"
                                 "2. (Л)Методы оптимизации: Легков 301")
        elif today_weekday == "Среда":
            if define_numerator() == "Числитель":
                await message.answer("1.\n"
                                     "2. (Л)Теория автоматов: Кузьмин 220\n"
                                     "3. (Л)Рекурсивно-логическое пр-е: Башкин 224\n")
            elif define_numerator() == "Знаменатель":
                await message.answer("1.\n"
                                     "2. (Л)Теория автоматов: Кузьмин 220\n"
                                     "3. (Л)Рекурсивно-логическое пр-е: Башкин 224\n"
                                     "4. (Л)Рекурсивно-логическое пр-е: Башкин 224")
        elif today_weekday == "Четверг":
            if define_numerator() == "Числитель":
                await message.answer("1.\n"
                                     "2. (Пр)Huawei: Корсаков 201\n"
                                     "3.\n"
                                     "4. (Л)Нейронки: Сажин 204")
            elif define_numerator() == "Знаменатель":
                await message.answer("1. (Л)БЖД: Зеркалина 410-411\n"
                                     "2. (Пр)БЖД: Зеркалина 410-411\n"
                                     "3.\n"
                                     "4. (Л)Нейронки: Сажин 204")
        elif today_weekday == "Пятница":
            if define_numerator() == "Числитель":
                await message.answer("1. (Пр)Теория автоматов: Гладков 304\n"
                                     "2. (Л)Веб-приложения: Васильев 221\n"
                                     "3. (Пр)Веб-приложения: Васильев 221\n"
                                     "4. Физра")
            elif define_numerator() == "Знаменатель":
                await message.answer("1. (Пр)Теория автоматов: Гладков 304\n"
                                     "2. (Л)Huawei: Корсаков 201(312)\n"
                                     "3. (Пр)Веб-приложения: Васильев 221\n"
                                     "4. Физра")
        elif today_weekday == "Суббота":
            await message.answer("1. (Л)БД: Горбунов 216\n"
                                 "2. (Л)БД: Горбунов 216")

    elif message.text == "Вторник":  # Выбор юзера
        await message.answer("1. (Пр)Методы оптимизации: Легков 301\n"
                             "2. (Л)Методы оптимизации: Легков 301")
    elif message.text == "Среда":
        await message.answer("1.\n"
                             "2. (Л)Теория автоматов: Кузьмин 220\n"
                             "3. (Л)Рекурсивно-логическое пр-е: Башкин 224\n"
                             "4. 🔺\n"
                             "    🔹(Л)Рекурсивно-логическое пр-е: Башкин 224", parse_mode="HTML")
    elif message.text == "Четверг":
        await message.answer("1. 🔺\n"
                             "    🔹(Л)БЖД: Зеркалина 410-411\n"
                             "2. 🔺(Пр)Huawei: Корсаков 201\n"
                             "    🔹(Пр)БЖД: Зеркалина 410-411\n"
                             "3.\n"
                             "4. (Л)Нейронки: Сажин 204", parse_mode="HTML")
    elif message.text == "Пятница":
        await message.answer("1. (Пр)Теория автоматов: Гладков 304\n"
                             "2. 🔺(Л)Веб-приложения: Васильев 221\n"
                             "    🔹(Л)Huawei: Корсаков 201(312)\n"
                             "3. (Пр)Веб-приложения: Васильев 221\n"
                             "4. Физра", parse_mode="HTML")
    elif message.text == "Суббота":
        await message.answer("1. (Л)БД: Горбунов 216\n"
                             "2. (Л)БД: Горбунов 216")

    elif message.text == "Время пар 🕗":
        await message.answer("1️⃣  9:00 - 10:35\n" 
                             "2️⃣  10:45 - 12:20\n"
                             "3️⃣  13:20 - 14:55\n"
                             "4️⃣  15:05 - 16:40\n"
                             "5️⃣  16:50 - 18:25")

# Сразу сработает
# (lambda message: message.text.lower() == "собачка", state="Control")

# Декоратор для dog
'''@dp.message_handler(state="dog")
async def dogger(message: Message, state: FSMContext):  # Для возврата к Control
    if message.text.lower() == "собачка":
        await message.answer_photo(photo="https://terra.vet/wp-content/uploads/30-1.jpg")
        await state.set_state("Control")
@dp.message_handler(state="cat")
async def catter(message: Message, state: FSMContext):
    if message.text.lower() == "кошечка":
        await message.answer_photo(photo="https://icdn.lenta.ru/images/2022/02/22/12/20220222122412571/wide_4_3_f7a1fd0b424854c0415f2faa1efa1b93.jpeg")
        await state.set_state("Control")'''
