"""
4
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
"""


import copy


class OfficeEquipment:

    def __init__(self, eq_type: str, model: str, paper_size: str):
        self.__eq_type = eq_type
        self.__model = model
        self.__paper_size = paper_size

    @property
    def get_main_info(self):
        """
        Method returns main info about equipment
        :return: main info about equipment
        """
        return {'type': self.__eq_type, 'model': self.__model}


class Printer(OfficeEquipment):

    def __init__(self, model: str, print_speed: str, paper_size: str = 'A4',
                 print_technology: str = 'laser', is_color: bool = False):
        super().__init__(eq_type='printer', model=model, paper_size=paper_size)
        self.print_technology = print_technology
        self.print_speed = print_speed
        self.is_color = is_color


class Scanner(OfficeEquipment):

    def __init__(self, model: str, optical_resolution: str,
                 sensor_type: str, paper_size: str = 'A4'):
        super().__init__(eq_type='scanner', model=model, paper_size=paper_size)
        self.optical_resolution = optical_resolution
        self.sensor_type = sensor_type


class Xerox(OfficeEquipment):

    def __init__(self, model: str, max_copies_number: int,
                 cost_price: float, paper_size: str = 'A4'):
        super().__init__(eq_type='xerox', model=model, paper_size=paper_size)
        self.max_copies_number = max_copies_number
        self.cost_price = cost_price


# Ошибка инициализации экземпляра класса Store
class StoreInitializationError(Exception):

    def __init__(self, text: str = ''):
        self.text = text


# Ошибки связанные с манипуляцией со складом (добавление на склад или отправка со склада)
class StoreProcessingError(Exception):

    def __init__(self, text: str = ''):
        self.text = text


class Store:

    __slots__ = ('__name', '__capacity', '__catalog')

    __storages = {}                 # Список складов: {name: object}
    __general_equipment_types = []  # Список типов техники, которые могут размещаться на всех складах

    def __init__(self, name: str, capacity: int, *args):
        """
        Store class instance constructor
        :param name: name of store
        :param capacity: amount of equipment that can be placed in the store
        :param args: additional types of equipment for this store
        """
        # Проверяем есть ли уже такое наименование склада в списке складов
        if name not in Store.__storages:
            Store.__storages[name] = self
            self.__name = name
        else:
            raise StoreInitializationError('This name is already taken.\n')
        # вместимость склада (шт.)
        self.__capacity = capacity
        # каталог техники реализован в виде словаря:
        # {type: {model: [s/n]}}

        # На основании общего списка (general_equipment_types) и дополнительного списка (args)
        # допустимых типов техники формируется словарь, где уже указаны типы техники для этого склада.
        self.__catalog = {item: {} for item in (Store.__general_equipment_types + list(args))}

    # Допустимые типы техники
    def valid_eq_type(self):
        return self.catalog.keys()

    # Вывод информации о ттом, какая техника находится на складе
    def __str__(self):
        result = ''
        for i_type, models in self.catalog.items():
            result += f'Information about {i_type}s\n'
            for model, sn_list in models.items():
                result += f'Model {model}: {sn_list}\n'
        return result

    @classmethod
    def add_type(cls, eq_type: str) -> None:
        """
        Adding a type of equipment
        :param eq_type: type of equipment which need to add to the list
        :return: None
        """
        # Добавляем в список допустимых типов техники
        cls.__general_equipment_types.append(eq_type)
        # Обновляем информацию на всех складах
        for store in cls.__storages.values():
            store.catalog[eq_type] = {}

    @property
    def catalog(self):
        return self.__catalog

    # Добавление техники в список имеющегося на складе оборудования
    @catalog.setter
    def catalog(self, value: dict):
        """
        Setter for adding equipment to the store.
        :param value: dictionary: {'type': <eq type>, 'model': <model name>, 'sn': <sn list>}
        :return: None
        """
        if value['model'] in self.catalog[value['type']].keys():
            # Проверяем есть ли повторения между тем, что добавляется и тем, что уже есть на складе
            # Уникальность серийных номеров поддерживается в рамках конкретной модели
            if len(set(value['sn']) & set(self.catalog[value['type']][value['model']])) != 0:
                raise StoreProcessingError('S/n of the adding equipment is already in store.\n')
            self.catalog[value['type']][value['model']] += list(value['sn'])
        else:
            self.catalog[value['type']][value['model']] = copy.deepcopy(list(value['sn']))

    # Вычисление количества свободных мест на складе
    @property
    def free_volume(self):
        result = self.__capacity
        for item_type in self.catalog.values():
            for item_model in item_type.values():
                result -= len(item_model)
        return result

    def equipment_reception(self, equipment: OfficeEquipment, count: int, sn_list: set) -> None:
        """
        Adding equipment to the store.
        :param equipment: equipment class
        :param count: amount if equipment
        :param sn_list: s/n set of equipment
        :return: None
        """
        if not isinstance(equipment, OfficeEquipment):
            raise TypeError('Attempt to add non-technique')
        elif not isinstance(count, int):
            raise TypeError('Number of equipment must be an integer digit')
        elif count != len(sn_list):
            raise ValueError('Count of adding equipment and length of sn list must be equal')
        elif count > self.free_volume:
            raise StoreProcessingError('Store is full. Operation of adding canceled\n')
        else:
            tmp = {'sn': sn_list}
            tmp.update(equipment.get_main_info)
            # Может быть ошибка StoreProcessingError, если сеттер выявит повторение серийных номеров
            self.catalog = tmp

    def equipment_transfer(self, unit_initiator: str, *args: tuple) -> dict:
        """
        Transfer equipment to the units of organisation
        :param unit_initiator: unit customer
        :param args: equipment request (some number of tuples). Tuple: (equipment type, number)
        :return: a dictionary with response to the request.
                 Dictionary: {'initiator': <unit customer>, 'type': ['Comment of result', [sn list]] ...}
        """
        # Словарь с результатом запроса на получение техники
        response = {'initiator': unit_initiator}
        # Перебираем все кортежи в запросе.
        # В случае возникновения ошибки, указываем на каком кортеже возникла ошибка.
        # В этом случае данные будут обработаны до указанного в ошибке номера кортежа (не включительно).
        for i, item in enumerate(args, 1):
            # Если хотя бы один параметрбыл обработан корректно, то в строку с ошибкой (которая
            # потенциально может быть) добавляется информация о выполнении части запроса
            if i > 1:
                # В случае возникновения ошибки при обработке args в ошибку будет добавлена информация
                # о части выполненного запроса.
                error_str = f'Part of response which done before mistake: {response}\n'
            else:
                error_str = ''

            if (not isinstance(item, tuple)) | (len(item) != 2):
                raise ValueError(f"Request contains non-tuple data or tuple with wrong length.\n{error_str}")
            # Проверяем есть ли такой тип (допустим ли для этого склада) техники на складе
            elif item[0] not in self.catalog.keys():
                raise StoreProcessingError(f'Wrong type of equipment type.\n{error_str}')
            elif not isinstance(item[1], int):
                raise TypeError(f'Number of equipment must be an integer digit.\n{error_str}')
            else:
                # Начинаем формировать ответ на запрос
                # Ключ - тип техники. Значение - список, состоящий из комментария по результату и
                # списка с серийными номерами техники.
                response[item[0]] = ["", []]

                # Запоминаем количество требуемой техники
                tmp = item[1]
                # Список моделей техники, которые полностью будут отпарвлены на запрос (не останется
                # ни одного экземпляра) и, соответственно, должны быть удалены со склада
                pop_list = []
                # Перебираем все модели по требуемому типу техники
                for model, sn_list in self.catalog[item[0]].items():
                    # Если количество требуемой техники меньше чем имеется конкретной модели,
                    # то извлекаем требуемое количество техники, остальное оставляем.
                    if tmp < len(sn_list):
                        response[item[0]][1] += sn_list[:tmp]
                        self.catalog[item[0]][model] = sn_list[tmp:]
                        break
                    # Если количество требуемой техники совпадает с количеством имеющейся
                    # по конкретной модели, то забирается вся техника, а модель добавялется
                    # в список на удаление со склада.
                    elif tmp == len(sn_list):
                        response[item[0]][1] += sn_list
                        self.catalog[item[0]].pop(model)
                        break
                    # Если количество требуемой техники превышает количество техники модели.
                    else:
                        response[item[0]][1] += sn_list
                        tmp -= len(sn_list)
                        pop_list.append(model)
                        continue

                # Проверяем сколько техники было извлечено.
                # Если столько, сколько требовалось, значит все успешно. В комментарии пишем "успех".
                # Удаляем опустошенные модели.
                # Если нет, то указываем в комментарии, что получилось отправить меньшее количество
                # техники. Удаляем все модели по указанному типу техники, так как получается, что
                # вся техника была отправлена со склада.
                if len(response[item[0]][1]) == item[1]:
                    response[item[0]][0] = 'Successfull.'
                    for ind in pop_list:
                        self.catalog[item[0]].pop(ind)
                else:
                    response[item[0]][0] = f'Only {len(response[item[0]][1])} sent.'
                    self.catalog[item[0]].clear()

        return response


printer1 = Printer('LaserJet-101', '10 per minute')
printer2 = Printer('HP 23', '20 per minute')
printer3 = Printer('Canon M34', '30 per minute')
printer4 = Printer('HP 45', '20 per minute')

scanner1 = Scanner('MP 454', '5000 dpi', 'CIS')
scanner2 = Scanner('HP 8304', '3000 dpi', 'CIS')
scanner3 = Scanner('KW 22', '1000 dpi', 'CDC')

xerox1 = Xerox('Xerox 22', 10000, 2)
xerox2 = Xerox('HP 322', 15000, 1)
#-----
Store.add_type('printer')
storage1 = Store('main store', 35, 'xerox')
storage2 = Store('usual store', 5)
print(f'1: store1: {storage1.valid_eq_type()}, store2: {storage2.valid_eq_type()}')
Store.add_type('scanner')
print(f'2: store1: {storage1.valid_eq_type()}, store2: {storage2.valid_eq_type()}')

try:
    storage = Store('main store', 50)
except StoreInitializationError as sie:
    print('3(error):', sie)

try:
    storage2.equipment_reception(printer1, '10', {'2332', '32323', '32323'})
except TypeError as te:
    print('4(error):', te)

try:
    storage2.equipment_reception(printer1, 3, {'111', '222', '3333', '4444'})
except ValueError as ve:
    print('5(error):', ve)

try:
    storage2.equipment_reception(printer1, 6, {'1', '33', '444', '34234', '4444', '3434343'})
except StoreProcessingError as spe:
    print('6(error):', spe)

print('7')
print('Было места: ', storage2.free_volume)
storage2.equipment_reception(printer1, 3, {'1', '2', '3'})
print('Осталось места: ', storage2.free_volume)
print()

try:
    storage2.equipment_reception(printer1, 2, {'1', '23'})
except StoreProcessingError as spe:
    print('8(error):', spe)

print('9')
storage1.equipment_reception(printer1, 6, {'1', '11', '111', '1111', '11111', '111111'})
storage1.equipment_reception(printer2, 4, {'2', '22', '222', '2222'})
storage1.equipment_reception(printer3, 3, {'3', '33', '333'})
storage1.equipment_reception(printer4, 2, {'4', '44'})

storage1.equipment_reception(scanner1, 4, {'4', '44', '444', '4444'})
storage1.equipment_reception(scanner2, 3, {'5', '55', '555'})
storage1.equipment_reception(scanner3, 2, {'6', '66'})
print(storage1, '\n')
storage1.equipment_reception(xerox1, 3, {'7', '77', '777'})
storage1.equipment_reception(xerox2, 4, {'8', '88', '888', '8888'})
print(storage1)
print('Free volume: ', storage1.free_volume)
print()

try:
    result = storage1.equipment_transfer('HR', ['printer', 10])
except ValueError as ve:
    print('10(error):', ve)

try:
    result = storage1.equipment_transfer('HR', ('some_eq', 20))
except StoreProcessingError as spe:
    print('11(error):', spe)

print('12')
print(storage1)
print('Свободное место до передачи:', storage1.free_volume)
print('Результат запроса: ',storage1.equipment_transfer('HR', ('printer', 2), ('scanner', 2)))
print(storage1)
print('Свободное место после передачи:', storage1.free_volume)
print()

print('13')
# Передача техники:
# принтеров - меньше, чем в первой модели (LaserJet-101) экземпляров (должна остаться в списке).
# ксероксы - больше, чем всего есть
# сканеров - больше, чем есть в одной модели (MP 454)
print(storage1)
print('Результат запроса: ', storage1.equipment_transfer('PR', ('printer', 3), ('xerox', 10), ('scanner', 4)), '\n')
print(storage1)

print('14')
print(storage1)
try:
    print('Результат запроса: ', storage1.equipment_transfer('bookkeeping', ('printer', 2), 'wrong data', ('scanner', 2)))
except ValueError as ve:
    print(ve)
print(storage1)
