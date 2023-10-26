import Character


class Warrior(Character):
    def __init__(self):
        super().__init__(health=275, armor=40, str=20, agi=10, int=8, faith=6, acc=6,
                         res_magic=5, res_phys=10)

    def skill_a(self):
        pass

    def skill_b(self):
        pass
