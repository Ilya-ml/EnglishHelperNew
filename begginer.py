import string

lvl: string = "beginner"


nature = "air - воздух\n"  \
         "wind - ветер\n"  \
         "water - вода\n"  \
         "west - запад\n"  \
         "east - восток\n" \
         "north - север\n" \
         "south - юг\n"    \
         "tree - дерево\n" \
         "sea - море\n"    \
         "ocean - океан"

nature_arr = ["air - воздух\n" \
              "wind - ветер",
              "water - вода\n" \
              "west - запад",
              "east - восток\n"\
              "north - север",
              "south - юг\n"
              "tree - дерево", \
              "sea - море\n"
              "ocean - океан"]

nature_size: int = len(nature_arr)


family = "family - семья\n"                      \
         "boy - мальчик\n"                       \
         "girl - девочка\n"                      \
         "mother - мама\n"                       \
         "father - отец\n"                       \
         "son - сын\n"                           \
         "daughter - дочь\n"                     \
         "baby - малыш\n"                        \
         "grand mother - бабушка\n"              \
         "grand father - дедушка\n"              \
         "children - дети\n"                     \
         "home - дом\n"                          \
         "love - любовь\n"                       \
         "apartment - квартира\n"                \
         "joy - радость\n"                       \
         "nephew - племянник\n"                  \
         "aunt - тетя\n"                         \
         "uncle - дядя\n"                        \
         "cousin - двоюродная сестра или брат\n" \
         "man - мужчина\n"                       \
         "woman - женщина\n"                     \
         "child - ребенок\n"                     \
         "brother - брат\n"                      \
         "relatives - родственники\n"            \
         "friend - друг\n"                       \
         "wife - жена\n"                         \
         "husband - муж\n"                       \
         "address - адрес\n"                     \
         "happiness - счастье\n"                 \
         "people - люди"

family_arr = ["family - семья\n"                      \
              "people - люди",
              "boy - мальчик\n"                       \
              "girl - девочка",
              "mother - мама\n"                       \
              "father - отец",
              "son - сын\n"                           \
              "daughter - дочь",
              "baby - малыш\n"                        \
              "relatives - родственники",
              "grand mother - бабушка\n"              \
              "grand father - дедушка",
              "child - ребенок\n"                     \
              "children - дети",
              "home - дом\n"                          \
              "apartment - квартира",
              "love - любовь\n"                       \
              "happiness - счастье\n"                 \
              "joy - радость",
              "nephew - племянник\n"                  \
              "address - адрес",
              "aunt - тетя\n"                         \
              "uncle - дядя",
              "friend - друг\n"                       \
              "cousin - двоюродная сестра или брат",
              "man - мужчина\n"                       \
              "woman - женщина\n",
              "brother - брат\n"                      \
              "sister - сестра",
              "wife - жена\n"                         \
              "husband - муж"]

family_size: int = len(family_arr)


social = "phone - телефон\n"                    \
         "question - вопрос\n"                  \
         "place - место\n"                      \
         "market - рынок\n"                     \
         "order - заказ\n"                      \
         "food - еда\n"                         \
         "work - работа\n"                      \
         "communication - общение\n"            \
         "story - история\n"                    \
         "relax - отдых\n"                      \
         "time - время\n"                       \
         "word - слово\n"                       \
         "dialogue - диалог\n"                  \
         "meeting - встреча\n"                  \
         "week - неделя\n"                      \
         "distance - дистанция\n"               \
         "club - клуб\n"                        \
         "theatre - театр\n"                    \
         "cinema - кинотеатр\n"                 \
         "coffee shop - кофейня\n"              \
         "friendship - дружба\n"                \
         "behavior - поведение\n"               \
         "attitude - отношение\n"               \
         "student - студент\n"                  \
         "university - университет\n"           \
         "union - объединение\n"                \
         "party - вечеринка\n"                  \
         "date - свидание\n"                    \
         "sweetheart - партнер, возлюбленный\n" \
         "leisure time - досуг"

social_arr = ["phone - телефон\n"                    \
              "question - вопрос",
              "place - место\n"                      \
              "market - рынок",
              "order - заказ\n"                      \
              "food - еда",
              "work - работа\n"                      \
              "communication - общение",
              "story - история\n"                    \
              "relax - отдых",
              "time - время\n"                       \
              "word - слово",
              "dialogue - диалог\n"                  \
              "meeting - встреча",
              "week - неделя\n"                      \
              "distance - дистанция",
              "club - клуб\n"                        \
              "theatre - театр",
              "cinema - кинотеатр\n"                 \
              "coffee shop - кофейня",
              "friendship - дружба\n"                \
              "behavior - поведение\n"               \
              "attitude - отношение",
              "student - студент\n"                  \
              "university - университет",
              "union - объединение\n"                \
              "party - вечеринка",
              "date - свидание\n"                    \
              "sweetheart - партнер, возлюбленный\n" \
              "leisure time - досуг"]

social_size: int = len(social_arr)


tourism = "road - дорога\n"                        \
          "ticket - билет\n"                       \
          "map - карта\n"                          \
          "motel - мотель\n"                       \
          "highway - шоссе\n"                      \
          "reception - регистратура, ресепшн\n"    \
          "wallet - бумажник\n"                    \
          "bank - банк\n"                          \
          "subway - метро\n"                       \
          "cab - такси\n"                          \
          "parking - парковка\n"                   \
          "food order - заказ еды\n"               \
          "cash - наличные\n"                      \
          "passport - паспорт\n"                   \
          "permission - разрешение\n"              \
          "lawyer - адвокат\n"                     \
          "problem - проблема\n"                   \
          "waiting room - зал ожидания\n"          \
          "transfer - пересадка\n"                 \
          "bag - сумка\n"                          \
          "suitcase - чемодан\n"                   \
          "property - имущество\n"                 \
          "law - право, закон\n"                   \
          "police station - полицейский участок\n" \
          "price - стоимость, цена\n"              \
          "price list - ценник\n"                  \
          "courier - курьер\n"                     \
          "delivery - доставка\n"                  \
          "location - местоположение\n"            \
          "route - маршрут\n"                      \
          "agreement - договор\n"                  \
          "hospital - больница\n"                  \
          "ambulance - скорая помощь"

tourism_arr = ["road - дорога\n"                        \
               "ticket - билет",
               "map - карта\n"                          \
               "motel - мотель",
               "highway - шоссе\n"                      \
               "reception - регистратура, ресепшн",
               "wallet - бумажник\n"                    \
               "bank - банк",
               "subway - метро\n"                       \
               "cab - такси",
               "parking - парковка\n"                   \
               "food order - заказ еды",
               "cash - наличные\n"                      \
               "passport - паспорт",
               "permission - разрешение\n"              \
               "lawyer - адвокат",
               "problem - проблема\n"                   \
               "waiting room - зал ожидания",
               "transfer - пересадка\n"                 \
               "bag - сумка",
               "suitcase - чемодан\n"                   \
               "property - имущество",
               "law - право, закон\n"                   \
               "police station - полицейский участок",
               "price - стоимость, цена\n"              \
               "price list - ценник",
               "courier - курьер\n"                     \
               "delivery - доставка",
               "location - местоположение\n"            \
               "route - маршрут",
               "agreement - договор\n"                  \
               "hospital - больница\n"                  \
               "ambulance - скорая помощь"]

tourism_size: int = len(tourism_arr)


books = "Вот список книг для твоего уровня:\n"         \
        "1)  «Снежная королева», Г.Х. Андерсен\n"      \
        "2)  «Ешь, молись, люби», Элизабет Гилберт\n"  \
        "3)  «Красавица и чудовище», Ш. Перро\n"       \
        "4)  «Поллианна», Э.Х. Портер\n"               \
        "5)  «Затерянный мир», Артур Конан Дойл\n"     \
        "6)  «Над пропастью во ржи», Д.Д. Сэлинджер\n" \
        "7)  «Убить пересмешника», Харпер Ли\n"        \
        "8)  «Интервью с вампиром», Энн Райс\n"        \
        "9)  «Дракула», Брэм Стокер\n"                 \
        "10) «Дневник Бриджит Джонс», Х. Филдинг\n"    \
        "11) «Принц и нищий», Марк Твен\n"             \
        "12) «Алиса в стране чудес», Л. Кэрролл\n"
