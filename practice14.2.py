class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, initial_rating: float = 0, flavors=None, location="", working_hours=""):
        super().__init__(restaurant_name, "кафе-мороженое", initial_rating)
        self.flavors = flavors if flavors is not None else []
        self.location = location
        self.working_hours = working_hours

    def show_flavors(self):
        print("\nДоступные сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Сорт '{flavor}' добавлен в список.")
        else:
            print(f"Сорт '{flavor}' уже есть в списке.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт '{flavor}' удален из списка.")
        else:
            print(f"Сорта '{flavor}' нет в списке.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт '{flavor}' есть в наличии.")
        else:
            print(f"Сорта '{flavor}' нет в наличии.")

    def describe_restaurant(self):
        super().describe_restaurant()
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.working_hours}")

    def add_stick_ice_cream(self, flavor, price):
        print(f"Добавлено мороженое на палочке '{flavor}' по цене {price} руб.")

    def add_soft_ice_cream(self, flavor, price):
        print(f"Добавлено мягкое мороженое '{flavor}' по цене {price} руб.")

    def add_sorbet(self, flavor, price):
        print(f"Добавлено сорбет '{flavor}' по цене {price} руб.")


ice_cream_stand = IceCreamStand(
    "Сладкоежка",
    initial_rating=4.7,
    flavors=["ванильное", "шоколадное", "клубничное", "фисташковое"],
    location="ул. Пушкина, 10",
    working_hours="10:00 - 22:00"
)

ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()

ice_cream_stand.add_flavor("банановое")
ice_cream_stand.add_flavor("ванильное")  # Уже есть
ice_cream_stand.remove_flavor("клубничное")
ice_cream_stand.remove_flavor("мятное")  # Нет в списке
ice_cream_stand.check_flavor("шоколадное")
ice_cream_stand.check_flavor("клубничное")  # Уже удалено

ice_cream_stand.add_stick_ice_cream("ванильное", 50)
ice_cream_stand.add_soft_ice_cream("шоколадное", 70)
ice_cream_stand.add_sorbet("лимонное", 60)