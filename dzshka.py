from collections import UserDict
from datetime import datetime
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Birthday(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Date must be a string in the format DD.MM.YYYY")
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

 
class Phone(Field):
    def __init__(self, value):
           if not (len(value) == 10 and value.isdigit()):
               raise ValueError("нужно 10 цифр")
           super().__init__(value)
            

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
    
    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if not phone_obj:
            raise ValueError("Phone number not found.")
        self.add_phone(new_phone)
        self.remove_phone(old_phone)

        

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)
    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john) # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

 # Видалення запису Jane
book.delete("Jane")

date_input = input("Введите дату рождения (ДД.ММ.ГГГГ): ")

# Проверка формата перед созданием объекта
if not re.match(r"\d{2}\.\d{2}\.\d{4}", date_input):
    print("Ошибка: неверный формат даты!")
else:
    b = Birthday(date_input)
    print("Дата рождения: которуя я сам только что вписал 🤩>>>", b.value)