# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
vvod = input("Введите несколько слов: ").split()
for i, stroki in enumerate(vvod):
    print("№ Строки:", i, ">> Ваши слова: >>", stroki)
for x in vvod:
    if (len(x) > 10):
        print("Первые 10 букв длинного слова: >>>", x[:10])

