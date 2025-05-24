class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг обновлен: {self.rating}")


class IceCreamStand(Restaurant):#наследует все атрибуты
    def __init__(self, restaurant_name, initial_rating: float = 0, flavors=None):
        super().__init__(restaurant_name, "кафе-мороженое", initial_rating) #конструктор родительского класса
        self.flavors = flavors if flavors is not None else []

    def show_flavors(self):
        print("\nДоступные сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand(
    "Сладкоежка",
    initial_rating = 4.7,
    flavors = ["ванильное", "шоколадное", "клубничное", "фисташковое"]
)

ice_cream_stand.describe_restaurant()

ice_cream_stand.show_flavors()