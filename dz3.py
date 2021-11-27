# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

#================================через dict====================================

seasons = {"Зима" : (1, 2, 12),
           "Весна" : (3, 4, 5),
           "Лето" : (6, 7, 8),
           "Осень" : (9, 10, 11)}

month = int(input("Введите месяц в виде числа от 1 до 12: "))

for key in seasons.keys():
    if month in seasons[key]:
        print(key)


# ================================через list====================================

seasons_winter = [1,2,12]
seasons_spring = [3,4,5]
seasons_summer = [6,7,8]
seasons_autumn = [9,10,11]
month1 = int(input("Введите месяц в виде числа от 1 до 12: "))
if month1 in seasons_winter:
   print('Зима')
elif month1 in seasons_spring:
   print('Весна')
elif month1 in seasons_summer:
   print('Лето')
elif month1 in seasons_autumn:
   print('Осень')











