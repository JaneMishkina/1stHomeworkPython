# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list_1 = input("Введите текст: ").split()
word = input("Введите слово, которое ищем: ")
count = 0

i, flag = 0, True
while i < len(list_1) and flag:
    if list_1[i] == word:
        count += 1
        if count == 2:
            print(i)
            flag = False
    i += 1
if count < 2:
    print("-1")