class Item():
    def __init__(self, name="", item_id=0, item_type=None, effect_range=None, dmg=None, protection=None, effect_duration=None, class_type=None):
        self.name = name
        self.item_id = item_id
        self.item_type = item_type
        self.effect_range = effect_range
        self.dmg = dmg
        self.protection = protection
        self.effect_duration = effect_duration
        self.class_type = class_type


sword_bahvagraba = Item("Espada de Bahvagraba", 0, "weapon", None, 20, None, None, "Warrior")
shield_kurt = Item("Escudo de Kurt", 1, "shield", None, 20, 25, None, "Warrior")
armor_silentplea = Item("Pechera del Lamento", 2, "armor", None, 20, 10, None, "Warrior")
potion_healing_small = Item("Poción de curación (pequeña)", 3, "healing", None, 20, None, "any")
