"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} едет')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости (лимит 60 км/ч)')


class SportCar(Car):
    def __init__(self, speed, color, name, nitro=True):
        super().__init__(speed, color, name)
        self.nitro = nitro

    def start_nitro(self):
        if self.nitro:
            print('Старт Nitro')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости (лимит 40 км/ч)')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_car = TownCar(65, 'зелёный', 'Волга')
print(town_car.name, town_car.color, town_car.speed, town_car.is_police)
town_car.go()
town_car.show_speed()
town_car.turn('налево')
town_car.stop()
print()

sport_car = SportCar(225, 'жёлтый', 'Camaro')
print(sport_car.name, sport_car.color, sport_car.speed, sport_car.is_police, sport_car.nitro)
sport_car.go()
sport_car.start_nitro()
sport_car.show_speed()
sport_car.turn('направо')
sport_car.stop()
print()

work_car = WorkCar(45, 'белый', 'Largus')
print(work_car.name, work_car.color, work_car.speed, work_car.is_police)
work_car.go()
work_car.show_speed()
work_car.turn('налево')
work_car.stop()
print()

police_car = PoliceCar(70, 'серый', 'УАЗ')
print(police_car.name, police_car.color, police_car.speed, police_car.is_police)
police_car.go()
police_car.show_speed()
police_car.turn('налево')
police_car.stop()
