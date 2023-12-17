import pygame

toyota_marka = "Toyota_Supra"
toyota_speed = "220-266"
toyota_power = "105-387"
toyota_diametr = "15-19"
toyota_energy = "Бензин"
toyota_fuel = 7
toyota_budget = 2900
bmw_marka = "BMW_M3"
bmw_speed = "227-302"
bmw_power = "195-510"
bmw_diametr = "17-20"
bmw_energy = "Бензин"
bmw_fuel = 7
bwm_budget = 2500
mercedes_marka = "Mercedes_Benz"
mercedes_speed = "165-310"
mercedes_power = "435"
mercedes_diametr = "16-19"
mercedes_energy = "Бензин"
mercedes_fuel = 7
mercedes_budget = 3100
nissan_marka = "Nissan Qashqai"
nissan_speed = "173-206"
nissan_power = "144"
nissan_diametr = "15-18"
nissan_energy = "Бензин"
nissan_fuel = 7
nissan_budget = 2350
subaru_marka = "Subaru Impreza"
subaru_speed = "164-255"
subaru_power = "90-250"
subaru_diametr = "17-21"
subaru_energy = "Бензин"
subaru_fuel = 7
subaru_budget = 3300
class Car:
    def __init__(self, marka,  speed, power, diametr, energy, fuel, budget):
        self.marka = marka
        self.speed = speed
        self.power = power
        self.diametr = diametr
        self.energy = energy
        self.fuel = fuel
        self.budget = budget
        self.all_speed = 0
        self.engine = False
    def __str__(self):
        return f"Марка машины: {self.marka},\nСкорость разгона машины: {self.speed},\nКоличество конских сил: {self.power},\nДиаметр колеса: {self.diametr},\nТип двигателя: {self.energy}"
    def start_engine(self):
        self.engine = True
        print(f"Двигатель {self.marka} запущен")
    def stop_engine(self):
        self.engine = False
        print(f"Двигатель {self.marka} остановлен")
    def stop_run(self, number):
        if self.engine:
            self.all_speed -= number
            print(f"{self.marka} Тормозит до {self.all_speed}")
    def fast_run(self, number):
        if self.engine:
            self.all_speed += number
            print(f"{self.marka} Разгоняеться до {self.all_speed}")
        else:
            print(f"{self.marka} Неможет разогнаться когда двигатель заглушон")
    def score_money(self, distance):
        money = 40
        fuel_need = ((distance / 100) * self.fuel) * money
        if self.budget >= fuel_need:
            change = self.budget - fuel_need
            station = change / money
            print("Денег на", distance, "km", "Хватает")
            print("Сдача после поездки: ", change, "\nНа заправке машина может заправиться:", station, "л")
        else:
            print("Денег нa", distance, "km", "Не хватает")
        print("Стоимость поездки: ", fuel_need)

toyota = Car(toyota_marka, toyota_speed, toyota_power, toyota_diametr, toyota_energy, toyota_fuel, toyota_budget)
#print(toyota)
#toyota.score_money(1000)
toyota.start_engine()
toyota.fast_run(250)
toyota.stop_run(30)
toyota.stop_engine()
bmw = Car(bmw_marka, bmw_speed, bmw_power, bmw_diametr, bmw_energy, bmw_fuel, bwm_budget)
#print(bmw)
#bmw.score_money(1000)
bmw.fast_run(260)
mercedes = Car(mercedes_marka, mercedes_speed, mercedes_power, mercedes_diametr, mercedes_energy, mercedes_fuel, mercedes_budget)
#print(mercedes)
#mercedes.score_money(1000)
nissan = Car(nissan_marka, nissan_speed, nissan_power, nissan_diametr, nissan_energy, nissan_fuel, nissan_budget)
#print(nissan)
#nissan.score_money(1000)
subaru = Car(subaru_marka, subaru_speed, subaru_power, subaru_diametr, subaru_energy, subaru_fuel, subaru_budget)
#print(subaru)
#subaru.score_money(1000)