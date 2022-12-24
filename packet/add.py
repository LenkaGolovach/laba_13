#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add(students):
    # Запросить данные о студенте.
    name = input("Фамилия и инициалы? ")
    group = input("Номер группы? ")
    progress = [
        int(input("Оценка за 1 семестр")),
        int(input("Оценка за 2 семестр")),
        int(input("Оценка за 3 семестр")),
        int(input("Оценка за 4 семестр")),
        int(input("Оценка за 5 семестр"))
    ]
    # Создать словарь.
    student = {
        'name': name,
        'group': group,
        'mark': progress
    }
    # Добавить словарь в список.
    students.append(student)
    if len(students) > 1:
        students.sort(key=lambda item: item.get('group')[::-1])
    return students