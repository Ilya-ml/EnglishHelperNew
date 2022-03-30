import uses
import messages
import begginer
import pre_intermediate
import intermediate
import upper_intermediate
import advanced


# Бот - @EnglishHelperTestBot


@uses.bot.message_handler(commands=['start'])
def start_message(message):
    uses.bot.send_message(message.chat.id, messages.first_message)


@uses.bot.message_handler(commands=['eng_level'])
def button_message(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Begginer")
    item2 = uses.types.KeyboardButton("Pre-Intermediate")
    item3 = uses.types.KeyboardButton("Intermediate")
    item4 = uses.types.KeyboardButton("Upper-Intermediate")
    item5 = uses.types.KeyboardButton("Advanced")

    markup.add(item1, item2, item3, item4, item5)
    uses.bot.send_message(message.chat.id, messages.choose_level_message, reply_markup=markup)


# Begginer

@uses.bot.message_handler("Begginer")
def beggg(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова (begginer)")
    item2 = uses.types.KeyboardButton("Тест (begginer)")
    item3 = uses.types.KeyboardButton("Книги (begginer)")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова (begginer)")
def new_word_for_beg(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Окружающий мир")
    item2 = uses.types.KeyboardButton("Семья")
    item3 = uses.types.KeyboardButton("Для туриста")
    item4 = uses.types.KeyboardButton("Социальная коммуникация (begginer)")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад (begginer)")
def for_beg(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова (begginer)")
    item2 = uses.types.KeyboardButton("Тест (begginer)")
    item3 = uses.types.KeyboardButton("Книги (begginer)")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Pre-Intermediate

@uses.bot.message_handler("Pre-Intermediate")
def pre_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова (pre-intermediate)")
    item2 = uses.types.KeyboardButton("Тест (pre-intermediate)")
    item3 = uses.types.KeyboardButton("Книги (pre-intermediate)")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова (pre-intermediate)")
def new_word_for_pre_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Отдых")
    item2 = uses.types.KeyboardButton("Климат")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад (pre-intermediate)")
def for_pre_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова (pre-intermediate)")
    item2 = uses.types.KeyboardButton("Тест (pre-intermediate)")
    item3 = uses.types.KeyboardButton("Книги (pre-intermediate)")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Intermediate

@uses.bot.message_handler("Intermediate")
def inter(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова (intermediate)")
    item2 = uses.types.KeyboardButton("Тест (intermediate)")
    item3 = uses.types.KeyboardButton("Книги (intermediate)")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова (intermediate)")
def new_word_for_inter(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Социальная коммуникация (intermediate)")
    item2 = uses.types.KeyboardButton("Повседневные")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад (intermediate)")
def for_inter(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова (intermediate)")
    item2 = uses.types.KeyboardButton("Тест (intermediate)")
    item3 = uses.types.KeyboardButton("Книги (intermediate)")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


# Upper-Intermediate

@uses.bot.message_handler("Upper-Intermediate")
def upper_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова (int)")
    item2 = uses.types.KeyboardButton("Тест (int)")
    item3 = uses.types.KeyboardButton("Книги (int)")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова (int)")
def new_word_for_upper_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Социальная коммуникация (int)")
    item2 = uses.types.KeyboardButton("Повседневные (int)")
    markup.add(item1, item2)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад (int)")
def for_upper_int(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова (int)")
    item2 = uses.types.KeyboardButton("Тест (int)")
    item3 = uses.types.KeyboardButton("Книги (int)")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler(content_types='text')
def message_reply(message):

    if message.text == "Begginer":
        beggg(message)

    if message.text == "Pre-Intermediate":
        pre_int(message)

    if message.text == "Intermediate":
        inter(message)

    if message.text == "Поменять уровень":
        uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')


    # Begginer

    if message.text == "Новые слова (begginer)":
        new_word_for_beg(message)

    if message.text == "Окружающий мир":
        uses.bot.send_message(message.chat.id, begginer.nature)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (begginer)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Семья":
        uses.bot.send_message(message.chat.id, begginer.family)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (begginer)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Для туриста":
        uses.bot.send_message(message.chat.id, begginer.tourism)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (begginer)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Социальная коммуникация (begginer)":
        uses.bot.send_message(message.chat.id, begginer.social)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (begginer)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Книги (begginer)":
        uses.bot.send_message(message.chat.id, begginer.books)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (begginer)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Назад (begginer)":
        for_beg(message)

    if message.text == "Тест (begginer)":
        uses.bot.send_message(message.chat.id, "В скором времени")
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (begginer)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)


    # Pre-Intermediate

    if message.text == "Новые слова (pre-intermediate)":
        new_word_for_pre_int(message)

    if message.text == "Отдых":
        uses.bot.send_message(message.chat.id, pre_intermediate.relax)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (pre-intermediate)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Климат":
        uses.bot.send_message(message.chat.id, pre_intermediate.climate)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (pre-intermediate)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Книги (pre-intermediate)":
        uses.bot.send_message(message.chat.id, pre_intermediate.books)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (pre-intermediate)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Назад (pre-intermediate)":
        for_pre_int(message)

    if message.text == "Тест (pre-intermediate)":
        uses.bot.send_message(message.chat.id, "В скором времени")
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (pre-int)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)


    # Intermediate

    if message.text == "Новые слова (intermediate)":
        new_word_for_inter(message)

    if message.text == "Социальная коммуникация (intermediate)":
        uses.bot.send_message(message.chat.id, intermediate.social)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (intermediate)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Повседневные":
        uses.bot.send_message(message.chat.id, intermediate.life)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (intermediate)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Книги (intermediate)":
        uses.bot.send_message(message.chat.id, pre_intermediate.books)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (intermediate)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Назад (intermediate)":
        for_inter(message)

    if message.text == "Тест (intermediate)":
        uses.bot.send_message(message.chat.id, "В скором времени")
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад (intermediate)")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)


uses.bot.infinity_polling()
