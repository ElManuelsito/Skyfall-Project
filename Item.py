class Item:
    def __init__(self,
                 name,
                 description,
                 item_type,
                 dmg,
                 protection,
                 effect_range,
                 effect_duration,
                 class_bonus,
                 rarity):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.dmg = dmg
        self.protection = protection
        self.effect_range = effect_range
        self.effect_duration = effect_duration
        self.class_bonus = class_bonus
        self.rarity = rarity


# -------------------- Starter items (common) --------------------

potion_healing_small = Item("Poción de curación (pequeña)",
                            "Evidentemente, no podrás curarte de todos tus males con una sola.",
                            "potion",
                            20,
                            0,
                            None,
                            None,
                            "Cualquiera",
                            "common")
bow_newborn = Item("Arco del Recién Nacido",
                   "Todos tenemos que empezar en algún lado",
                   "bow",
                   18,
                   0,
                   None,
                   None,
                   "Arquero y Ladrón",
                   "common")

# -------------------- Intermediate items (uncommon) --------------------

armor_breastplate_silenthills = Item("Pechera de las Colinas Silenciosa",
                                     "Es mejor no usarla fuera de combate, los gritos que emite se hacen cada vez más "
                                     "fuerte...",
                                     "breastplate",
                                     0,
                                     20,
                                     None,
                                     None,
                                     "Cualquiera",
                                     "uncommon")

# -------------------- Legendary items (rare) --------------------

sword_bahvagraba = Item("Espada de Bahvagraba",
                        "Una espada que alguna vez le perteneció a una criatura celestial."
                        " Se dice que el dueño aún deambula por estas tierras, comiendo duraznos.",
                        "weapon",
                        20,
                        None,
                        None,
                        None,
                        "Guerrero",
                        "rare")
shield_kurt = Item("Escudo de Kurt",
                   "Forjado durante un concierto, es capaz de protegerte de casi todo, CASI todo.",
                   "shield",
                   9,
                   30,
                   None,
                   None,
                   "Guerrero, Paladin y Tanque",
                   "rare")
