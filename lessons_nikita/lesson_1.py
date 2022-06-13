number = int(input("Введите четырёх значьное число "))#здесь мы создали переменную и записали туда число

once = int(number % 10)#одиницы число
tense = int((number/10) % 10)#десятки число
hundreds = int((number / 100) % 10)#сотни число

print("сума:", once + tense + hundreds + thowsands)#сума
