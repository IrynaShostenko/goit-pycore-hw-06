"""Розроблюємо систему для управління адресною книгою"""

from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Клас для зберігання імені контакту
    pass

class Phone(Field):
    # Клас для зберігання номера телефону з валідацією
    def __init__(self, value):
        # Перевіряємо правильність номера перед збереженням
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        # Перевіряємо, що номер складається з 10 цифр
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Веедіть коректний номер телефону, він повинен містити 10 цифр")

class Record:
    # Клас для зберігання контакту із ім'ям та списком телефонів, також містить методи для додавання, видалення та редагування телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Додаємо телефон до списку
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Видаляємо телефон зі списку
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        # Замінюємо старий номер на новий
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone):
        # Шукаємо конкретний номер серед телефонів
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        # Повертає інформацію про контакт у вигляді рядка
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # Клас для зберігання адресної книги
    def add_record(self, record):
        # Додаємо новий контакт до адресної книги за ім'ям контакту
        self.data[record.name.value] = record

    def find(self, name):
        # Шукаємо контакт за ім'ям
        return self.data.get(name, None)

    def delete(self, name):
        # Видаляємо контакт за ім'ям
        if name in self.data:
            del self.data[name]