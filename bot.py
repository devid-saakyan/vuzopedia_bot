from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.exceptions import MessageTextIsEmpty
from parser import get_vuzi
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

token = os.environ.get('TOKEN')
bot = Bot(token = token)
dp = Dispatcher(bot, storage=MemoryStorage())

dict_of_number = {'Майкоп': 1, 'Барнаул': 2, 'Выбратьгород': 111, 'Благовещенск': 4, 'Архангельск': 5, 'Астрахань': 7,
                  'Уфа': 8, 'Стерлитамак': 9, 'Белорецк': 10, 'Белгород': 11, 'Старый Оскол': 12, 'Брянск': 13,
                  'Улан-Удэ': 14, 'Владимир': 15, 'Волгоград': 16, 'Вологда': 17, 'Череповец': 18, 'Воронеж': 19,
                  'Махачкала': 20, 'Биробиджан': 21, 'Чита': 22, 'Иваново': 23, 'Иркутск': 25, 'Калининград': 27,
                  'Калуга': 28, 'Обнинск': 29, 'Петропавловск-Камчатский': 30, 'Черкесск': 31, 'Петрозаводск': 33,
                  'Кемерово': 34, 'Киров': 35, 'Кирово-Чепецк': 36, 'Сыктывкар': 37, 'Ухта': 38, 'Краснодар': 40,
                  'Сочи': 41, 'Новороссийск': 42, 'Анапа': 43, 'Геленджик': 44, 'Красноярск': 45, 'Железногорск': 46,
                  'Норильск': 47, 'Курган': 48, 'Курск': 49, 'Санкт-Петербург': 50, 'Выборг': 51, 'Сосновый Бор': 52,
                  'Липецк': 53, 'Елец': 54, 'Магадан': 55, 'Саранск': 58, 'Москва': 59, 'Серпухов': 60, 'Электросталь': 61,
                  'Дмитров': 62, 'Подольск': 63, 'Балашиха': 64, 'Химки': 65, 'Мурманск': 66, 'Нижний Новгород': 67,
                  'Великий Новгород': 68, 'Новосибирск': 69, 'Омск': 70, 'Оренбург': 71, 'Орск': 72, 'Орел': 73, 'Пенза': 74,
                  'Пермь': 75, 'Владивосток': 76, 'Псков': 77, 'Ростов-на-Дону': 78, 'Таганрог': 79, 'Рязань': 80, 'Самара': 81,
                  'Тольятти': 82, 'Екатеринбург': 83, 'Нижний Тагил': 84, 'Каменск-Уральск': 85, 'Саратов': 86, 'Якутск': 87,
                  'Южно-Сахалинск': 88, 'Владикавказ': 89, 'Смоленск': 90, 'Ставрополь': 91, 'Пятигорск': 92, 'Кисловодск': 93,
                  'Ессентуки': 94, 'Тамбов': 95, 'Мичуринск': 96, 'Казань': 98, 'Набережные Челны': 99, 'Альметьевск': 100,
                  'Нижнекамск': 101, 'Елабуга': 102, 'Тверь': 103, 'Конаково': 104, 'Ржев': 105, 'Вышний Волочек': 106,

                  'Томск': 107, 'Тула': 109, 'Новомосковск': 110, 'Нижневартовск': 112, 'Сургут': 113, 'Тюмень': 114, 'Ханты-Мансийск': 115}
dict_of_subjects = {'Информатика': 'inform', 'Математика': 'mat', 'Физика': 'fiz', 'Обществознание':'obshe', 'История': 'ist',
                    'Биология': 'biol', 'Химия': 'him', 'Литература': 'liter', 'География': 'georg', 'Иностранныйязык': 'inyaz',
                    'Русскийязык': 'rus', 'Русский': 'rus'}

class States(StatesGroup):
    state1 = State()
    state2 = State()
    state3 = State()
    state4 = State()
    state5 = State()
    state6 = State()

@dp.message_handler(commands = ['start', 'Veronika'])
async def say_hello(message: types.Message):
    await message.answer('Приветствую, уважемый {}'.format(message.from_user.username))
    await message.answer('Хотите ли вы выбрать вуз по результатам ЕГЭ?', reply_markup=keyboard1())


@dp.message_handler(content_types=['text'])
async def say_city(message: types.Message):
    if message.text == 'Да':
        await message.answer('Введите город в который хотите поступать')
        await States.state1.set()
    elif message.text == 'Нет':
        await message.answer('Ждём тебя снова')

# @dp.message_handler(content_types=['text'])
# async def say_answer(message: types.Message):
#     if message.text == 'Да':
#         await message.answer('Отправьте результаты ваших экзаменов в одном сообщении  в таком формате\n'
#                              'Информатика - 68\nМатематика - 56\nОбществознание - 87')
#         await States.state1.set()
#     elif message.text == 'Нет':
#         await message.answer('Пока друг')

@dp.message_handler(state = States.state1)
async def say_subjects(message: types.Message):
    text = message.text
    global city
    if str(text).title() in dict_of_number:
        city = str(text).title()
        await message.answer('Отправьте результаты ваших экзаменов в одном сообщении  в таком формате\n'
                              'Информатика - 68\nМатематика - 56\nОбществознание - 87')
        await States.state2.set()
    else:
        await message.answer('Такого города нет в базе')
        await message.answer('Введите ещё раз')
        await States.state1.set()

@dp.message_handler(state = States.state2)
async def getter(message: types.Message, state: FSMContext):
    text = message.text
    a = text.replace(' ','').split('\n')
    inputs = {}
    for i in a:
        temp = str(i).split('-')
        try:
            inputs[dict_of_subjects[temp[0]]] = temp[1]
        except [KeyError, IndexError]:
            await message.answer('Проверьте корректность данных, и отправьте снова, или перезапустите бот')
            return
    url = f'https://vuzopedia.ru/kalkulator-ege/{dict_of_number[city]}?mat={inputs.get("mat")}&rus={inputs.get("rus")}&' \
          f'fiz={inputs.get("fiz")}&obshe={inputs.get("obshe")}&ist={inputs.get("ist")}&biol={inputs.get("biol")}' \
          f'&inform={inputs.get("inform")}&him={inputs.get("him")}&liter={inputs.get("liter")}' \
          f'&georg={inputs.get("georg")}&inyaz={inputs.get("inyaz")}'.replace('None','')
    await state.update_data(url = url)
    await message.answer('Выберите основу обучения (платное основа или бюджет)', reply_markup=keyboard2())
    await States.state3.set()


@dp.message_handler(state = States.state3)
async def say_form(message: types.Message, state: FSMContext):
    await state.update_data(osnova=message.text)
    await message.answer('Выберите форму обучения',reply_markup=keyboard3())
    await States.state4.set()

@dp.message_handler(state = States.state4)
async def say_forma(message:types.Message, state: FSMContext):
    await state.update_data(forma = message.text)
    data = await state.get_data()
    await message.answer('Найти оптимальные варианты вузов для поступления?', reply_markup=keyboard1())
    await States.state5.set()

@dp.message_handler(state=States.state5)
async def budjet(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        await message.answer('Хорошо, ищу варианты...')
        data = await state.get_data()
        url = data.get('url')
        print(url)
        answer = get_vuzi(url)
        rang = len(answer[0])
        if rang >= 6:
            rang = 6
        for i in range(rang):
            await message.answer('{}. {}\nСсылка на вуз: {}'.format(i+1,answer[0][i], answer[1][i]))
            sleep(1)
        napr = ''

        if data.get('osnova') == 'Платная основа':
            await message.answer('Направления вузов на платную основу ⬇️')
            for i in range(len(answer[3])):
                napr += '{}. '.format(i+1) + str(answer[3][i]).replace("'",'') + '\n'
            try:
                await message.answer(napr)
            except MessageTextIsEmpty:
                await message.answer('Не найдены вузы по введенным предметам\nПопробуйте ещё')
                return await States.state2.set()
        else:
            await message.answer('Основные направления вузов в которых вы проходите на бюджет ⬇️')
            for i in range(len(answer[2])):
                napr += '{}. '.format(i + 1) + str(answer[2][i]).replace("'",'') + '\n'
            try:
                await message.answer(napr)
            except MessageTextIsEmpty:
                await message.answer('Не найдены вузы по введенным предметам\nПопробуйте ещё')
                return await States.state2.set()
    else:
        await message.answer('До свидания')
    await message.answer('Хотите продолжить поиски ?', reply_markup=keyboard1())
    await States.state6.set()

@dp.message_handler(state=States.state6)
async def answer(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        await message.answer('Отправьте результаты ваших экзаменов в одном сообщении  в таком формате\n'
                             'Информатика - 68\nМатематика - 56\nОбществознание - 87')
        await States.state2.set()
    elif message.text == "Нет":
        await message.answer('Хорошо, ждём вас снова!')
        await state.reset_state()
executor.start_polling(dp)



