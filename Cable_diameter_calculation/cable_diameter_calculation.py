import json
import math


def main():
    print('Введите количество типов проводов: ', end='')
    n_type_wires = int(input())  # количество типов проводов
    if n_type_wires == 0:
        main()
    n_wires = 0  # общее число проводов
    d_wires = []  # список диаметров проводов
    for i in range(n_type_wires):
        print(f'Введите обозначение провода №{i + 1} (например МГТФ 0,03 или МС 16-15 2х0,2): ', end='')
        my_wire = input()
        my_wire_checked = check_name_wire(my_wire)  # вызов функции корректности ввода
        d_wire = define_wire_params(my_wire_checked)  # вызов функции определения диаметра данного провода из json файла
        d_wires.append(d_wire)
        # print(d_wires)
        print('Введите количество проводов данного типа: ', end='')
        n_wire = int(input())  # количество проводов данного типа
        n_wires += n_wire  # прибавляем к общему количеству проводов
        # print(n_wires)
    d_jgut = 1.25 * math.sqrt(n_wires) * sum(d_wires)/len(d_wires)
    print(f'Диаметр жгута: {round(d_jgut, 1)}\n')
    what_to_do_next()  # вызов функции о дальнейшем действии


def check_name_wire(my_wire):
    """функция проверки на: регистр букв, точка или запятая"""
    find_space = my_wire.find(' ')
    my_wire_name = my_wire[:find_space].upper()
    # print(my_wire_name)
    my_wire_type = my_wire[find_space:].replace('.', ',')
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
