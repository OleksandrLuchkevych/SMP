import re
from datetime import datetime
from prettytable import PrettyTable
import os
from API.APIRepository import *
from loaders.savers import *
from pathlib import Path

class UserInterface:

    def __init__(self):
        self.repository = APIRepository()
        self.unit_of_work = UnitOfWork()

    def display_data(self, data, format="table"):
        if format == "table":
            table = PrettyTable()
            table.field_names = data[0].keys()
            for row in data:
                table.add_row(row.values())
            print(table)
        else:
            for row in data:
                print(row)

    def get_user_input(self):
        user_choice = input("Введіть 'posts' для перегляду постів або 'users' для перегляду користувачів: ").strip()
        if user_choice not in ['posts', 'users']:
            print("Неправильний вибір. Спробуйте ще раз.")
            return self.get_user_input()
        return user_choice

    def parse_input(self, input_string):
        date_pattern = r'\d{4}-\d{2}-\d{2}'
        if re.match(date_pattern, input_string):
            return datetime.strptime(input_string, '%Y-%m-%d').date()
        return input_string

    def save_data(self, data):
        path = Path('./source/')
        filename_base = input("Введіть ім'я файлу для збереження даних (без розширення): ").strip()

        self.unit_of_work.save_to_json(data, path / f"{filename_base}.json")
        self.unit_of_work.save_to_csv(data, path / f"{filename_base}.csv", fieldnames=data[0].keys())
        self.unit_of_work.save_to_txt([str(row) for row in data], path / f"{filename_base}.txt")

        print(f"Дані збережені у файлах {filename_base}.json, {filename_base}.csv та {filename_base}.txt.")

    def view_history(self):
        if os.path.exists("./source/history.txt"):
            with open("./source/history.txt", "r") as file:
                print(file.read())
        else:
            print("Історія порожня.")

    def log_history(self, data):
        with open("./source/history.txt", "a") as file:
            file.write(f"{datetime.now()}: {data}\n")