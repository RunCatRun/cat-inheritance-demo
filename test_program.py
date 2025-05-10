from cat_classes import Cat, BritishShorthair, Sphynx, RoboCat


def demonstrate_robo_cat_features(cat):
    """Демонстрирует уникальные функции робокота."""
    print("\n[RoboCat: дополнительные возможности]")
    cat.power_on()
    cat.work()


def main():
    # === Создание объектов ===
    robocat = RoboCat(name="Катэ", model="RC-2077")
    simple_cat = Cat("Мурзик", 3)
    british_cat = BritishShorthair("Барон", 2, "голубой")
    sphynx_cat = Sphynx("Рокки", 4)

    # === Демонстрация работы робокота ===
    print("=== Демонстрация возможностей робокота ===")
    demonstrate_robo_cat_features(robocat)
    robocat.meow()
    robocat.info()

    # === Полиморфизм: разные коты ===
    print("\n=== Полиморфизм: разные типы котов ===")
    cats = [simple_cat, british_cat, sphynx_cat, robocat]

    for cat in cats:
        cat.meow()
        cat.info()
        if isinstance(cat, BritishShorthair):
            cat.groom()
        print("-" * 30)

    # === Порядок разрешения методов (MRO) ===
    print("\n=== Порядок разрешения методов (MRO) для RoboCat ===")
    for idx, cls in enumerate(RoboCat.__mro__, start=1):
        print(f"{idx}. {cls}")


if __name__ == "__main__":
    main()