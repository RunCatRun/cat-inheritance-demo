class Cat:
    """
    Базовый класс "Кот".
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def meow(self):
        """Метод мяуканья."""
        print(f"{self.name} мяукает.")

    def info(self):
        """Информация о коте."""
        print(f"Это кот по имени {self.name}, возраст: {self.age} лет.")


class BritishShorthair(Cat):
    """
    Производный класс, представляющий британского короткошёрстного кота.
    """

    def __init__(self, name: str, age: int, fur_color: str):
        super().__init__(name, age)  # вызываем конструктор родительского класса
        self.fur_color = fur_color   # добавляем уникальный атрибут

    def meow(self):
        """Переопределяем звук мяуканья."""
        print(f"{self.name}, британец, говорит: Мяяяу!")

    def groom(self):
        """Уникальный метод ухода за шерстью."""
        print(f"{self.name} аккуратно умывается.")


class Sphynx(Cat):
    """
    Ещё один подкласс кота — лысый кот Сфинкс.
    """

    def meow(self):
        """Специфическое мяуканье сфинкса."""
        print(f"{self.name}, сфинкс, говорит: Рррмяу!")

    def info(self):
        """Расширяем метод info из родительского класса."""
        super().info()  # вызываем оригинал
        print("Порода: Сфинкс (лысый).")


class Robot:
    """
    Класс, представляющий робота.
    """

    def __init__(self, model: str):
        self.model = model

    def power_on(self):
        print(f"[Робот {self.model}] Включаюсь... Готов к работе!")

    def work(self):
        print(f"[Робот {self.model}] Выполняю задачу...")


class RoboCat(Cat, Robot):
    """
    Гибридный класс: кот-робот. Наследуется от двух классов.
    """

    def __init__(self, name: str, model: str):
        # Вызываем оба конструктора явно, так как MRO может не справиться автоматически
        Cat.__init__(self, name=name, age=0)
        Robot.__init__(self, model=model)

    def meow(self):
        print(f"{self.name} (робокот {self.model}) говорит: Цзириии!")

    def info(self):
        print(f"Я робокот по имени {self.name}, модель: {self.model}")