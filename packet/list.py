#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def listt(students):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "Успеваемость"
        )
    )
    print(line)

    # Вывести данные о всех студентах.
    for idx, student in enumerate(students, 1):
        ma = student.get('mark', '')
        print(
            '| {:^4} | {:<30} | {:<20} | {}.{}.{}.{}.{:<7} |'.format(
                idx,
                student.get('name', ''),
                student.get('group', ''),
                ma[0],
                ma[1],
                ma[2],
                ma[3],
                ma[4]
            )
        )
        print(line)