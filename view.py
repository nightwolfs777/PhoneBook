import text
from model import PhoneBook


def main_menu() -> int:
    for n, item in enumerate(text.main_menu):
        if n == 0:
            print(item)
        else:
            print(f'\t{n}. {item}')
    while True:
        choice = input(text.main_menu_choice)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(f'Введите пункт меню от 1 до {len(text.main_menu) - 1}')


def show_contacts(p_book: PhoneBook, error_message: str):
    max_size = p_book.max_len()
    if p_book:
        print('\n' + '=' * (sum(max_size) + 7))
        for n, contact in p_book.phonebook.items():
            print(
                f'{n:>3}.{contact.name:<{max_size[0]}} {contact.phone:<{max_size[1]}} {contact.comment:<{max_size[2]}}')
        print('=' * (sum(max_size) + 7) + '\n')
    else:
        print_message(error_message)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def add_contact(message: list[str], contact: list[str] = None):
    contact = contact if contact else ['', '', '']
    for n, mes in enumerate(message):
        field = input(mes)
        contact[n] = field if field else contact[n]
    return contact


def input_data(message: str) -> str:
    return input(message)
