import json
import math


def main():
    print('Введите количество типов проводов: ', end='')
    n_type_wires = input()  # количество типов проводов
    try:
        n_type_wires = int(n_type_wires)
        if n_type_wires == 0:
            main()
    except ValueError:
        main()
    n_wires = 0  # общее число проводов
    d_wires = []  # список диаметров проводов
    for i in range(n_type_wires):
        print(f'Введите обозначение провода №{i + 1} (например МГТФ 0,03 или МС 16-15 2х0,2): ', end='')
        my_wire = input()
        my_wire_checked = check_name_wire(my_wire)  # вызов функции корректности ввода
        d_wire = define_wire_params(my_wire_checked)  # вызов функции определения диаметра данного провода из json файла
        print('Введите количество проводов данного типа: ', end='')
        n_wire = int(input())  # количество проводов данного типа
        n_wires += n_wire  # прибавляем к общему количеству проводов
        for _ in range(n_wire):
            d_wires.append(d_wire)  # добавляем диаметр каждого провода в список диаметров
        # print(d_wires)
        # print(n_wires)
    diam_sredniy = sum(d_wires) / len(d_wires)  # среднее арифметическое значение диаметра провода, мм
    if len(d_wires) == 1:
        diametr_jguta = math.sqrt(n_wires) * diam_sredniy
    else:
        diametr_jguta = 1.25 * math.sqrt(n_wires) * diam_sredniy
    print(f'Диаметр жгута: {round(diametr_jguta, 1)} мм\n')
    what_to_do_next()  # вызов функции о дальнейшем действии


def check_name_wire(my_wire):
    """функция проверки на: регистр букв, точка или запятая"""
    find_space = my_wire.find(' ')
    my_wire_name = my_wire[:find_space].upper()
    # print(my_wire_name)
    my_wire_type = my_wire[find_space:].replace('.', ',').replace('x', 'х')
    my_wire = my_wire_name + my_wire_type
    # print('type:', my_wire)
    return my_wire


def define_wire_params(my_wire):
    """функция поиска введенного провода в json файле"""
    for k, v in data_json.items():
        if k == my_wire:
            find_space = v['Наружный диаметр'].find(' ')
            diam_wire = v['Наружный диаметр'][:find_space].replace(',', '.')
            # print(diam_wire)
            try:
                return float(diam_wire)
            except ValueError:
                find_x = v['Наружный диаметр'].find('х')
                diam_wire = v['Наружный диаметр'][(find_x + 1):find_space].replace(',', '.')
                # print(f'd = {diam_wire}')
                return float(diam_wire)
    else:
        print('''
        Такого провода не существует.
        Начните сначала.
        ''')
        main()


def what_to_do_next():
    """функция спрашивает что делать дальше"""
    print('''
    Нажмите 1 - посчитать еще.
    Нажмите 2 - выход.''')
    what_to_do = input()
    if what_to_do == '1':
        main()
    elif what_to_do == '2':
        exit()
    else:
        what_to_do_next()


if __name__ == '__main__':
    with open('wires.json', encoding='utf-8') as file:
        data_json = json.load(file)
    main()
