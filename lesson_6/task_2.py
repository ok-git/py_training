"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    asphalt_per_sqmeter = 25

    def __init__(self, road_length, road_width, thickness=5):
        self._road_length = road_length
        self._road_width = road_width
        self._thickness = thickness

    def calc(self):
        return self._road_length*self._road_width*self._thickness*self.asphalt_per_sqmeter


a = Road(5000, 20)
print(f'Масса асфальта {a.calc()} кг.')
