import Character


class Mage(Character):
    def __init__(self):
        super().__init__(health=110, armor=10, str=7, agi=10, int=20, faith=12, acc=7,
                         res_magic=18)
