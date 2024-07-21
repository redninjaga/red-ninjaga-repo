import pygame

toyota_marka = "Toyota_Supra"
toyota_speed = "220-266"
toyota_power = "105-387"
toyota_diametr = "15-19"
toyota_energy = "Бензин"
bmw_marka = "BMW_M3"
bmw_speed = "227-302"
bmw_power = "195-510"
bmw_diametr = "17-20"
bmw_energy = "Бензин"
mercedes_marka = "Mercedes_Benz"
mercedes_speed = "165-310"
mercedes_power = "435"
mercedes_diametr = "16-19"
mercedes_energy = "Бензин"
nissan_marka = "Nissan Qashqai"
nissan_speed = "173-206"
nissan_power = "144"
nissan_diametr = "15-18"
nissan_energy = "Бензин"
subaru_marka = "Subaru Impreza"
subaru_speed = "164-255"
subaru_power = "90-250"
subaru_diametr = "17-21"
subaru_energy = "Бензин"
class Car:
    def __init__(self, marka,  speed, power, diametr, energy):
        self.marka = marka
        self.speed = speed
        self.power = power
        self.diametr = diametr
        self.energy = energy
    def __str__(self):
        return f"Марка машины: {self.marka},\nСкорость разгона машины: {self.speed},\nКоличество конских сил: {self.power},\nДиаметр колеса: {self.diametr},\nТип двигателя: {self.energy}"


toyota = Car(toyota_marka, toyota_speed, toyota_power, toyota_diametr, toyota_energy)
print(toyota)
bmw = Car(bmw_marka, bmw_speed, bmw_power, bmw_diametr, bmw_energy)
print(bmw)
mercedes = Car(mercedes_marka, mercedes_speed, mercedes_power, mercedes_diametr, mercedes_energy)
print(mercedes)
nissan = Car(nissan_marka, nissan_speed, nissan_power, nissan_diametr, nissan_energy)
print(nissan)
subaru = Car(subaru_marka, subaru_speed, subaru_power, subaru_diametr, subaru_energy)
print(subaru)




