import string

import uses
import messages
import begginer
import pre_intermediate
import intermediate
import upper_intermediate
import advanced


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
    uses.bot.send_message(message.chat.id, messages.first_message)


@uses.bot.message_handler(commands=['eng_level'])
def button_message(message):
    global level
    level = "start"
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Beginner")
    item2 = uses.types.KeyboardButton("Pre-Intermediate")
    item3 = uses.types.KeyboardButton("Intermediate")
    item4 = uses.types.KeyboardButton("Upper-Intermediate")
    item5 = uses.types.KeyboardButton("Advanced")
    markup.add(item1, item2, item3, item4, item5)
    uses.bot.send_message(message.chat.id, messages.choose_level_message, reply_markup=markup)


# Beginner

@uses.bot.message_handler("Beginner")
def beggg(message):
    global level
    level = begginer.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
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
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Pre-Intermediate

@uses.bot.message_handler("Pre-Intermediate")
def pre_int(message):
    global level
    level = pre_intermediate.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
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
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Intermediate

@uses.bot.message_handler("Intermediate")
def inter(message):
    global level
    level = intermediate.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
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
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Upper-Intermediate

@uses.bot.message_handler("Upper-Intermediate")
def upper_int(message):
    global level
    level = upper_intermediate.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
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
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Advanced

@uses.bot.message_handler("Advanced")
def adv(message):
    global level
    level = advanced.lvl
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
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
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler(content_types='text')
def message_reply(message):

    if level == "start":

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

    # Beginner
    elif level == begginer.lvl:

        if message.text == "Новые слова":
            new_word_for_beg(message)

        if message.text == "Окружающий мир":
            uses.bot.send_message(message.chat.id, begginer.nature)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Семья":
            uses.bot.send_message(message.chat.id, begginer.family)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Для туриста":
            uses.bot.send_message(message.chat.id, begginer.tourism)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Социальная коммуникация":
            uses.bot.send_message(message.chat.id, begginer.social)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Книги":
            uses.bot.send_message(message.chat.id, begginer.books)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Назад":
            for_beg(message)

        if message.text == "Тест":
            uses.bot.send_message(message.chat.id, "В скором времени")
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

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

        if message.text == "Тест":
            uses.bot.send_message(message.chat.id, "В скором времени")
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

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

        if message.text == "Тест":
            uses.bot.send_message(message.chat.id, "В скором времени")
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

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

        if message.text == "Тест":
            uses.bot.send_message(message.chat.id, "В скором времени")
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

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

        if message.text == "Тест":
            uses.bot.send_message(message.chat.id, "В скором времени")
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

        if message.text == "Поменять уровень":
            uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')


uses.bot.infinity_polling()
