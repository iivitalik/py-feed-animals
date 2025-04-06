from typing import List


class Animal:
    def __init__(
        self,
        name: str,
        appetite: int,
        is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"{self.name} is eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite

        print(f"{self.name} is not hungry.")
        return 0

    def __str__(self) -> str:
        return (f"{self.__class__.__name__}('{self.name}', "
                f"Hungry: {self.is_hungry})")


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print(f"{self.name} says: The hunt began!")


class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        print(f"{self.name} says: The slippers delivered!")


def feed_animals(animals: List[Animal]) -> int:
    sum_food_points = 0
    for animal in animals:
        sum_food_points += animal.feed()
    return sum_food_points


if __name__ == "__main__":
    cat1 = Cat("Whiskers")
    dog1 = Dog("Buddy")
    cat2 = Cat("Luna", is_hungry=False)
    dog2 = Dog("Max")

    animals = [cat1, dog1, cat2, dog2]

    for animal in animals:
        animal.print_name()

    print("\n--- Feeding animals ---")
    total_food = feed_animals(animals)
    print(f"\nTotal food consumed: {total_food} food points")

    print("\n--- Animal actions ---")
    cat1.catch_mouse()
    dog1.bring_slippers()
