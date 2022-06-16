import random
import os
q = True
while q:
	x1 = 1
	x2 = 100
	menu = '''
1.random namber min:1 max:100
2.random namber min:1 max:1000
3.your choise

'''

	print(menu)
	ch = input(">>")
	if ch == "2":
			x2 = 1000
	if ch == "3":
			x1 = int(input("Min number: "))
			x2 = int(input("Max number: "))
	os.system('cls')
	w = True
	a = (random.randint(x1, x2))
	print ("Угадай число от 1 до 100")
	while w :
		print ("                    ")
		s = input ("Введите число : ")
		print ("                    ")
		if (int(a) == int(s)):
			print ("У вас получилось")
			w = False;
		else :
			if (int(a) > int(s)):
				print ("СЛИШКОМ МАЛО")
			if (int(a) < int(s)):
				print ("СЛИШКОМ МНОГО")