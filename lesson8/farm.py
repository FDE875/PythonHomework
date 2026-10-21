
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Color: {self.color}")


class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says: Moo!")

    def give_milk(self):
        print(f"{self.name} gives milk.")


class Sheep(Animal):
    def make_sound(self):
        print(f"{self.name} says: Baa!")

    def produce_wool(self):
        print(f"{self.name} produces wool.")


class Horse(Animal):
    def make_sound(self):
        print(f"{self.name} says: Neigh!")

    def run(self):
        print(f"{self.name} is running.")


# Create animal objects
cow = Cow("Bessie", 4, "White")
sheep = Sheep("Dolly", 2, "White")
horse = Horse("Spirit", 5, "Brown")

# Display information and behavior
animals = [cow, sheep, horse]

for animal in animals:
    print("\n--- Animal Information ---")
    animal.show_info()
    animal.eat()
    animal.sleep()
    animal.make_sound()

print()
cow.give_milk()
sheep.produce_wool()
horse.run()
