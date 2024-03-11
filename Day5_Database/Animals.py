class Animal:

    def __init__(self, name: str, sound: str, age: int) -> None:
        self.name = name
        self.sound = sound
        self.age = age

    def __str__(self) -> str:
        return f"The {self.name} goes {self.sound}"
