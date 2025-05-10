from cat_classes import Cat, BritishShorthair, Sphynx, RoboCat


def main():
    print("=== Создание робокота ===")
    robocat = RoboCat(name="Катэ", model="RC-2077")

    print("\n=== Вызов методов робокота ===")
    robocat.power_on()
    robocat.meow()
    robocat.work()
    robocat.info()

    print("\n=== Порядок разрешения методов (MRO) для RoboCat ===")
    for cls in RoboCat.__mro__:
        print(cls)

    print("\n=== Полиморфизм с разными типами котов ===")
    cats = [
        Cat("Мурзик", 3),
        BritishShorthair("Барон", 2, "голубой"),
        Sphynx("Рокки", 4),
        robocat
    ]

    for cat in cats:
        cat.meow()
        cat.info()
        print()


if __name__ == "__main__":
    main()