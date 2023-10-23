class Car:
    total_cars = 0

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_running = False

    def start_engine(self):
        self.engine_running = True

    def stop_engine(self):
        self.engine_running = False

    @staticmethod
    def car_info(brand, model):
        print(f"Это автомобиль марки {brand} модели {model}")

    def print_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Двигатель работает: {'Да' if self.engine_running else 'Нет'}")


def get_valid_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Некорректный ввод. Попробуйте еще раз.")


brand = get_valid_input("Введите марку автомобиля: ")
model = get_valid_input("Введите модель автомобиля: ")

car1 = Car(brand, model)

car1.print_info()

car1.start_engine()
print("Двигатель заведен")

car1.print_info()

brand = get_valid_input("Введите марку автомобиля: ")
model = get_valid_input("Введите модель автомобиля: ")

car2 = Car(brand, model)

print("Количество созданных автомобилей:", Car.get_total_cars())

Car.car_info("BMW", "X5")