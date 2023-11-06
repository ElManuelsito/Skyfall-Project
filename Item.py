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

PotionManaSmall = Item("Poción de Mana (pequeña)",
                            "Posicion de mana que se utiliza para las habilidades.",
                            "potion",
                            20,
                            0,
                            "common")

BowNewborn = Item("Arco del Recién Nacido",
                   "Todos tenemos que empezar en algún lado",
                   "weapon",
                   18,
                   0,
                   "common")

MiraculousHarp = Item("Arpa Milagrosa",
                   "Con musica todo es mejor",
                   "weapon",
                   14,
                   0,
                   "common")

SoulBlinder = Item("Segador de Alma",
                   "Ven que yo cuidare tu alma,no como tu ex",
                   "weapon",
                   20,
                   0,
                   "common")

HolySword = Item("Espada Sagrada",
                   "Con la Guia de Dios al camino de la victoria",
                   "weapon",
                   16,
                   0,
                   "common")

MagickBook = Item("Libro Magico",
                   "Libro de la vida magica",
                   "weapon",
                   23,
                   0,
                   "common")

RapthaliaShield = Item("Raphatalia",
                   "Yo sere tu hogar",
                   "weapon",
                   10,
                   0,
                   "common")

PhoenixDagger = Item("Daga Fénix",
                   "Pequeño pero rapido, el silencio lo es todo",
                   "weapon",
                   18,
                   0,
                   "common")

WolfSword = Item("Espada de lobo",
                   "Fiel y compañera de un Guerrero en la vida",
                   "weapon",
                   20,
                   0,
                   "common")

ElementaryCharity = Item("Caridad Elemental",
                   "Caridad con la energia elemental del mundo",
                   "weapon",
                   22,
                   0,
                   "common")

items_common = [PotionHealingSmall,
                PotionManaSmall,
                BowNewborn,
                MiraculousHarp,
                SoulBlinder,
                HolySword,
                MagickBook,
                RapthaliaShield,
                PhoenixDagger,
                WolfSword,
                ElementaryCharity]

# -------------------- Intermediate items (uncommon) --------------------

ArmorBreastplateSilenthills = Item("Pechera de las Colinas Silenciosa",
                                     "Los gritos de agonia hizo que el silencio sea duro como el hierro",
                                     "armor",
                                     0,
                                     20,
                                     "uncommon")

ArmorGauntletsSilentHill = Item("Guantes de las Colinas Silenciosa",
                                     "Estos guantes se endureciron de tantos lamentos y guardan un secreto en su silencio",
                                     "armor",
                                     0,
                                     20,
                                     "uncommon")

ArmorChaussesSilentHill = Item("Botas de las Colinas Silenciosa",
                                     "El caminar de lamentos ha endurecido su material estando en silencio su sufrimiento ",
                                     "armor",
                                     0,
                                     20,
                                     "uncommon")

DragonBow = Item("Arco Dragon",
                   "Fuerte como la piel del dragon y fuerte como uno",
                   "weapon",
                   25,
                   20,
                   "uncommon")

HeavenlyHarp = Item("Arpa Celestial",
                   "Arpa dado por los mismo angeles",
                   "weapon",
                   18,
                   20,
                   "uncommon")

HellishSoul = Item("Alma Infernal",
                   "Alama poseida por lucifer para el terror en la tierra",
                   "weapon",
                   30,
                   0,
                   "uncommon")

SwordofGod = Item("Espada de Dios",
                   "Con la fuerza de Dios dispuesta en una espada ",
                   "weapon",
                   20,
                   0,
                   "uncommon")

DarkBook = Item("Libro oscuro",
                   "Libro con las magias prohibidas,con miedo a ser revelados",
                   "weapon",
                   23,
                   0,
                   "uncommon")

FlameShield = Item("Escudo de LLamas",
                   "Escudo con fuego dispuesto a proteger a los que aman",
                   "weapon",
                   15,
                   0,
                   "uncommon")

SnakeDagger = Item("Daga serpiente",
                   "Daga muy filosa pero y silenciosa",
                   "weapon",
                   25,
                   0,
                   "uncommon")

HoundSword = Item("Espada Sabueso",
                   "Espada lista para la guerra sin miedo a morir",
                   "weapon",
                   28,
                   0,
                   "uncommon")

AvatarCharity = Item("Caridad Avatar",
                   "Caridad con los elementos conectado con la naturaleza rebozando de su energia al cien",
                   "weapon",
                   32,
                   0,
                   "uncommon")

items_uncommon = [ArmorBreastplateSilenthills,
                  ArmorChaussesSilentHill,
                  ArmorGauntletsSilentHill,
                  DragonBow,
                  HeavenlyHarp,
                  HellishSoul,
                  SwordofGod,
                  DarkBook,
                  FlameShield,
                  SnakeDagger,
                  HoundSword,
                  AvatarCharity]

# -------------------- Legendary items (rare) --------------------

ValshBow = Item("Arco Valsh",
                   "Arco profundamente ligero pero fuerte y preciso,confiable en los momentos decisivo",
                   "weapon",
                   30,
                   25,
                   "legendary")

ArchangelHarp = Item("Arpa Arcangel",
                   "Arpa del Angel Arcangel",
                   "weapon",
                   24,
                   25,
                   "legendary")

SoulLucifer = Item("Alma de Lucifer",
                   "Alama de lucifer,rey del inframundo",
                   "weapon",
                   40,
                   25,
                   "legendary")

SwordBahvagraba = Item("Espada de Bahvagraba",
                        "Una espada que alguna vez le perteneció a una criatura celestial.",
                        "weapon",
                        28,
                        25,
                        "legendary")

StephenStrangeBook = Item("Libro de Stephen Strange",
                   "Libro con las magias temporales capaces de cambiar la historia el cual se conoce",
                   "weapon",
                   29,
                   0,
                   "legendary")

DensetsunoTate = Item("Escudo legendario ",
                   "Arma legendaria que se encuentra en este mundo, que solo sera encontrada por un corazon puro",
                   "weapon",
                   24,
                   25,
                   "legendary")

TwilightDagger = Item("Daga Crespuscular ",
                   "Daga de gran calidad que se enceuntra en el intervalo de la salida de la puesta del sol",
                   "weapon",
                   35,
                   25,
                   "legendary")

ThunderSword = Item("Espada Trueno",
                   "Espada ligera y destructivo como el rayo, resplandece como uno entre los cielos grises",
                   "weapon",
                   38,
                   25,
                   "legendary")

NaturalConnection = Item("Conexion Naturall",
                   "Caridad que provoca que el usuario y la naturaleza se conecten siendo uno",
                   "weapon",
                   42,
                   25,
                   "legendary")

items_legendary = [ValshBow,
                   ArchangelHarp,
                   SoulLucifer,
                   SwordBahvagraba,
                   StephenStrangeBook,
                   DensetsunoTate,
                   TwilightDagger,
                   ThunderSword,
                   NaturalConnection]