adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")
print(adventures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

adventures_of_tom_sawer = adventures_of_tom_sawer.replace("....", " ")
print(adventures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

text_split = adventures_of_tom_sawer.split()
adventures_of_tom_sawer = " ".join(text_split)
print(adventures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print("The letter 'h' occurs in the text, times:", adventures_of_tom_sawer.count("h"))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count = 0
for word in adventures_of_tom_sawer.split():
    if word.istitle():
        count += 1
print("With a capital letter in the text begins, words:", count)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

position_1 = adventures_of_tom_sawer.find("Tom")
position_2 = adventures_of_tom_sawer.find("Tom", position_1 + 1)
print(f"The word 'Tom' occurs in the text for the second time at {position_2} position")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adventures_of_tom_sawer_sentences = [sentence.strip() for sentence in adventures_of_tom_sawer.split(".")
                                     if sentence.strip()]
print(adventures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print("Sentences with all words in lowercase:", adventures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for sentence in adventures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print("The sentence 'By the time' is found:", sentence)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adventures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print("In the last sentence the number of words is:", word_count)