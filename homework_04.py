contacts = {}  

# Декоратор для обробки помилок введення користувача
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Цього контакту не існує."
        except ValueError:
            return "Невірний формат введення. Використовуйте 'ім'я та номер'."
        except IndexError:
            return "Невірний формат введення. Використовуйте 'ім'я та номер'."
    return wrapper

# Функція для виводу привітання
def say_hello():
    return "How can I help you?"

# Функція для додавання контакту
@input_error
def add_contact(data):
    name, phone = data.split(' ', 1)
    name = name.capitalize()
    if len(phone) < 10:
        return "Номер телефону повинен мати мінімум 10 символів."  
    contacts[name] = phone
    return f"Контакт {name} з номером {phone} доданий."

# Функція для зміни номера телефону існуючого контакту
@input_error
def change_contact(data):
    name, new_phone = data.split()
    name = name.capitalize()
    if name in contacts:
        contacts[name] = new_phone
        return f"Номер телефону для контакту {name} змінено на {new_phone}"
    else:
        return f"Контакт з ім'ям {name} не знайдений."

# Функція для виведення номера телефону для зазначеного контакту
@input_error
def get_phone(name):
    name = name.capitalize()
    if name in contacts:
        return f"Номер телефону для контакту {name}: {contacts[name]}"
    else:
        return f"Контакт з ім'ям {name} не знайдений"

# Функція для виведення всіх контактів
def show_all_contacts():
    if not contacts:
        return "Список контактів порожній."
    else:
        result = "Список всіх контактів та їх номерів телефонів:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result

# Функція для завершення роботи бота
def exit_bot():
    return "Good bye!"

# Головна функція бота
def main():
    instruction = """
    Вітаю! Я ваш бот-помічник. Ось, що я можу для вас зробити:

    1. Додавати контакти та номери телефонів. Для цього використовуйте команду 'add'. 
    
    2. Показувати вам список всіх контактів та їх номерів телефонів. 
    Для цього використовуйте команду 'show all'.

    3. Змінювати номер існуючого контакту. Використовуйте команду 'change'.

    4. Виводити номер телефону для зазначеного контакту. Використовуйте команду 'phone'.

    5. Для завершення роботи введіть, good bye, exit, close або вийти.

    Будь ласка, користуйтесь цими командами для взаємодії зі мною. 
    Я готовий допомогти вам у керуванні вашими контактами.
    """
    
    print(instruction)
    
    while True:
        user_input = input("Введіть команду: ").lower()

        if user_input in ('вийти', 'good bye', 'close', 'exit'):
            print(exit_bot())
            break
        elif user_input == '.':
            print("Good bye")
            break
        elif user_input == 'привіт' or user_input == 'hello':
            print(say_hello())
        elif user_input.startswith('add '):
            result = add_contact(user_input[4:])
            print(result)
        elif user_input.startswith('change '):
            result = change_contact(user_input[7:])
            print(result)
        elif user_input.startswith('phone '):
            result = get_phone(user_input[6:])
            print(result)
        elif user_input == 'show all':
            result = show_all_contacts()
            print(result)
        else:
            print("Спробуйте ще раз.")

if __name__ == "__main__":
    main()