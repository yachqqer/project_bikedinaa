
# Создайте класс "Фрукт", который содержит информацию о наименовании и весе фрукта.
# Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса "Фрукт" и содержат информацию о цвете.

class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Apple(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

class Orange(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

apple = Apple(name='Лагуна', weight=0.2, color='Красный')
orange = Orange(name='Летний', weight=0.5, color='Оранжевый')

print(f"фрукт: {apple.name}, вес: {apple.weight}, цвет: {apple.color}")
print(f"фрукт: {orange.name}, вес: {orange.weight}, цвет: {orange.color}")