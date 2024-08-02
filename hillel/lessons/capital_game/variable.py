health = 100  #глобальна змінна


def damage():
    global health  #щоб можна було змінювати значення глобальної змінної
    power = 20  #локальна змінна
    health -= power


damage()
print(health)