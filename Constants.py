# print(INTRO_GAME)
# se deben guardar las constantes en un archivo "constant"
# INTRO_GAME = "INTRODUCCIÓN AL JUEGO"
# MENU = "1- Entrar al juego" \
#        "2- Etc."
# MAX_PLAYERS = 5

# -- Testeando pickle --
# import pickle
#
# player_info = {"weapon_1": False,
#                "weapon_2": False,
#                "helmet": False,
#                "breastplate": False,
#                "chausses": False,
#                "gauntlets": False,
#                "money": 0,
#                "location": None}
# with open("savefile.pickle", "wb") as f:
#     pickle.dump(player_info, f, protocol=0)
# f.close()
#
# with open("savefile.pickle", "rb") as f:
#     player_info = pickle.load(f)
# f.close()
# print(player_inv.items())

# -----


# -------------------- Menu Related --------------------
# [ PLAYER INTERACTION WITH SYSTEM]

PLAYER_PROMPT_OPTION = "Opción: "
PLAYER_PROMPT_NAME = "Nombre: "
PRESS_ENTER_TO_CONTINUE = "\nPresiona Enter para continuar...\n"
PRESS_ENTER_TO_RETURN = "\nPresiona Enter para volver...\n"

# [ OPTIONS, MESSAGES AND WARNINGS ]
WELCOMING_MESSAGE = "\n\n                    ~ Skyfall ~\nSelecciona una opción ingresando su número por teclado.\n"
MAIN_MENU_OPTIONS = "1. Nuevo juego\n2. Continuar\n3. Instrucciones\n4. Salir\n"
WARNING_MESSAGE_INVALID_MAIN_MENU_OPTION = "No existe esa opción! Por favor selecciona una de las opciones dadas."
MAIN_MENU_MESSAGE_SAVEFILE_ALREADY_EXISTS = "Advertencia! Ya existe un archivo de guardado!\nSi eliges continuar ahora se eliminará tu progreso y tendrás que comenzar desde cero.\n"
MAIN_MENU_MESSAGE_SAVEFILE_DELETE_CONFIRMATION = "¿Deseas continuar? (si/no)"
MAIN_MENU_MESSAGE_SAVEFILE_DELETED = "\nEl archivo a sido eliminado\n"
MAIN_MENU_MESSAGE_SAVEFILE_NOT_DELETED_GOING_BACK_TO_MENU = "\nVolviendo al menu principal..."
MAIN_MENU_MESSAGE_GAME_LOADING = "Cargando mundo..."
PLAYER_PROMPT_SET_FOR_YES = {"s", "S", "si", "sí", "SI", "SÍ", "Si", "Sí", "sI", "sÍ", "y", "Y", "yes", "Yes", "YES"}   # estructura de datos Set, incluye posibilidades para la respuesta del usuario "si"
PLAYER_PROMPT_SET_FOR_NO = {"no", "No", "NO", "nO", "n", "N"}                                                           # misma estructura, pero para "No"
TIME_BETWEEN_MESSAGES = 0.85
TIME_BETWEEN_WARNINGS = 3.5

INSTRUCTIONS_MENU = "\nBienvenido a Skyfall! Para comenzar por favor lea estas instrucciones:\n1. Navegar el menú\n2. Navegar el mundo\n 3. Combate\n 4. Items\n"
TIPS = ["Tip: para abrir el menu de opciones durante el combate, ingresar \"pausa\"."]

CHARACTER_CREATION_NAME_MESSAGE = "\nComienza creando tu personaje!\n\nPrimero ingresa tu nombre (recuerda que solo puedes utilizar caracteres alfabéticos y sin espacios)"
WARNING_MESSAGE_INVALID_NAME = "Nombre no valido! Solo utiliza caracteres alfabéticos sin espacios!"

CHARACTER_CREATION_CLASS_MESSAGE = "\nAhora selecciona una clase (solo utiliza números del 1-9)"
WARNING_MESSAGE_INVALID_CLASS = "Clase no valida! Solo utiliza un número del 1-9!"

CHARACTER_CREATION_CLASS_CONFIRM = "¿Deseas usar esta clase? (si/no)"
WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION = "Por favor ingresa solamente \"si\" o \"no\"."

CHARACTER_CREATION_ALL_CLASSES = "\n1. Arquero\n2. Mago\n3. Guerrero\n4. Ladrón\n5. Hechicero\n6. Paladín\n7. Nigromante\n8. Tanque\n9. Bardo\n"

CHARACTER_CREATION_DESCRIPTION_ARCHER = "\n\n|| Arquero ||\nSalud: 120\nDefensa: 20\nMana: 20\nFuerza: 10\nAgilidad: 18" \
                                        "\nInteligencia: 7\nFé: 8\nPrecisión: 19\nResistencia mágica: 7%\nResistencia física: 5%" \
                                        "\n\nDescripción:\n Maestro del arco y armas de distancia, el arquero se especializa en ataques a distancias, donde" \
                                        " su agilidad es muy importante para moverse junto a su gran precisión.\n No tiene mucha salud ni resistencia, pero" \
                                        " sus capacidades de esquivar e huir le son más que suficientes para sus batallas y descubrimientos a lo largo del mundo.\n"

CHARACTER_CREATION_DESCRIPTION_WIZARD = "\n\n|| Mago ||\nSalud: 100\nDefensa: 15\nMana: 75\nFuerza: 10\nAgilidad: 6" \
                                        "\nInteligencia: 30\nFé: 6\nPrecisión: 15\nResistencia mágica: 10%\nResistencia física: 3%" \
                                        "\n\nDescripción:\n Los magos son famosos por controlar el campo de batalla debido a sus manejos de los elementos, son personas que estudian la magia y los elementos para su beneficio.\n" \
                                        " Son muy lentos y de bajo daño físico, pero sus grandes poderes mágicos les son más que suficientes para ganar un combate.\n"

CHARACTER_CREATION_DESCRIPTION_WARRIOR = "\n\n|| Guerrero ||\nSalud: 275\nDefensa: 40\nMana: 25\nFuerza: 20\nAgilidad: 10" \
                                        "\nInteligencia: 8\nFé: 6\nPrecisión: 6\nResistencia mágica: 2%\nResistencia física: 10%" \
                                        "\n\nDescripción:\n Guerreros dispuestos a la batalla sin miedo a la muerte, con sus espadas listas y sus armaduras preparadas para la batalla.\n" \
                                         " Su fuerza física es remarcable, dicen que llega incluso a atravesar armaduras como si fueran meros papeles.\n" \
                                         " Cuentan con un físico intermedio en aspectos como la agilidad, fuerza y defensa, pero son muy débiles contra la magia ya que son fáciles de poseer y de entrar en su mente.\n"

CHARACTER_CREATION_DESCRIPTION_THIEF = "\n\n|| Ladrón ||\nSalud: 150\nDefensa: 20\nMana: 30\nFuerza: 18\nAgilidad: 24" \
                                        "\nInteligencia: 0\nFé: 5\nPrecisión: 10\nResistencia mágica: 8%\nResistencia física: 10%" \
                                        "\n\nDescripción:\n Ladrones de naturaleza, con agilidad como un felino y precisión como un Halcón a la ahora de atacar, son muy cautelosos y difíciles de rastrear.\n" \
                                       " En batalla, su audacia junto a su experiencia de salir de problemas apretados lo ayudan a ganar la contienda.\n" \
                                       " Si bien su salud es intermedia, su agilidad y fuerza le son más que suficientes para salir adelante.\n"

CHARACTER_CREATION_DESCRIPTION_SORCERER = "\n\n|| Hechicero ||\nSalud: 100\nDefensa: 10\nMana: 60\nFuerza: 8\nAgilidad: 5" \
                                        "\nInteligencia: 45\nFé: 3\nPrecisión: 20\nResistencia mágica: 5%\nResistencia física: 4%" \
                                        "\n\nDescripción:\n Los hechiceros son especialistas en la magia de control e invocaciones de criaturas vivas, su magia es muy poderosa pero su cuerpo y debilidad física no lo acompañan.\n" \
                                          " Compensan sus debilidades físicas invocando criaturas que pelean por ellos, permitiéndoles ganar sus batallas.\n" \
                                          " Son muy astutos pero su movilidad es muy lenta, no creen en la fe divina pero sí en su divina magia.\n"

CHARACTER_CREATION_DESCRIPTION_PALADIN = "\n\n|| Paladin ||\nSalud: 200\nDefensa: 40\nMana: 25\nFuerza: 10\nAgilidad: 4" \
                                        "\nInteligencia: 20\nFé: 1\nPrecisión: 8\nResistencia mágica: 10%\nResistencia física: 12%" \
                                        "\n\nDescripción:\n Los paladines son una clase hibrida entre Caballero y Sacerdote que pueden ser denominados como caballeros sagrados.\n" \
                                         " Se recubren con sus armaduras, junto a sus escudos y espadas, pero por el peso que llevan son muy lentos a la hora de la batalla.\n" \
                                         " Su fe divina siempre lo protege junto a la dureza de su armadura y su noble corazón.\n"

CHARACTER_CREATION_DESCRIPTION_NECROMANCER = "\n\n|| Nigromante ||\nSalud: 100\nDefensa: 9\nMana: 55\nFuerza: 7\nAgilidad: 5" \
                                        "\nInteligencia: 40\nFé: 0\nPrecisión: 20\nResistencia mágica: 9%\nResistencia física: 4%" \
                                        "\n\nDescripción:\n Maestro de las magias de la muerte, capaces de invocar seres no-muertos y magias infernales. Sus armas pueden ser dagas o varitas para realizar invocaciones.\n" \
                                             " Siempre en búsqueda de lo desconocido y lo prohibido de la magia, son personas muy cautelosas, donde su salud es baja pero su magia es poderosa.\n"

CHARACTER_CREATION_DESCRIPTION_TANK = "\n\n|| Tanque ||\nSalud: 300\nDefensa: 60\nMana: 15\nFuerza: 15\nAgilidad: 6" \
                                        "\nInteligencia: 4\nFé: 9\nPrecisión: 4\nResistencia mágica: 11%\nResistencia física: 15%" \
                                        "\n\nDescripción:\n Guerreros con armaduras pesadas junto a un escudo y un fiel mazo o espada que los acompañan para la guerra, nunca titubean a la hora de defender e ir en primera fila para proteger a su gente.\n " \
                                      "Poseen un corazón noble y siempre dispuesto ayudar a su Reino, debido a sus pesadas armaduras son muy lentos pero tienen una resistencia inigualable.\n"

CHARACTER_CREATION_DESCRIPTION_BARD = "\n\n|| Bardo ||\nSalud: 80\nDefensa: 10\nMana: 40\nFuerza: 5\nAgilidad: 6" \
                                        "\nInteligencia: 30\nFé: 15\nPrecisión: 13\nResistencia mágica: 6%\nResistencia física: 4%" \
                                        "\n\nDescripción:\n Bardo es un elegante luchador que utiliza el poder de la canción para mejorar a sus aliados y derrotar a sus enemigos.\n" \
                                      " Abriéndose paso entre sus enemigos con una variedad de ataques llamativos, el Bardo inspira a sus aliados a nunca bajar los brazos, dándoles ánimo y mejoras para seguir luchando.\n"

CHARACTER_CREATION_WORLD_MESSAGE = "\nPara finalizar, elige tu punto de aparición"
CHARACTER_CREATION_WORLD_SPAWNPOINTS = "\n1. Muldraugh\n2. Riverside\n"
WARNING_MESSAGE_INVALID_SPAWNPOINT_CHOICE = "No existe ese lugar! Por favor elige donde quieres aparecer"
CHARACTER_CREATION_WORLD_SPAWNPOINT_CONFIRMATION = "¿Deseas aparecer aquí? (si/no)"


# -------------------- Exploration Related --------------------
INTRO_MESSAGE_RIVERSIDE = "Comienza un nuevo día, te levantas de tu pequeña y miserable caja, la misma caja que ha " \
                          "actuado como tu hogar por ya no sabes cuánto tiempo.\nOtra día en donde la comida es escasa" \
                          " y lo único que hay en tu bolso es polvo y un vacío que representa tu voluntad de seguir en" \
                          " este estado deplorable.\n\nDecides ponerle un fin a este estilo de vida, haciendo el " \
                          "último llamado: salir adelante o morir. Recoges tus únicas pertenencias, y emprendes viaje." \
                          "\n\n"
INTRO_MESSAGE_MULDRAUGH = "Un punzante dolor te despierta de tu sueño repentino, todo tu alrededor parece dar vueltas" \
                          " y no logras alcanzar a comprender tu situación.\nTratas de recomponerte, y luego de un rato" \
                          " comienzas a recordar, esos bandidos se llevaron todo!\n\nSabías que venir a este reino no" \
                          " era buena idea, pero la invitación al Cuarto Real era muy tentadora para no aceptarla." \
                          " Recoges lo primero que encuentras entre la basura, y emprendes viaje para vengarte de " \
                          "aquellos que te hicieron daño.\n\n"
WORLD_PLAYER_IS_IN_POI = "Ahora mismo te encuentras en:"


# -------------------- Combat Related --------------------
# [ GENERAL OPTIONS & MESSAGES ]
COMBAT_OPTIONS = "Decide qué hacer:\n1. Ataque Común    2. Habilidades\n" \
                 "3. item                4. Huir\n"
SPECIAL_ATTACK_CONFIRM = "¿Deseas usar esta habilidad? (si/no)"
SOMEONE_ATTACKS = "ataca!"
SOMEONE_ATTACKS_AND_MISSES = "intentó atacar, pero falló!"
SOMEONE_RECEIVES_DAMAGE = "recibe daño:"
SOMEONE_FLED = "no pudo soportalo y salió corriendo!"
SOMEONE_FLED_AND_FAILED = "...pero no logró escapar."
SOMEONE_FLED_AND_SUCCEEDED = "...y escapó."
SOMEONE_is_DEFEATED = "no puede continuar, y es derrotado!"


# [ ARCHER ]
SPECIAL_ATTACKS_ARCHER = "\nHabilidades:\n1. Lluvia de flechas\n2. Flecha de fuego\n3. Ojo de Águila\n"
SPECIAL_ATTACK_A_DESC_ARCH = "Lluvia de flechas:\n+ Daña multiples enemigos a la vez\n- Utiliza más Mana de lo normal\n"
SPECIAL_ATTACK_B_DESC_ARCH = "Flecha de fuego:\n+ Enemigo recibe daño por turno dependiendo de tu INT\n+ Más daño de lo normal\n -20% Chance de no aplicar el efecto\n"
SPECIAL_ATTACK_B_CHANCE_ARCH = 80
SPECIAL_ATTACK_C_DESC_ARCH = "Ojo de Águila:\n+ Aumenta tu precisión por un turno\n"

# [Wizard]
SPECIAL_ATTACKS_WIZARD = "\nHabilidades:\n1. Bola de Fuego\n2. LLuvida de fuego\n3. Congelamiento \n"
SPECIAL_ATTACK_A_DESC_WIZ = "Bola de Fuego:\n+ Mete mucho daño a un solo objetivo\n- Coste Intermedio de Mana\n"
SPECIAL_ATTACK_B_DESC_WIZ = "Lluvia de Fuego:\n+ En una Zona circular cae una lluvia de fuego, donde mete daño en Area y afectando a mas de un enemigo\n+ Coste Alto de Mana\n"
SPECIAL_ATTACK_C_DESC_WIZ = "Congelamiento:\n+ En una zona crea un escarcha de hielo provocando que los enemigos queden congelado y aturdido\n+ Coste Intermedio de Mana"
SPECIAL_ATTACK_C_CHANCE_WIZ = 70

# [Warrior]
SPECIAL_ATTACKS_WARRIOR = "\nHabilidades:\n1. Corte \n2. Spiral Splash \n3. Multiples cortes  \n"
SPECIAL_ATTACK_A_DESC_WARR = "Corte:\n+ Provoca un daño intermedio a un objetivo \n- Coste bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_WARR = "Spiral Splash:\n+ Genera un espiral de fuego en la espada provocando daño a un objetivo\n+ Coste intermedio de Mana\n"
IAL_ATTACK_B_CHANCE_WARR = 50
SPECIAL_ATTACK_C_DESC_WARR = "Multix Cortes:\n+ Provoca multiples cortes a un objetivo, provocando mucho daño\n+ Coste Alto de mana"

# [THIEF]
SPECIAL_ATTACKS_THIEF = "\nHabilidades:\n1.Golpe bajo \n2. Corte desgarrador \n3. Golpe en los Riñones\n"
SPECIAL_ATTACK_A_DESC_THIE = "Golpe Bajo:\n+ Provoca un daño intermedio a un objetivo golpeando en los puntos bajo \n- Coste bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_THIE = "Corte desgarrador:\n+  Provoca un corte con sangrado \n+ Coste intermedio de Mana\n"
SPECIAL_ATTACK_B_CHANCE_THIE = 70
SPECIAL_ATTACK_C_DESC_THIE = "Golpe en los Riñones:\n+ Provoca mucho daño al objetivo logrando paralizarlo \n+ Coste Alto de mana"
SPECIAL_ATTACK_C_CHANCE_THIE = 40

# [SORCERER]
SPECIAL_ATTACKS_SORC = "\nHabilidades:\n1.Magia Control \n2. Invocacion bestia \n3. Fear\n"
SPECIAL_ATTACK_A_DESC_SORC = "Magia Control :\n+ Controla por un breve momento al enemigo haciendo que se lastime el mismo \n- Coste intermedio de Mana\n"
SPECIAL_ATTACK_B_DESC_SORC = "Invocacion Bestia:\n+ Invoca a una criatura que le ayuda a luchar provocando daño a un objetivo \n+ Coste Alto de Mana\n"
SPECIAL_ATTACK_C_DESC_SORC = "Fear:\n+ Provoca un miedo al enemigo que hace que no ataque por un breve momento \n+ Coste intermedio  de mana"
SPECIAL_ATTACK_C_CHANCE_SORC = 45

# [Paladin]
SPECIAL_ATTACKS_PAL = "\nHabilidades:\n1.Sentencia \n2. Destello de luz  \n3. Golpe de Cruzado \n"
SPECIAL_ATTACK_A_DESC_PAL = "Sentencia:\n+ Juzga al enemigo provocandole un daño con la espada sagrada \n- Coste Bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_PAL = "Destello de Luz:\n+ Invoca una luz que cae en el provocando curarce un 20% de su vida faltante \n+ Coste Alto de Mana\n"
SPECIAL_ATTACK_C_DESC_PAL = "Golpe de Cruzada:\n+ Golpea al objetivo provocando un gran daño y aturdiendolo brevemente\n+ Coste intermedio  de mana"
SPECIAL_ATTACK_C_CHANCE_PAL = 50

# [NECROMANCER]
SPECIAL_ATTACKS_NEC = "\nHabilidades:\n1.Invoacion NO-MUERTO \n2. Invoaciones Infernales \n3. Descomposición \n"
SPECIAL_ATTACK_A_DESC_NEC = "Invoacion NO-MUERTO:\n+ Invoca personas sin vida para atacar a un objetivo \n- Coste Bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_NEC = "Invoacion Infernal:\n+ Invoca Bestias del Infierno para dañar todo lo que se ponga por delante \n+ Coste Alto de Mana\n"
SPECIAL_ATTACK_C_DESC_NEC = "Descomposición:\n+ Lanza una maldicion que hace que el objetivo se descomponga como si estuviera envenenado\n+ Coste intermedio de mana"
SPECIAL_ATTACK_C_CHANCE_NEC = 50

# [TANK]
SPECIAL_ATTACKS_TANK = "\nHabilidades:\n1.Power up \n2. Focus \n3. Desesperacion \n"
SPECIAL_ATTACK_A_DESC_TANK = "Power UP:\n+ Hace que su ataque aumente \n- Coste Bajo de Mana\n"
SPECIAL_ATTACK_B_DESC_TANK = "Focus:\n+ Se concentra aumentando su defensa a todo tipo de daño \n+ Coste bajo de Mana\n"
SPECIAL_ATTACK_C_DESC_TANK = "Desesperacion:\n+ Cuando ya se esta por rendir entra en su desesperacion aumentando drasticamente su defensa y daño \n+ Coste intermedio de mana"

# [BARD]
SPECIAL_ATTACKS_BARD = "\nHabilidades:\n1.Ispiracion \n2. Curar \n3. Remover Efectos\n"
SPECIAL_ATTACK_A_BARD = "Ispiracion:\n+ Sube los stat de si mismo inspirandose \n- Coste Bajo de mana \n"
SPECIAL_ATTACK_B_BARD = "Helear:\n+ Restaura un 40HP de vida \n+ Coste Intermedio de Mana \n"
SPECIAL_ATTACK_C_DESC_BAR = "Remover Efecto:\n+ Remueve cualquier efecto que le hallan tirado\n+ Coste Intermedio de Mana \n"


# print(COMBAT_OPTIONS)
# input(USER_PROMPT)
# print(COMMON_ATTACKS_ARCHER)
# input(USER_PROMPT)

# with open("savefile.pickle", "rb") as f:
#     player_info = pickle.load()