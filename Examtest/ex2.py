from abc import ABC, abstractmethod

class beveragestore(ABC):
    def __init__ (self, drink_name, inventory):
        self.drink_name = drink_name
        self.inventory = inventory

    @abstractmethod
    def calcu_price(self, quantity):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def req_ingredients(self, quantity):
        pass

class coffeestore(beveragestore):
    def __init__ (self, drink_name, inventory, coffee):
        super().__init__(drink_name, inventory)
        self.inventory["coffee"] = coffee

    def calcu_price(self, quantity):
        return 25000 * quantity

    def req_ingredients(self, quantity):
        return {
            "milk": 50 * quantity,
            "sugar": 10 * quantity,
            "honey": 5 * quantity,
            "ice": 100 * quantity,
            "coffee": 20 * quantity
        }

    def show(self):
        print(f"Drink Name: {self.drink_name}")
        print(f"Inventory: {self.inventory}")

class juicestore(beveragestore):
    def __init__ (self, drink_name, inventory, fruits):
        super().__init__(drink_name, inventory)
        self.inventory["fruits"] = fruits

    def calcu_price(self, quantity):
        return 30000 * quantity

    def req_ingredients(self, quantity):
        ingredients = {
            "milk": 50 * quantity,
            "sugar": 10 * quantity,
            "honey": 5 * quantity,
            "ice": 100 * quantity,
            "fruits": {}
        }

        for fruit in self.inventory["fruits"]:
            self.inventory["fruits"][fruit] = 200 * quantity

    def show(self):
        print(f"Drink Name: {self.drink_name}")
        print(f"Inventory: {self.inventory}")

class order:
    def __init__ (self, payment):
        self.order_list = []
        self.payment = payment

    def check_inventory(self, order_list):
        for item in order_list:
            drink = item["drink"]
            quantity = item["quantity"]
            req = drink.req_ingredients(quantity)

            for ingredient in ["milk", "sugar", "honey", "ice"]:
                drink.inventory[ingredient] -= req[ingredient]

            if isinstance(drink, coffeestore):
                drink.inventory["coffee"] -= req["coffee"]

            elif isinstance(drink, juicestore):
                for fruit in req["fruits"]:
                    drink.inventory["fruits"][fruit] -= req["fruits"][fruit]

            self.order_list.append(item)

        print("Add drinks to order list successfully.")
        return True

    def cal_total_price(self, payment):
        total = 0

        for item in self.order_list:
            drink = item["drink"]
            quantity = item["quantity"]
            total += drink.calcu_price(quantity)

        if payment > total:
            print("rest money: ", payment - total)
        elif payment < total:
            print("not enough money", total - payment)
        else:
            print("thank you for your payment")

        print("Total price: ", total)
        return total