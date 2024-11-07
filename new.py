class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False  # Накормленное
        self.name = name  # Имя животного

    def eat(self, food):
        if not self.alive:
            print(f"{self.name} мертв и не может есть.")
            return

        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность
        self.name = name  # Имя растения


class Mammal(Animal):
    pass  # Можно добавить специфичные для млекопитающих методы


class Predator(Animal):
    pass  # Можно добавить специфичные для хищников методы


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем на съедобное


# Создание объектов классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка атрибутов
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Действия
a1.eat(p1)  # Хищник пытается съесть цветок
a2.eat(p2)  # Млекопитающее ест фрукт

# Проверка состояния после попытки еды
print(a1.alive)
print(a2.fed)