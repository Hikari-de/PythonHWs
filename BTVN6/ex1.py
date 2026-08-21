from abc import ABC, abstractmethod


class HomeAppliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def operate(self):
        pass


class KitchenAppliance(HomeAppliance):
    def turn_on(self):
        print("Plugged in and turned on.")


class RiceCooker(KitchenAppliance):
    def operate(self):
        print("Operating: Cooking rice...")


class Microwave(KitchenAppliance):
    def operate(self):
        print("Operating: Heating food...")


try:
    kitchen_appliance = KitchenAppliance()
except TypeError:
    print("Error: Cannot instantiate KitchenAppliance because the abstract method 'operate' is not implemented.")
    
print("---")

appliances = [
    RiceCooker(),
    Microwave()
]

for appliance in appliances:
    print(f"[{appliance.__class__.__name__}]", end=" ")
    appliance.turn_on()
    
    print(f"[{appliance.__class__.__name__}]", end=" ")
    appliance.operate()