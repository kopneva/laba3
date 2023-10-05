def is_valid_surname(surname):
    return surname.isalpha()


def is_valid_balance(balance):
    if balance.startswith('-'):      #если ввод только полож баланс
        return balance[1:].isdigit()      #если ввод только полож баланс
    return balance.isdigit()

def is_valid_date(date):
    if len(date) != 10 or date[2] != date[5] != '.' or not date[:2].isdigit() or not date[3:5].isdigit() or not date[
                                                                                                                6:].isdigit():
        return False
    return True


def get_user_data():
    while True:
        surname = input("Введите фамилию: ")
        if is_valid_surname(surname):
            break
        else:
            print("Фамилия должна содержать только буквы, попробуйте еще раз.")

    while True:
        balance = input("Введите баланс: ")
        if is_valid_balance(balance):
            break
        else:
            print("Баланс должен содержать только цифры, попробуйте еще раз.")
    while True:

        date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
        if is_valid_date(date):
            break
        else:
            print("Дата должна быть в формате ДД.ММ.ГГГГ, попробуйте еще раз.")

    return surname, balance, date


def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')


def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


def get_zero_balance_surnames(filename):
    zero_balance_surnames = []
    lines = read_file(filename)
    for line in lines:
        surname, balance, _ = line.split()
        if int(balance) == 0:
            zero_balance_surnames.append(surname)
    return zero_balance_surnames


def get_total_balance(filename):
    total_balance = 0
    lines = read_file(filename)
    for line in lines:
        _, balance, _ = line.split()
        total_balance += int(balance)
    return total_balance


def main():
    filename = 'Клиент банка.txt'

    while True:
        choice = input(
            "Выберите действие:\n1. Ввести информацию о клиенте\n2. Вывести фамилии клиентов с нулевым балансом\n3. Вывести общую сумму вложений клиентов\n4. Выйти\n")

        if choice == '1':
            surname, balance, date = get_user_data()
            data = f"{surname} {balance} {date}"
            write_to_file(filename, data)
            print("Информация о клиенте успешно добавлена.")
        elif choice == '2':
            zero_balance_surnames = get_zero_balance_surnames(filename)
            if zero_balance_surnames:
                print("Фамилии клиентов с нулевым балансом:")
                for surname in zero_balance_surnames:
                    print(surname)
            else:
                print("Нет клиентов с нулевым балансом.")
        elif choice == '3':
            total_balance = get_total_balance(filename)
            print(f"Общая сумма вложений всех клиентов: {total_balance}")
        elif choice == '4':
            break
        else:
            print("Некорректный выбор, попробуйте еще раз.")

if __name__ == "__main__":
    main()