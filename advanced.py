import string

lvl: string = "advanced"


science = "axis - ось\n"                   \
          "modality - метод, форма\n"      \
          "discerning - распознавание\n"   \
          "pattern - образец, модель\n"    \
          "anthropologist - антрополог\n"  \
          "Oversight - надзор, контроль\n" \
          "exhibition - выставка\n"        \
          "interference - вмешательство\n" \
          "bureaucracy - бюрократия\n"     \
          "generation - поколение\n"       \
          "implication - следствие\n"      \
          "offspring - потомство\n"        \
          "cognition - познание\n"

science_arr = ["axis - ось\n"                   \
               "modality - метод, форма",
               "discerning - распознавание\n"   \
               "pattern - образец, модель",
               "anthropologist - антрополог\n"  \
               "Oversight - надзор, контроль",
               "exhibition - выставка\n"        \
               "interference - вмешательство",
               "bureaucracy - бюрократия\n"     \
               "generation - поколение",
               "implication - следствие\n"      \
               "offspring - потомство\n"        \
               "cognition - познание"]

science_size: int = len(science_arr)


social = "perseverance - настойчивость\n"    \
         "disobedience - непослушание\n"     \
         "adolescent - подросток\n"          \
         "attempt - попытка\n"               \
         "proponent - сторонник\n"           \
         "anxiety - беспокойство, тревога\n" \
         "disparity - неравенство\n"         \
         "downward - снижение\n"             \
         "temptation - искушение\n"          \
         "distraction - отвлечение\n"        \
         "compassion - сострадание\n"        \
         "stigma - клеймо\n"                 \
         "affection - привязанность\n"

social_arr = ["perseverance - настойчивость\n"    \
              "disobedience - непослушание",
              "adolescent - подросток\n"          \
              "attempt - попытка",
              "proponent - сторонник\n"           \
              "anxiety - беспокойство, тревога",
              "disparity - неравенство\n"         \
              "downward - снижение",
              "temptation - искушение\n"          \
              "distraction - отвлечение",
              "compassion - сострадание\n"        \
              "stigma - клеймо\n"                 \
              "affection - привязанность"]

social_size: int = len(social_arr)


books = "Вот список книг для твоего уровня:\n"                 \
        "1)  «Atonement», Ian McEwan\n"                        \
        "2)  «The Remains of the Day», Kazuo Ishiguro\n"       \
        "3)  «The Power», Naomi Alderman\n"                    \
        "4)  «Warlight», Michael Ondaatje\n"                   \
        "5)  «Cloud Atlas», David Mitchell\n"                  \
        "6)  «Everything Illuminated», Jonathan Safran Foer\n" \
        "7)  «East Of Eden», John Steinbeck\n"                 \
        "8)  «Brave New World», Aldous Huxley\n"               \
        "9)  «The Great Gatsby», F.S. Fitzgeraldn\n"           \
        "10) «Catch-22», Joseph Heller\n"
