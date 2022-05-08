import string

lvl: string = "upper-intermediate"


education = "questionnaire - анкета, опросник\n"  \
            "oversight - надзор, контроль\n"      \
            "estimating - оценивание\n"           \
            "inquiry - исследование\n"            \
            "contemplation - размышление\n"       \
            "alternative - Аальтернатива\n"       \
            "grade - класс, оценка\n"             \
            "graduate - выпускник\n"              \
            "credential - диплом, аттестат\n"     \
            "accolade - награда, похвала\n"       \
            "scale - шкала, величина\n"           \
            "gliding - планерка\n"                \
            "record	- запись, досье\n"            \
            "measurability - исчислимость\n"      \
            "worksheet - рабочий лист, таблица\n" \
            "galore - множество\n"                \
            "sequence - последовательность"

education_arr = ["questionnaire - анкета, опросник\n"  \
                 "oversight - надзор, контроль",
                 "estimating - оценивание\n"           \
                 "inquiry - исследование",
                 "contemplation - размышление\n"       \
                 "alternative - Аальтернатива",
                 "grade - класс, оценка\n"             \
                 "graduate - выпускник",
                 "credential - диплом, аттестат\n"     \
                 "accolade - награда, похвала",
                 "scale - шкала, величина\n"           \
                 "gliding - планерка",
                 "record - запись, досье\n"            \
                 "measurability - исчислимость",
                 "worksheet - рабочий лист, таблица\n" \
                 "galore - множество\n"                \
                 "sequence - последовательность"]

education_size: int = len(education_arr)


social = "doorstep - порог квартиры\n"       \
         "supervisor - супервайзер\n"        \
         "affirmation - утверждение\n"       \
         "drop-off - спад\n"                 \
         "conversation - разговор, беседа\n" \
         "indifference - безразличие\n"      \
         "segmentation - сегментация\n"      \
         "landmark - веха, ориентир\n"       \
         "upheaval - переворот\n"            \
         "disarray - беспорядок\n"           \
         "proof - доказательство\n"          \
         "influx - наплыв\n"                 \
         "struggle - борьба\n"               \
         "authenticity - подлинность\n"      \
         "backlash - обратная реакция\n"     \
         "connotation - подтекст, смысл"

social_arr = ["doorstep - порог квартиры\n"       \
              "supervisor - супервайзер",
              "affirmation - утверждение\n"       \
              "drop-off - спад",
              "conversation - разговор, беседа\n" \
              "indifference - безразличие,"
              "segmentation - сегментация\n"      \
              "landmark - веха, ориентир",
              "upheaval - переворот\n"            \
              "disarray - беспорядок",
              "proof - доказательство\n"          \
              "influx - наплыв",
              "struggle - борьба\n"               \
              "authenticity - подлинность",
              "backlash - обратная реакция\n"     \
              "connotation - подтекст, смысл"]

social_size: int = len(social_arr)


books = "Вот список книг для твоего уровня:\n"       \
        "1) «Little Fires Everywhere», Celeste Ng\n" \
        "2) «The Bourne Identity», Robert Ludlum\n"  \
        "3) «Eat, Pray, Love», Elizabeth Gilbert\n"  \
        "4) «The Da Vinci Code», Dan Brown\n"        \
        "5) «Airport», Arthur Hailey\n"              \
        "6) «Fahrenheit 451», Ray Bradbury\n"        \
        "7) «Jane Eyre», Charlotte Brontë\n"         \
        "8) «Pride and Prejudice», Jane Austen\n"    \
        "9) «Little Women», Louisa May Alcott\n"
