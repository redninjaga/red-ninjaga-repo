# mouth = int(input("Ведите зарблату в месяце "))
# number_mouth = int(input("За какое количество месяцов вы хотите увидить зарплату "))
# print(mouth * number_mouth)
# number_cake = int(input("Ведите Сколько вы хотите тортов"))
# counter = 0
# eggs = 0
# while counter <= number_cake:
#     print("яиц")
#     eggs = eggs + counter
#     print(eggs)
#     counter = counter + 1

# number = int(input("Ведите Сколько минут вы перевести в часах "))# Водим количество минут которое будем переводить в часах
# rezalt = int(number / 60)# находим количество часов
# minutes = number - rezalt * 60# находим количество минут
# print(rezalt, "часа")# выводим часы
# print(minutes, "минут")

number = int(input("Ведите Сколько секунд вам нужно перевести в: дней, часах, минут, секундах "))
minutes = int(number / 60)# находим количество минут
hours = int(minutes / 60)# находим количество часов
days = int(hours / 24)# находим количество дней
seconds = number - minutes * 60
print(days, "дней")
print(hours, "часов")
print(minutes, "минут")
print(seconds, "секунд")
