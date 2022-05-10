from email import charset
from encodings import utf_8
import string
import uses
import messages
import beginner
import pre_intermediate
import intermediate
import upper_intermediate
import advanced
import wikipedia
import re
from translate import Translator
import sqlite3
import random


# Бот - @EnglishHelperTestBot


level: string = "start"


beg_nature: int = 0
beg_family: int = 0
beg_social: int = 0
beg_tourism: int = 0

pre_relax: int = 0
pre_climate: int = 0

int_social: int = 0
int_life: int = 0

upp_social: int = 0
upp_education: int = 0

adv_social: int = 0
adv_science: int = 0


@uses.bot.message_handler(commands=['start'])
def start_message(message):
    global UsId
    UsId = int(message.chat.id)
    global level
    level = "start"
    AddId(message)


@uses.bot.message_handler(commands=['eng_level'])
def button_message(message):
    global level
    level = "start_lvl"
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Beginner")
    item2 = uses.types.KeyboardButton("Pre-Intermediate")
    item3 = uses.types.KeyboardButton("Intermediate")
    item4 = uses.types.KeyboardButton("Upper-Intermediate")
    item5 = uses.types.KeyboardButton("Advanced")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item2, item3, item4, item5, item6)
    uses.bot.send_message(message.chat.id, messages.choose_level_message, reply_markup=markup)


@uses.bot.message_handler(commands=['test'])
def testtt(message):
    global level
    level = "start_test"
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Да)")
    item2 = uses.types.KeyboardButton("Нет(")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, messages.test_message, reply_markup=markup)


@uses.bot.message_handler(commands=['game'])
def gamee(message):
    global level
    level = "start_game"
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Да)")
    item2 = uses.types.KeyboardButton("Нет(")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, messages.game_message, reply_markup=markup)


@uses.bot.message_handler(commands=['extra'])
def extra_inf(message):
    global level
    level = "start_extra"
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Полезный сайт")
    item2 = uses.types.KeyboardButton("PDF")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, messages.extra_message, reply_markup=markup)


@uses.bot.message_handler(commands=['translater'])
def start_translate(message):
    global level
    level = "start_tran"
    translaterr(message)
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    uses.bot.send_message(message.chat.id, "Возвращаемся в начало", reply_markup=markup)
    to_start(message)


@uses.bot.message_handler("В начало")
def to_start(message):
    global level
    level = "start"
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    uses.bot.send_message(message.chat.id, messages.to_start_message, reply_markup=markup)


# Beginner

@uses.bot.message_handler("Beginner")
def beggg(message):
    global level
    level = beginner.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item2 = uses.types.KeyboardButton("Книги")
    item3 = uses.types.KeyboardButton("Поменять уровень")
    item4 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова")
def new_word_for_beg(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Окружающий мир")
    item2 = uses.types.KeyboardButton("Семья")
    item3 = uses.types.KeyboardButton("Для туриста")
    item4 = uses.types.KeyboardButton("Социальная коммуникация")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад")
def for_beg(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item3, item4, item6)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Pre-Intermediate

@uses.bot.message_handler("Pre-Intermediate")
def pre_int(message):
    global level
    level = pre_intermediate.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item3, item4, item6)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова")
def new_word_for_pre_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Отдых")
    item2 = uses.types.KeyboardButton("Климат")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад")
def for_pre_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item3, item4, item6)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Intermediate

@uses.bot.message_handler("Intermediate")
def inter(message):
    global level
    level = intermediate.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item3, item4, item6)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова")
def new_word_for_inter(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Социальная коммуникация")
    item2 = uses.types.KeyboardButton("Повседневные")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад")
def for_inter(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item3, item4, item6)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Upper-Intermediate

@uses.bot.message_handler("Upper-Intermediate")
def upper_int(message):
    global level
    level = upper_intermediate.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item3, item4, item6)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова")
def new_word_for_upper_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Социальная коммуникация")
    item2 = uses.types.KeyboardButton("Образование")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад")
def for_upper_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item3, item4, item6)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Advanced

@uses.bot.message_handler("Advanced")
def adv(message):
    global level
    level = advanced.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item3, item4, item6)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова")
def new_word_for_adv(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Социальная коммуникация")
    item2 = uses.types.KeyboardButton("Наука")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад")
def for_adv(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    item6 = uses.types.KeyboardButton("В начало")
    markup.add(item1, item3, item4, item6)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


def send_files(message):
    with open("C:\\Users\\tmeln\\Documents\\Илья\\Универ\\2 курс\\ПД\\EHelp\\files\\file1.pdf", "rb") as misc1:
        f1 = misc1.read()
    uses.bot.send_document(message.chat.id, f1)
    with open("C:\\Users\\tmeln\\Documents\\Илья\\Универ\\2 курс\\ПД\\EHelp\\files\\file2.pdf", "rb") as misc2:
        f2 = misc2.read()
    uses.bot.send_document(message.chat.id, f2)
    with open("C:\\Users\\tmeln\\Documents\\Илья\\Универ\\2 курс\\ПД\\EHelp\\files\\file3.pdf", "rb") as misc3:
        f3 = misc3.read()
    uses.bot.send_document(message.chat.id, f3)
    with open("C:\\Users\\tmeln\\Documents\\Илья\\Универ\\2 курс\\ПД\\EHelp\\files\\file4.pdf", "rb") as misc4:
        f4 = misc4.read()
    uses.bot.send_document(message.chat.id, f4)


#----------------------------Переводчик--------------------------------
def GetTranslate(s):
    try:
        translator = Translator(from_lang = "ru", to_lang = "en")
        translation = translator.translate(s)
        return translation
    except Exception as e:
        return 'Что-то пошло не так'


def translaterr(message):
    mess = uses.bot.send_message(message.chat.id, 'Введите слово для перевода:')
    uses.bot.register_next_step_handler(mess, Testik)
    
def Testik(message):
    uses.bot.send_message(message.chat.id, GetTranslate(message.text))

#-----------------------------------------------------------------------


@uses.bot.message_handler(content_types='text')
def message_reply(message):
    if level == "start_extra":
        if message.text == "Полезный сайт":
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "https://breakingnewsenglish.com", reply_markup=markup)
            uses.bot.send_message(message.chat.id, "Возвращаемся в начало", reply_markup=markup)
            to_start(message)
        else:
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "Вот полезные файлы:", reply_markup=markup)
            send_files(message)
            uses.bot.send_message(message.chat.id, "Возвращаемся в начало", reply_markup=markup)
            to_start(message)

    elif level == "start_test":
        if message.text == "Да)":
            global num
            num = 1
            global wrong_answ
            wrong_answ = 0
            global right_answ
            right_answ = 0
            answBut(message)
        else:
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "Ну ладно( Тогда возвращаемся в начало", reply_markup=markup)
            to_start(message)

    elif level == "start_game":
        if message.text == "Да)":
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "Круто) Тогда начинаем игру", reply_markup=markup)
            PlayWord(message)
        else:
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "Ну ладно( Тогда возвращаемся в начало", reply_markup=markup)
            to_start(message)

    elif level == "start_lvl":

        if message.text == "Beginner":
            beggg(message)

        if message.text == "Pre-Intermediate":
            pre_int(message)

        if message.text == "Intermediate":
            inter(message)

        if message.text == "Upper-Intermediate":
            upper_int(message)

        if message.text == "Advanced":
            adv(message)

        if message.text == "В начало":
            to_start(message)

    # Beginner
    elif level == beginner.lvl:

        if message.text == "Новые слова":
            new_word_for_beg(message)

        if message.text == "Окружающий мир":
            uses.bot.send_message(message.chat.id, beginner.nature)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Семья":
            uses.bot.send_message(message.chat.id, beginner.family)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Для туриста":
            uses.bot.send_message(message.chat.id, beginner.tourism)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Социальная коммуникация":
            uses.bot.send_message(message.chat.id, beginner.social)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Книги":
            uses.bot.send_message(message.chat.id, beginner.books)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Назад":
            for_beg(message)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

        if message.text == "В начало":
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "Возвращаемся в начало", reply_markup=markup)
            to_start(message)

    # Pre-Intermediate
    elif level == pre_intermediate.lvl:

        if message.text == "Новые слова":
            new_word_for_pre_int(message)

        if message.text == "Отдых":
            uses.bot.send_message(message.chat.id, pre_intermediate.relax)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Климат":
            uses.bot.send_message(message.chat.id, pre_intermediate.climate)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Книги":
            uses.bot.send_message(message.chat.id, pre_intermediate.books)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Назад":
            for_pre_int(message)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

        if message.text == "В начало":
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "Возвращаемся в начало", reply_markup=markup)
            to_start(message)

    # Intermediate
    elif level == intermediate.lvl:

        if message.text == "Новые слова":
            new_word_for_inter(message)

        if message.text == "Социальная коммуникация":
            uses.bot.send_message(message.chat.id, intermediate.social)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Повседневные":
            uses.bot.send_message(message.chat.id, intermediate.life)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Книги":
            uses.bot.send_message(message.chat.id, intermediate.books)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Назад":
            for_inter(message)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

        if message.text == "В начало":
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "Возвращаемся в начало", reply_markup=markup)
            to_start(message)

    # Upper-Intermediate
    elif level == upper_intermediate.lvl:

        if message.text == "Новые слова":
            new_word_for_upper_int(message)

        if message.text == "Социальная коммуникация":
            uses.bot.send_message(message.chat.id, upper_intermediate.social)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Образование":
            uses.bot.send_message(message.chat.id, upper_intermediate.education)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Книги":
            uses.bot.send_message(message.chat.id, upper_intermediate.books)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Назад":
            for_upper_int(message)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

        if message.text == "В начало":
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "Возвращаемся в начало", reply_markup=markup)
            to_start(message)

    # Advanced (if level == advanced.lvl:)
    else:

        if message.text == "Новые слова":
            new_word_for_adv(message)

        if message.text == "Социальная коммуникация":
            uses.bot.send_message(message.chat.id, advanced.social)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Наука":
            uses.bot.send_message(message.chat.id, advanced.science)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Книги":
            uses.bot.send_message(message.chat.id, advanced.books)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Назад":
            for_adv(message)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

        if message.text == "В начало":
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            uses.bot.send_message(message.chat.id, "Возвращаемся в начало", reply_markup=markup)
            to_start(message)


#-----------------------------------------

db = sqlite3.connect('C:\\Users\\tmeln\\Documents\\Илья\\Универ\\2 курс\\ПД\\EHelp\\database1.db', check_same_thread=False)


#Create cursor
cursor = db.cursor()

#Количество полей базы данных
def FildCount():
    cursor.execute("SELECT COUNT(*) FROM questions")
    DB_count = cursor.fetchone()[0]
    return DB_count

#рандомное число от 1 до кол-ва полей БД

@uses.bot.message_handler(content_types='text')
def PlayWord(message):
    #Create cursor
    cursor = db.cursor()
    #uses.bot.send_message(message.chat.id, "игра в слова")

    #рандомное число от 1 до кол-ва полей БД
    global r
    r = random.randint(1, 40)
    
    # вопрос
    cursor.execute("SELECT question FROM questions WHERE id = ?", [r])
    cc = cursor.fetchone()[0]
    mess = uses.bot.send_message(message.chat.id, cc)

    # правильный ответ
    cursor.execute("SELECT Correct_answer FROM questions WHERE id = ?", [r])
    global cc2
    cc2 = cursor.fetchone()[0]

    uses.bot.register_next_step_handler(mess, Answ)
    

def Answ(message):
    if message.text == "стоп":
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        uses.bot.send_message(message.chat.id, "Возвращаемся в начало", reply_markup=markup)
        to_start(message)
        return
    else:    
        cursor.execute("SELECT Correct_answer FROM questions WHERE id = ? AND Correct_answer = ?", [r, message.text])
        if cursor.fetchone() is None:
            uses.bot.send_message(message.chat.id, "не верно " + "("+ cc2 +")")
        else:
            uses.bot.send_message(message.chat.id, "верно")
    PlayWord(message)

#cursor.close
#db.close

#-------------проверка на регистрацию пользователя в боте-------------------

def AddId(message):   
    dbu = sqlite3.connect('C:\\Users\\tmeln\\Documents\\Илья\\Универ\\2 курс\\ПД\\EHelp\\Usrs.db', check_same_thread=False)
    curs = dbu.cursor()
    curs.execute("SELECT Id FROM Users WHERE Id = ?", [UsId])
    if curs.fetchone() is None:
        curs.execute("INSERT INTO Users ( Id, IsTestible) VALUES (?,?)" , [UsId, False])
        uses.bot.send_message(message.chat.id, messages.first_message)
        uses.bot.send_message(message.chat.id, "Вы успешно зарегистрированы!")
    else:
        uses.bot.send_message(message.chat.id, messages.first_message_else)
    dbu.commit()
    curs.close()
    dbu.close()


def IsTest(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    Item_Yes = uses.types.KeyboardButton("Да!😊")
    item_No = uses.types.KeyboardButton("Нет😒")
    markup.add(Item_Yes, item_No)
    uses.bot.send_message(message.chat.id, 'Хотите пройти тест на знание английского?', reply_markup=markup)


#----------------тест на уровень знаний------------------------

#Количество полей базы данных
def FildCount():
    dbase = sqlite3.connect('C:\\Users\\tmeln\\Documents\\Илья\\Универ\\2 курс\\ПД\\EHelp\\Testik.db')
    global cursForCount
    cursForCount = dbase.cursor()
    cursForCount.execute("SELECT COUNT(*) FROM tests")
    DB_count = cursForCount.fetchone()[0]
    cursForCount.close()
    dbase.close()
    return DB_count


def answBut(message):
    #try:
        dbForTest = sqlite3.connect('C:\\Users\\tmeln\\Documents\\Илья\\Универ\\2 курс\\ПД\\EHelp\\Testik.db')
        #Create cursor
        cursorForTest = dbForTest.cursor()

        # вопрос
        cursorForTest.execute("SELECT question FROM tests WHERE No = ?", [num])
        qt = cursorForTest.fetchone()[0]
        
        # правильный ответ 
        global ca
        cursorForTest.execute("SELECT correct_answer FROM tests WHERE No = ?", [num])
        ca = cursorForTest.fetchone()[0]

        # не правильный 1
        global ua1
        cursorForTest.execute("SELECT uncorrect_answ1 FROM tests WHERE No = ?", [num])
        ua1 = cursorForTest.fetchone()[0]

        # не правильный2
        global ua2
        cursorForTest.execute("SELECT uncorrect_answ2 FROM tests WHERE No = ?", [num])
        ua2 = cursorForTest.fetchone()[0]


        lst = [ca, ua1, ua2]
        random.shuffle(lst)

        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        CorAnsw = uses.types.KeyboardButton(lst[0])
        UncorAnsw1 = uses.types.KeyboardButton(lst[1])
        UncorAnsw2 = uses.types.KeyboardButton(lst[2])
        stop = uses.types.KeyboardButton("стоп")
        markup.add(CorAnsw, UncorAnsw1, UncorAnsw2, stop)
        mess = uses.bot.send_message(message.chat.id, qt, reply_markup=markup)
        uses.bot.register_next_step_handler(mess, ret)
    #except Exception as e:
        #print(e.message, e.args)

def ret(message):
    global num 
    global right_answ
    global wrong_answ


    if message.text == "стоп":
        num = 1
        to_start(message)
        return

    if message.text == ca:
        right_answ += 1
        uses.bot.send_message(message.chat.id, "Верно!🤩")

    if message.text == ua1:
        wrong_answ += 1
        uses.bot.send_message(message.chat.id, "Не верно!😯")


    if message.text == ua2:
        wrong_answ += 1
        uses.bot.send_message(message.chat.id, "Не верно!😯") 

    if num == FildCount():
        uses.bot.send_message(message.chat.id, "Вы ответили правильно на " + str(right_answ)  + " из " + str(right_answ + wrong_answ) + " вопросов " + RecomLevel() )  
        to_start(message)
        return
    num += 1
    answBut(message)


def RecomLevel():
    if  right_answ  <= 15:
        return "рекомендуемый уровень: начальный👼 "

    if  right_answ  >= 25:
        return "рекомендуемый уровень: продвинутый👨‍🎓 "
    else:
        return "рекомендуемый уровень: средний🤠"
    
    #отправляет картинку
def SendPhoto(message):
    dbForTest = sqlite3.connect('F:\\May be tut\\NEW Eng\\EnglishHelperNew\\Testik.db')
    #Create cursor
    CurPics = dbForTest.cursor()


    CurPics.execute("SELECT photo FROM Image WHERE Id = ?", [1])
    pt = CurPics.fetchone()[0]
    
    p = open(pt, "rb")
    uses.bot.send_photo(message.chat.id, p)

#отправляет указанный файл
def send_File(message):
    with open("F:\\May be tut\\NEW Eng\\EnglishHelperNew\images\\220310-plant-based-diet-m.pdf","rb") as misc:
        f = misc.read()
    uses.bot.send_document(message.chat.id, f)


uses.bot.infinity_polling()