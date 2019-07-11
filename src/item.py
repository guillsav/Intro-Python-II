class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def can_eat(self):
        return False

    def __str__(self):
        return "{self.name} {self.description}".format(self=self)


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories

    def can_eat(self):
        return True


class Safe(Item):
    def __init__(self, name, description, contains):
        super().__init__(name, description)
        self.contains = contains

    def can_open(self):
        return True
