class Weapon:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def reload(self, amount=None):
        if amount is None:
            self.ammo = 30
        else:
            self.ammo += amount

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1


class Vandal(Weapon):
    def __init__(self, ammo=30):
        super().__init__("Vandal", ammo)

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f"[Vandal] Bang! - Ammo left: {self.ammo}")
        else:
            print("[Vandal] Click! - Out of ammo!")


class Operator(Weapon):
    def __init__(self, ammo=5):
        super().__init__("Operator", ammo)

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f"[Operator] BOOM! - Ammo left: {self.ammo}")
        else:
            print("[Operator] Click! - Out of ammo!")


class JettSkill:
    def __init__(self, knives=5):
        self.knives = knives

    def shoot(self):
        if self.knives > 0:
            self.knives -= 1
            print(f"[JettSkill] Throwing knife! - Knives left: {self.knives}")
        else:
            print("[JettSkill] No knives left!")


def perform_attack(entity, times):
    for _ in range(times):
        entity.shoot()


vandal = Vandal()
operator = Operator()
jett_skill = JettSkill()

entities = [vandal, operator, jett_skill]

for entity in entities:
    perform_attack(entity, 2)

print("---")

vandal.reload(10)
print(f"Vandal reload 10 ammo -> Ammo: {vandal.ammo}")

vandal.reload()
print(f"Vandal full reload -> Ammo: {vandal.ammo}")