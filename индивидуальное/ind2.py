#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from packet.add import add
from packet.list import listt
from packet.select import selectt
from packet.help_1 import help_1


def main():
    # Список студентов.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            students = add(students)
        elif command == 'list':
            listt(students)
        elif command.startswith('select'):
            selectt(students)
        elif command == 'help':
            help_1()
        else:
            print("неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()