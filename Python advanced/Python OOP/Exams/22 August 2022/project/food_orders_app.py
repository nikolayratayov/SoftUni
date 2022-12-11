from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.client import Client


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number):
        for i in self.clients_list:
            if i.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *args):
        allowed_meals = ['Starter', 'MainDish', 'Dessert']
        for i in args:
            if i.__class__.__name__ not in allowed_meals:
                continue
            self.menu.append(i)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        res = []
        for i in self.menu:
            res.append(i.details())
        return '\n'.join(res)

    def add_meals_to_shopping_cart(self, client_phone_number, **kwargs):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        for i in self.clients_list:
            if i.phone_number == client_phone_number:
                person = i
                break
        else:
            person = Client(client_phone_number)
            self.clients_list.append(person)

        for meal_name, meal_quantity in kwargs.items():
            for i in self.menu:
                if i.name == meal_name:
                    break
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        for meal_name, meal_quantity in kwargs.items():
            for i in self.menu:
                if i.name == meal_name:
                    if meal_quantity > i.quantity:
                        raise Exception(f"Not enough quantity of {i.__class__.__name__}: {meal_name}!")

        ordered_meals_list = []
        for i in person.shopping_cart:
            ordered_meals_list.append(i.name)
        for meal_name, meal_quantity in kwargs.items():
            ordered_meals_list.append(meal_name)
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.__class__.__name__ == 'Starter':
                        new_meal = Starter(meal_name, meal.price, meal_quantity)
                    elif meal.__class__.__name__ == 'MainDish':
                        new_meal = MainDish(meal_name, meal.price, meal_quantity)
                    elif meal.__class__.__name__ == 'Dessert':
                        new_meal = Dessert(meal_name, meal.price, meal_quantity)
                    person.shopping_cart.append(new_meal)
                    person.bill += meal_quantity * meal.price
                    meal.quantity -= meal_quantity
        return f"Client {client_phone_number} successfully ordered {', '.join(ordered_meals_list)} for {person.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                if len(client.shopping_cart) == 0:
                    raise Exception("There are no ordered meals!")
                else:
                    for ordered_meal in client.shopping_cart:
                        for meal_in_menu in self.menu:
                            if meal_in_menu.name == ordered_meal.name:
                                meal_in_menu.quantity += ordered_meal.quantity
                    client.shopping_cart = []
                    client.bill = 0
                    return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                if len(client.shopping_cart) == 0:
                    raise Exception("There are no ordered meals!")
                else:
                    FoodOrdersApp.RECEIPT_ID += 1
                    total_money = client.bill
                    client.shopping_cart = []
                    client.bill = 0
                    return f"Receipt #{FoodOrdersApp.RECEIPT_ID} with total amount of {total_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."



# food_orders_app = FoodOrdersApp()
# print(food_orders_app.register_client("0899999999"))
# french_toast = Starter("French toast", 6.50, 5)
# hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
# tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
# risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
# chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
# chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
# print(food_orders_app.add_meals_to_menu(
#     french_toast, hummus_and_avocado_sandwich,
#     tortilla_with_beef_and_pork,
#     risotto_with_wild_mushrooms,
#     chocolate_cake_with_mascarpone,
#     chocolate_and_violets))
# print(food_orders_app.show_menu())
# food = {"Hummus and Avocado Sandwich": 5,
#         "Risotto with Wild Mushrooms": 1,
#         "Chocolate and Violets": 4}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
# additional_food = {"Risotto with Wild Mushrooms": 2,
#                    "Tortilla with Beef and Pork": 2}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
# for i in food_orders_app.menu:
#     print(f'{i.name} --- {i.quantity}')
# print(food_orders_app.cancel_order('0899999999'))
# for i in food_orders_app.menu:
#     print(f'{i.name} --- {i.quantity}')