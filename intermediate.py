import string

lvl: string = "intermediate"


social = "distancing - дистанцирование\n"            \
         "self-care - забота о себе\n"               \
         "medication - лекарство\n"                  \
         "celebration - мероприятие\n"               \
         "daily routine - ежедневная рутина\n"       \
         "physician - врач, доктор, терапевт\n"      \
         "treatment - лечение\n"                     \
         "improvement - улучшение\n"                 \
         "symptom - симптом\n"                       \
         "dismay - огорчение\n"                      \
         "cancellation - отмена\n"                   \
         "suspiciousness - подозрительность\n"       \
         "escalation - рбострение, эскалация\n"      \
         "proceeding - разбирательство\n"            \
         "awareness - осознание\n"                   \
         "responsibility - ответственность\n"        \
         "aftermath - последствие\n"                 \
         "weakness - слабость\n"                     \
         "rivalry - соперничество, противостояние\n" \
         "restlessness -беспокойство\n"             \
         "uncertainty - неопределенность\n"          \
         "conscience - совесть\n"                    \
         "protection - защита, протекция\n"          \
         "referral - направление\n"                  \
         "hopelessness - безнадежность\n"            \
         "reliability - надежность\n"                \
         "verification - проверка\n"                 \
         "self-isolation - самоизоляция\n"           \
         "vaccination - вакцинация"

social_arr = ["distancing - дистанцирование\n"            \
              "self-care - забота о себе",
              "medication - лекарство\n"                  \
              "celebration - мероприятие",
              "daily routine - ежедневная рутина\n"       \
              "physician - врач, доктор, терапевт",
              "treatment - лечение\n"                     \
              "improvement - улучшение",
              "symptom - симптом\n"                       \
              "dismay - огорчение",
              "cancellation - отмена\n"                   \
              "suspiciousness - подозрительность",
              "escalation - рбострение, эскалация\n"      \
              "proceeding - разбирательство",
              "awareness - осознание\n"                   \
              "responsibility - ответственность",
              "aftermath - последствие\n"                 \
              "weakness - слабость",
              "rivalry - соперничество, противостояние\n" \
              "restlessness -беспокойство",
              "uncertainty - неопределенность\n"          \
              "conscience - совесть",
              "protection - защита, протекция\n"          \
              "referral - направление",
              "hopelessness - безнадежность\n"            \
              "reliability - надежность",
              "verification - проверка\n"                 \
              "self-isolation - самоизоляция\n"           \
              "vaccination - вакцинация"]

social_size: int = len(social_arr)


life = "downfall - падение, упадок, крах,\n"   \
       "setback - неудача, провал\n"           \
       "bad luck - невезение, несчастье\n"     \
       "depression - депрессия\n"              \
       "solitude - одиночество\n"              \
       "self-blame - самобичевание\n"          \
       "disorder - расстройство\n"             \
       "instability - нестабильность\n"        \
       "challenge - вызов, сложность\n"        \
       "sustainability - устойчивость\n"       \
       "duration - продолжительность\n"        \
       "luckiness - везение\n"                 \
       "fluke - случайность, шанс\n"           \
       "a winning - победа\n"                  \
       "lottery - лотерея\n"                   \
       "destination - предназначение\n"        \
       "advantage - преимущество\n"            \
       "win - победа, выигрыш\n"               \
       "condition - условие\n"                 \
       "contest - соревнование,\n"             \
       "humbleness - смирение, скромность\n"   \
       "hardening - закалка, твердость\n"      \
       "fearlessness - бесстрашие\n"           \
       "buoyancy - оживленность, жизнелюбие\n" \
       "morale - мораль, дух, нрав,\n"         \
       "wisdom - мудрость\n"                   \
       "decisiveness - решительность"

life_arr = ["downfall - падение, упадок, крах,\n"   \
            "setback - неудача, провал",
            "bad luck - невезение, несчастье\n"     \
            "depression - депрессия",
            "solitude - одиночество\n"              \
            "self-blame - самобичевание",
            "disorder - расстройство\n"             \
            "instability - нестабильность",
            "challenge - вызов, сложность\n"        \
            "sustainability - устойчивость",
            "duration - продолжительность\n"        \
            "luckiness - везение",
            "fluke - случайность, шанс\n"           \
            "a winning - победа",
            "lottery - лотерея\n"                   \
            "destination - предназначение",
            "advantage - преимущество\n"            \
            "win - победа, выигрыш",
            "condition - условие\n"                 \
            "contest - соревнование",
            "humbleness - смирение, скромность\n"   \
            "hardening - закалка, твердость",
            "fearlessness - бесстрашие\n"           \
            "buoyancy - оживленность, жизнелюбие",
            "morale - мораль, дух, нрав,\n"         \
            "wisdom - мудрость\n"                   \
            "decisiveness - решительность"]

life_size: int = len(life_arr)


books = "Вот список книг для твоего уровня:\n"            \
        "1)  «Forrest Gump», Winston Groom\n"             \
        "2)  «The Harry Potter Series», Joanne Rowling\n" \
        "3)  «Five Feet Apart», Rachael Lippincott\n"     \
        "4)  «The Clockwork Orange», A. Burgess\n"        \
        "5)  «Normal People», Sally Rooney\n"             \
        "6)  «The Picture of Dorian Gray», Oscar Wilde\n" \
        "7)  «Three Men In a Boat», Jerome K. Jerome\n"   \
        "8)  «Alice in Wonderland», Lewis Carroll\n"      \
        "9)  «The Chronicles of Narnia», C.S. Lewis\n"    \
        "10) «The Jungle Book», R. Kipling\n"
