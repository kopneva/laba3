menu = {
    "торт": [["Слоеный", "Шоколадный"], 2.5, 500],
    "пирожное": [["Ванильное", "Фруктовое"], 1, 300],
    "маффин": [["Шоколадный", "Ягодный"], 0.8, 200]
}

def display_description():
    for item, details in menu.items():
        print(f"{item}: {details[0]}")

def display_price():
    for item, details in menu.items():
        print(f"{item}: {details[1]}")

def display_quantity():
    for item, details in menu.items():
        print(f"{item}: {details[2]} г")

def display_all_information():
    for item, details in menu.items():
        print(f"{item}: {details[0]}, Цена: {details[1]}, Вес: {details[2]} г")

def buy_item(item, quantity):
    if item in menu:
        if quantity <= 0:
            print("Количество товара должно быть положительным")
        elif menu[item][2] >= int(quantity):
            try:
                price = float(menu[item][1]) * (int(quantity) / 100)
            except ValueError:
                print("Цена должна быть числом")
                return
            menu[item][2] -= int(quantity)
            print(f"Покупка совершена. Цена: {price} руб. Осталось: {menu[item][2]} г")
        else:
            print("Недостаточно товара на складе")
    else:
        print("Такого товара нет в меню")

while True:
    print("Меню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        display_description()
    elif choice == "2":
        display_price()
    elif choice == "3":
        display_quantity()
    elif choice == "4":
        display_all_information()
    elif choice == "5":
        item = input("Введите название продукции: ")
        if item == 'п':
            break
        try:
            quantity = int(input("Введите нужный вес: "))
            buy_item(item, quantity)
        except ValueError:
            print("Вес должен быть цифрой")
    elif choice == "6":
        break
    else:
        print("Неверный пункт меню")

print("До свидания!")

