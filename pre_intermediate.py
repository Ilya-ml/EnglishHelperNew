import string

lvl: string = "pre-intermediate"


relax = "cartoon - мультфильм\n"                           \
        "movie - фильм\n"                                  \
        "circus - цирк\n"                                  \
        "composer - композитор\n"                          \
        "dream - мечта\n"                                  \
        "daily routine - ежедневная рутина\n"              \
        "horror - ужастик\n"                               \
        "laughter - смех\n"                                \
        "novel - роман\n"                                  \
        "story - история\n"                                \
        "weather forecast - прогноз погоды\n"              \
        "thought - мысль\n"                                \
        "writer - писатель\n"                              \
        "access - доступ\n"                                \
        "account - аккаунт\n"                              \
        "adventure - приключение\n"                        \
        "affair - страх\n"                                 \
        "anniversary - дело, интрига\n"                    \
        "entertainment - развлечение\n"                    \
        "amusement - веселье\n"                            \
        "influence - влияние\n"                            \
        "attraction - достопримечательность, аттракцион\n" \
        "rock-climbing - скалолазание\n"                   \
        "cycling - катание на велосипеде\n"                \
        "number painting - живопись по номерам\n"          \
        "swimming pool - бассейн\n"                        \
        "yoga - йога\n"                                    \
        "coffee shop - кофейня\n"                          \
        "central park - центральный парк\n"                \
        "inspiration - вдохновение"

relax_arr = ["cartoon - мультфильм\n"                           \
             "movie - фильм",
             "circus - цирк\n"                                  \
             "composer - композитор",
             "dream - мечта\n"                                  \
             "daily routine - ежедневная рутина",
             "horror - ужастик\n"                               \
             "laughter - смех",
             "novel - роман\n"                                  \
             "story - история",
             "weather forecast - прогноз погоды\n"              \
             "thought - мысль",
             "writer - писатель\n"                              \
             "access - доступ\n"                                \
             "account - аккаунт",
             "adventure - приключение\n"                        \
             "affair - страх",
             "anniversary - дело, интрига\n"                    \
             "entertainment - развлечение",
             "amusement - веселье\n"                            \
             "influence - влияние",
             "attraction - достопримечательность, аттракцион\n" \
             "rock-climbing - скалолазание",
             "cycling - катание на велосипеде\n"                \
             "number painting - живопись по номерам",
             "swimming pool - бассейн\n"                        \
             "yoga - йога",
             "coffee shop - кофейня\n"                          \
             "central park - центральный парк\n"                \
             "inspiration - вдохновение"]

relax_size: int = len(relax_arr)


climate = "activist - активист\n"                   \
          "pollution - загрязнение\n"               \
          "impurity - примеси, загрязнение\n"       \
          "algae - водоросли\n"                     \
          "Earth - земля\n"                         \
          "atmosphere - атмосфера\n"                \
          "environment - окружающий мир\n"          \
          "climate - климат\n"                      \
          "air - воздух\n"                          \
          "water reserve - водные ресурсы\n"        \
          "greenhouse effect - парниковый эффект\n" \
          "oxygen - кислород\n"                     \
          "explorer - исследователь\n"              \
          "investigation - расследование\n"         \
          "future - будущее\n"                      \
          "tropic forest - тропический лес\n"       \
          "humidity	 - влажность, влага\n"          \
          "flora - флора\n"                         \
          "wildlife - дикая природа, животные\n"    \
          "plastic waste - пластиковые отходы\n"    \
          "recycling - переработка\n"               \
          "hydrosphere - гидросфера\n"              \
          "background - происхождение, фон\n"       \
          "bank - берег\n"                          \
          "banner - баннер, реклама\n"              \
          "beast - зверь, животное\n"               \
          "cave - пещера, грот\n"                   \
          "caviar - икра"

climate_arr = ["Earth - земля\n"                         \
               "atmosphere - атмосфера",
               "activist - активист\n"                   \
               "pollution - загрязнение",
               "impurity - примеси, загрязнение\n"       \
               "algae - водоросли,"
               "environment - окружающий мир\n"          \
               "climate - климат",
               "air - воздух\n"                          \
               "water reserve - водные ресурсы",
               "greenhouse effect - парниковый эффект\n" \
               "oxygen - кислород",
               "explorer - исследователь\n"              \
               "investigation - расследование",
               "future - будущее\n"                      \
               "tropic forest - тропический лес",
               "humidity - влажность, влага\n"           \
               "flora - флора",
               "wildlife - дикая природа, животные\n"    \
               "plastic waste - пластиковые отходы",
               "recycling - переработка\n"               \
               "hydrosphere - гидросфера",
               "background - происхождение, фон\n"       \
               "bank - берег",
               "banner - баннер, реклама\n"              \
               "beast - зверь, животное",
               "cave - пещера, грот\n"                   \
               "caviar - икра"]

climate_size: int = len(climate_arr)


books = "Вот список книг для твоего уровня:\n"                      \
        "1)  «Mr. Bean In Town», John Escott\n"                     \
        "2)  «The Hound of the Baskervilles», Arthur Conan Doyle\n" \
        "3)  «The Fisherman and His Soul», Oscar Wilde\n"           \
        "4)  «Dracula», Bram Stoker\n"                              \
        "5)  «The Million Pound Bank Note», Mark Twain\n"           \
        "6)  «The Wonderful Wizard of Oz», Lyman Frank Baum\n"      \
        "7)  «Winnie-the-Pooh», A. A. Milne\n"                      \
        "8)  «Mary Poppins», P. L. Travers\n"                       \
        "9)  «Two Little Savages», E. T. Seton\n"                   \
        "10) «The Adventures of Tom Sawyer», M. Twain\n"
