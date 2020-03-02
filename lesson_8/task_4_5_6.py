"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру, например словарь.
Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""

from abc import ABC, abstractmethod


class Warehouse:
    __locations_list = []

    def __init__(self):
        self.__equipment_dict = {}  # {location, equipment_list}

    @classmethod
    def add_location(cls, *args):
        cls.__locations_list.extend(args)

    @classmethod
    def del_location(cls, location):
        cls.__locations_list.remove(location)

    @classmethod
    def get_locations(cls):
        return cls.__locations_list

    def add_equipment(self, equipment, location):
        if location in self.get_locations():
            self.__equipment_dict.setdefault(location, []).append(equipment)
        else:
            self.print_msg(location)

    def move_equipment(self, equipment, old_location, new_location):
        if new_location in self.get_locations():
            self.__equipment_dict[old_location].remove(equipment)
            self.__equipment_dict.setdefault(new_location, []).append(equipment)
        else:
            self.print_msg(new_location)

    def del_equipment(self, equipment, location):
        self.__equipment_dict[location].remove(equipment)

    def get_equipment_list(self, location=None):
        if not location:
            return self.__equipment_dict
        elif location in self.get_locations():
            return self.__equipment_dict.setdefault(location, [])
        else:
            self.print_msg(location)

    @staticmethod
    def print_msg(text):
        print(f'Локации "{text}" на складе не существует')


class OfficeEquipment(ABC):
    __total_equipment = 0

    def __init__(self, equip_type, model, inventory_number):
        self.equip_type = equip_type
        self.model = model
        self.inventory_number = inventory_number
        self.__update_total_equipment()

    @classmethod
    def __update_total_equipment(cls):
        cls.__total_equipment += 1

    @classmethod
    def get_total_equipment(cls):
        return cls.__total_equipment

    @abstractmethod
    def service_works(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, equip_type, model, inventory_number, cartridge_model):
        super().__init__(equip_type, model, inventory_number)
        self.cartridge_model = cartridge_model

    def service_works(self):
        print('Регламент сервисных работ для принтеров')

    def __str__(self):
        return f'{self.equip_type}: {self.model}, {self.inventory_number}, {self.cartridge_model}'

    def __repr__(self):
        return f'{self.equip_type}: {self.model}, {self.inventory_number}, {self.cartridge_model}'


class Scanner(OfficeEquipment):
    def __init__(self, equip_type, model, inventory_number, lamp_model):
        super().__init__(equip_type, model, inventory_number)
        self.lamp_model = lamp_model

    def service_works(self):
        print('Регламент сервисных работ для сканеров')

    def __str__(self):
        return f'{self.equip_type}: {self.model}, {self.inventory_number}, {self.lamp_model}'

    def __repr__(self):
        return f'{self.equip_type}: {self.model}, {self.inventory_number}, {self.lamp_model}'


class Copier(OfficeEquipment):
    def __init__(self, equip_type, model, inventory_number, paper_tray_model):
        super().__init__(equip_type, model, inventory_number)
        self.paper_tray_model = paper_tray_model

    def service_works(self):
        print('Регламент сервисных работ для копиров')

    def __str__(self):
        return f'{self.equip_type}: {self.model}, {self.inventory_number}, {self.paper_tray_model}'

    def __repr__(self):
        return f'{self.equip_type}: {self.model}, {self.inventory_number}, {self.paper_tray_model}'


def separator():
    print('-' * 40)


wh = Warehouse()  # init warehouse object
# setup locations
wh.add_location('бухгалтерия', 'технический отдел', 'коммерческий отдел', 'склад')
wh.del_location('бухгалтерия')  # del location
print(f'\nСписок созданных локаций оборудования {wh.get_locations()}')
separator()

# create equipment
prn_1 = Printer('printer', 'hp', 'inv-prn-1000', 'hp-cart-1')
prn_2 = Printer('printer', 'hp', 'inv-prn-1001', 'hp-cart-1')
prn_3 = Printer('printer', 'epson', 'inv-prn-1002', 'eps-cart-10')
prn_4 = Printer('printer', 'lexmark', 'inv-prn-1003', 'lx-cart-20')
scn_1 = Scanner('сканер', 'epson', 'inv-scn-2000', 'lamp-111')
cpr_1 = Copier('копир', 'xerox', 'inv-cpr-3000', 'xr-paper-tray-100')
cpr_2 = Copier('копир', 'xerox', 'inv-cpr-3001', 'xr-paper-tray-100')

print('Всего создано оргтехники по типам:')
print(f'Принтеры - {Printer.get_total_equipment()} шт.')
print(f'Сканеры - {Scanner.get_total_equipment()} шт.')
print(f'Копиры - {Copier.get_total_equipment()} шт.')
separator()

prn_1.service_works()
scn_1.service_works()
cpr_1.service_works()
separator()

# add equipment to locations
wh.add_equipment(prn_1, 'коммерческий отдел')
wh.add_equipment(prn_2, 'коммерческий отдел')
wh.add_equipment(prn_3, 'технический отдел')
wh.add_equipment(prn_4, 'склад')
wh.add_equipment(scn_1, 'технический отдел')
wh.add_equipment(cpr_1, 'технический отдел')
wh.add_equipment(cpr_2, 'коммерческий отдел')

print('Распределение техники по отделам:')
for key, value in wh.get_equipment_list().items():
    print(key, value)
separator()

# move prn_4 from old_location to new_location
wh.move_equipment(prn_4, 'склад', 'коммерческий отдел')

print('Распределение техники по отделам после перемещения:')
for key, value in wh.get_equipment_list().items():
    print(key, value)
separator()

# move to invalid location
wh.move_equipment(prn_4, 'коммерческий отдел', 'бухгалтерия')
