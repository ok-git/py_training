"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру, например словарь.
"""

from abc import ABC


class Warehouse:
    def __init__(self):
        self.total_equipment = 0

    def set_location(self):
        pass

    @staticmethod
    def __location_validation():
        pass


class OfficeEquipment(ABC):
    def __init__(self, equip_type, model, inventory_number):
        self.equip_type = equip_type
        self.model = model
        self.inventory_number = inventory_number
        self.location = None

    def quantity(self):
        pass

class Printer(OfficeEquipment):
    def __init__(self, equip_type, model, inventory_number, cartridge_model):
        super().__init__(equip_type, model, inventory_number)
        self.cartridge_model = cartridge_model


class Scanner(OfficeEquipment):
    def __init__(self, equip_type, model, inventory_number, lamp_model):
        super().__init__(equip_type, model, inventory_number)
        self.lamp_model = lamp_model


class Copier(OfficeEquipment):
    def __init__(self, equip_type, model, inventory_number, paper_tray_model):
        super().__init__(equip_type, model, inventory_number)
        self.paper_tray_model = paper_tray_model
