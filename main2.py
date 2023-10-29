from collections import UserDict

def has_key(func):
    def wraper(*arg, **kwarg):
        try:
            return func(*arg, **kwarg)
        except KeyError:
            print('Key not found.')
    return wraper

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, phone):
        if len(phone) != 10:
            raise ValueError(f'{self.__class__} -> Must be 10 number')
        super().__init__(phone)

    def edit(self, phone:str) -> None:
        self.value = phone
        print('Number were aded')

class Record:
    def __init__(self, name):
        self.name:Name = Name(name)
        self.phones:list[Phone] = []

    def add_phone(self, phone:str) -> None:
        try:
            self.phones.append(Phone(phone))
        except:
            print('Error length number. Must be 10 numbers.')

    def remove_phone(self, phone:str) -> None:
        for n, p in enumerate(self.phones):
            if p.value == phone:
                del self.phones[n]

    def edit_phone(self, old_phone:str, new_phone:str) -> None:
        for n, p in enumerate(self.phones):
            if p.value == old_phone:
                p.edit(new_phone)

    def find_phone(self, phone:str) -> str:
        for p in self.phones:
            if p.value == phone:
                return p
        return 'Not found.'

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record:Record) -> None:
        self.data[record.name.value] = record

    @has_key
    def find(self, name:str) -> Record:
        return self.data[name]

    @has_key  
    def delete(self, name:str) -> None:
        del self.data[name]
        print(f'Record {name} was deleted.')
        
# book = AddressBook()
Lisa = Record('Lisa')
# Lisa.add_phone('1234567890')
# Lisa.add_phone('3242344324')
# Lisa.add_phone('5467456456')
# Lisa.add_phone('045656')
# Lisa.add_phone('1111111111')
# print(Lisa.find_phone('0661366855'))
# # print(Lisa)
# # Phone('1234')
# book.add_record(Lisa)
# print(book.data['Lisa'])
# print(book.find('Lisa'))
# book.delete('alsd')

book = AddressBook()

book.data['Lisa'] = Lisa

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
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
print(book)