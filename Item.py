class Item:
    def __init__(self,
                 name,
                 description,
                 item_type,
                 dmg,
                 protection,
                 rarity):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.dmg = dmg
        self.protection = protection
        self.rarity = rarity


# -------------------- Starter items (common) --------------------

PotionHealingSmall = Item("Poción de curación (pequeña)",
                            "Evidentemente, no podrás curarte de todos tus males con una sola.",
                            "potion",
                            20,
                            0,
                            "common")
BowNewborn = Item("Arco del Recién Nacido",
                   "Todos tenemos que empezar en algún lado",
                   "bow",
                   18,
                   0,
                   "common")

MiraculousHarp = Item("Arpa Milagrosa",
                   "Con musica todo es mejor",
                   "Harp",
                   14,
                   0,
                   "common")

SoulBlinder = Item("Segador de Alma",
                   "Ven que yo cuidare tu alma,no como tu ex",
                   "Soul",
                   20,
                   0,
                   "common")

HolySword = Item("Espada Sagrada",
                   "Con la Guia de Dios al camino de la victoria",
                   "Sword",
                   16,
                   0,
                   "common")

MagickBook = Item("Libro Magico",
                   "Libro de la vida magica",
                   "Book",
                   23,
                   0,
                   "common")

RapthaliaShield = Item("Raphatalia",
                   "Yo sere tu hogar",
                   "Shield",
                   10,
                   0,
                   "common")

PhoenixDagger = Item("Daga Fénix",
                   "Pequeño pero rapido, el silencio lo es todo",
                   "Dagger",
                   18,
                   0,
                   "common")

WolfSword = Item("Espada de lobo",
                   "Fiel y compañera de un Guerrero en la vida",
                   "Sword",
                   20,
                   0,
                   "common")

ElementaryCharity = Item("Caridad Elemental",
                   "Caridad con la energia elemental del mundo",
                   "Caridad",
                   22,
                   0,
                   "common")


# -------------------- Intermediate items (uncommon) --------------------

ArmorBreastplateSilenthills = Item("Pechera de las Colinas Silenciosa",
                                     "Los gritos de agonia hizo que el silencio sea duro como el hierro",
                                     "breastplate",
                                     0,
                                     20,
                                     "uncommon")

ArmorGauntletsSilentHill = Item("Guantes de las Colinas Silenciosa",
                                     "Estos guantes se endureciron de tantos lamentos y guardan un secreto en su silencio",
                                     "Gauntles",
                                     0,
                                     20,
                                     "uncommon")

ArmorChaussesSilentHill = Item("Botas de las Colinas Silenciosa",
                                     "El caminar de lamentos ha endurecido su material estando en silencio su sufrimiento ",
                                     "Botas",
                                     0,
                                     20,
                                     "uncommon")

DragonBow = Item("Arco Dragon",
                   "Fuerte como la piel del dragon y fuerte como uno",
                   "bow",
                   25,
                   20,
                   "uncommon")

HeavenlyHarp = Item("Arpa Celestial",
                   "Arpa dado por los mismo angeles",
                   "Harp",
                   18,
                   20,
                   "uncommon")

HellishSoul = Item("Alma Infernal",
                   "Alama poseida por lucifer para el terror en la tierra",
                   "Soul",
                   30,
                   0,
                   "uncommon")

SwordofGod = Item("Espada de Dios",
                   "Con la fuerza de Dios dispuesta en una espada ",
                   "Sword",
                   20,
                   0,
                   "uncommon")

DarkBook = Item("Libro oscuro",
                   "Libro con las magias prohibidas,con miedo a ser revelados",
                   "Book",
                   23,
                   0,
                   "common")

FlameShield = Item("Escudo de LLamas",
                   "Escudo con fuego dispuesto a proteger a los que aman",
                   "Shield",
                   15,
                   0,
                   "uncommon")

SnakeDagger = Item("Daga serpiente",
                   "Daga muy filosa pero y silenciosa",
                   "Dagger",
                   25,
                   0,
                   "uncommon")

HoundSword = Item("Espada Sabueso",
                   "Espada lista para la guerra sin miedo a morir",
                   "Sword",
                   28,
                   0,
                   "uncommon")

AvatarCharity = Item("Caridad Avatar",
                   "Caridad con los elementos conectado con la naturaleza rebozando de su energia al cien",
                   "Caridad",
                   32,
                   0,
                   "uncommon")

# -------------------- Legendary items (rare) --------------------

ValshBow = Item("Arco Valsh",
                   "Arco profundamente ligero pero fuerte y preciso,confiable en los momentos decisivo",
                   "bow",
                   30,
                   25,
                   "Legendary")

ArchangelHarp = Item("Arpa Arcangel",
                   "Arpa del Angel Arcangel",
                   "Harp",
                   24,
                   25,
                   "Legendary")

SoulLucifer = Item("Alma de Lucifer",
                   "Alama de lucifer,rey del inframundo",
                   "Soul",
                   40,
                   25,
                   "Legendary")

SwordBahvagraba = Item("Espada de Bahvagraba",
                        "Una espada que alguna vez le perteneció a una criatura celestial.",
                        "Sword",
                        28,
                        25,
                        "Legendary")

StephenStrangeBook = Item("Libro de Stephen Strange",
                   "Libro con las magias temporales capaces de cambiar la historia el cual se conoce",
                   "Book",
                   29,
                   0,
                   "Legendary")

DensetsunoTate = Item("Escudo legendario ",
                   "Arma legendaria que se encuentra en este mundo, que solo sera encontrada por un corazon puro",
                   "Shield",
                   24,
                   25,
                   "Legendary")

TwilightDagger = Item("Daga Crespuscular ",
                   "Daga de gran calidad que se enceuntra en el intervalo de la salida de la puesta del sol",
                   "Dagger",
                   35,
                   25,
                   "Legendary")

ThunderSword = Item("Espada Trueno",
                   "Espada ligera y destructivo como el rayo, resplandece como uno entre los cielos grises",
                   "Sword",
                   38,
                   25,
                   "Legendary")

NaturalConnection = Item("Conexion Naturall",
                   "Caridad que provoca que el usuario y la naturaleza se conecten siendo uno",
                   "Caridad",
                   42,
                   25,
                   "Legendary")
