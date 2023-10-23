class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашом")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")


# Создание экземпляра класса Stationery
stationery = Stationery("Канцелярская принадлежность")

# Вызов метода draw для экземпляра Stationery
stationery.draw()

# Создание экземпляра класса Pen
pen = Pen("Ручка")

# Вызов метода draw для экземпляра Pen
pen.draw()

# Создание экземпляра класса Pencil
pencil = Pencil("Карандаш")

# Вызов метода draw для экземпляра Pencil
pencil.draw()

# Создание экземпляра класса Handle
handle = Handle("Маркер")

# Вызов метода draw для экземпляра Handle
handle.draw()