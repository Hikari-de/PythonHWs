import numpy as np
from abc import ABC, abstractmethod


class Appliance(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def generate_data(self):
        pass

    @abstractmethod
    def print_report(self):
        pass


class Refrigerator(Appliance):
    def __init__(self, name):
        super().__init__(name)
        self.data = None

    def generate_data(self):
        self.data = np.random.uniform(1.0, 2.5, 30)

    def print_report(self):
        total = self.data.sum()
        max_index = np.argmax(self.data)
        max_value = self.data[max_index]

        print(f"=== REPORT: {self.name} ===")
        print(f"- Total electricity for 30 days: {total:.2f} kWh")
        print(
            f"- Highest consumption: Day {max_index + 1} "
            f"({max_value:.2f} kWh)"
        )


class AirConditioner(Appliance):
    def __init__(self, name):
        super().__init__(name)
        self.data = None

    def generate_data(self):
        self.data = np.random.uniform(4.0, 12.0, (4, 7))

    def print_report(self):
        weekly_consumption = self.data.sum(axis=1)

        daily_data = self.data.reshape(-1)
        top_3 = np.sort(daily_data)[-3:][::-1]

        first_level = np.minimum(daily_data, 8) * 2500
        second_level = np.maximum(daily_data - 8, 0) * 4000
        total_cost = np.sum(first_level + second_level)

        print(f"=== REPORT: {self.name} ===")
        print("- Weekly electricity consumption:", np.round(weekly_consumption, 2))
        print("- Top 3 highest consumption days:", np.round(top_3, 2), "kWh")
        print(f"- TOTAL ELECTRICITY COST: {total_cost:,.0f} VND")


appliances = [
    Refrigerator("Refrigerator"),
    AirConditioner("Air Conditioner")
]

for appliance in appliances:
    appliance.generate_data()
    appliance.print_report()
    print()