# print(INTRO_GAME)
# se deben guardar las constantes en un archivo "constant"
# INTRO_GAME = "INTRODUCCIÓN AL JUEGO"
# MENU = "1- Entrar al juego" \
#        "2- Etc."
# MAX_PLAYERS = 5


# -------------------- Menu Related --------------------
# [ PLAYER INTERACTION WITH SYSTEM]

PLAYER_PROMPT_OPTION = "Opción: "
PLAYER_PROMPT_NAME = "Nombre: "
PLAYER_PROMPT_ITEM_NUMBER = "Item: "
PRESS_ENTER_TO_CONTINUE = "\nPresiona Enter para continuar...\n"
PRESS_ENTER_TO_RETURN = "\nPresiona Enter para volver...\n"

# [ OPTIONS, MESSAGES AND WARNINGS ]
WELCOMING_MESSAGE = "\n\n                    ~ Skyfall ~\nSelecciona una opción ingresando su número por teclado.\n"
MAIN_MENU_OPTIONS = "1. Nuevo juego\n2. Continuar\n3. Instrucciones\n4. Salir\n"
WARNING_MESSAGE_INVALID_MAIN_MENU_OPTION = "No existe esa opción! Por favor selecciona una de las opciones dadas."
WARNING_MESSAGE_CHOICE_IS_NOT_NUMERIC = "Por favor ingresa solamente números."
MAIN_MENU_MESSAGE_SAVEFILE_ALREADY_EXISTS = "Advertencia! Ya existe un archivo de guardado!\nSi eliges continuar ahora se eliminará tu progreso y tendrás que comenzar desde cero.\n"
MAIN_MENU_MESSAGE_SAVEFILE_DELETE_CONFIRMATION = "¿Deseas continuar? (si/no)"
MAIN_MENU_MESSAGE_SAVEFILE_DELETED = "\nEl archivo a sido eliminado\n"
MAIN_MENU_MESSAGE_SAVEFILE_NOT_DELETED_GOING_BACK_TO_MENU = "\nVolviendo al menu principal..."
MAIN_MENU_MESSAGE_GAME_LOADING = "\n\n\n\nCargando mundo..."
PLAYER_PROMPT_SET_FOR_YES = {"s", "S", "si", "sí", "SI", "SÍ", "Si", "Sí", "sI", "sÍ", "y", "Y", "yes", "Yes", "YES"}   # estructura de datos Set, incluye posibilidades para la respuesta del usuario "si"
PLAYER_PROMPT_SET_FOR_NO = {"no", "No", "NO", "nO", "n", "N"}                                                           # misma estructura, pero para "No"
PLAYER_INVENTORY_MESSAGE = "Actualmente tienes estos items:\n"
PLAYER_INVENTORY_MESSAGE_WEAPONS = "\nArmas:"
PLAYER_INVENTORY_MESSAGE_POTIONS = "\nPociones:"
PLAYER_INVENTORY_MESSAGE_ARMORS = "\nArmaduras:"
PLAYER_INVENTORY_MESSAGE_NO_ITEMS = "No tienes ningún item de este tipo"
PLAYER_INVENTORY_MESSAGE_ACTIONS = "Decide qué quieres hacer (seleccionar/volver)"
WARNING_MESSAGE_INVALID_INVENTORY_ACTION = "Por favor solo ingresa \"seleccionar\" o \"volver\""
WARNING_MESSAGE_INVALID_INVENTORY_ITEM_ACTION = "Por favor solo ingresa \"descartar\", \"equipar\" o \"usar\""
PLAYER_INVENTORY_ACTION_SET_SELECT = {"seleccionar"}
PLAYER_INVENTORY_ACTION_SET_RETURN = {"volver"}
PLAYER_INVENTORY_ACTION_SET_DISCARD = {"descartar"}
PLAYER_INVENTORY_ACTION_SET_EQUIP = {"equipar"}
PLAYER_INVENTORY_ACTION_SET_USE = {"usar"}
PLAYER_INVENTORY_SELECTED_ITEM = "Item seleccionado:"
PLAYER_INVENTORY_SELECTED_ITEM_OPTIONS = "¿Qué deseas hacer con él? (descartar/equipar/usar)"
PLAYER_INVENTORY_ALREADY_HAS_WEAPON = "Ya tienes un arma equipada, ¿quieres reemplazarla? (si/no)"
PLAYER_INVENTORY_NEW_WEAPON_EQUIPPED = "Te has equipado el arma seleccionada"
PLAYER_INVENTORY_ALREADY_HAS_ARMOR = "Ya tienes eso puesto, ¿Quieres reemplazarlo?"
PLAYER_INVENTORY_NEW_ARMOR_EQUIPPED = "Te has equipado la nueva armadura"
PLAYER_INVENTORY_CANNOT_EQUIP_ITEM = "No puedes equiparte eso!"
PLAYER_INVENTORY_ITEM_WAS_DISCARDED = "Has descartado:"
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
                          "\n"
INTRO_MESSAGE_MULDRAUGH = "Un punzante dolor te despierta de tu sueño repentino, todo tu alrededor parece dar vueltas" \
                          " y no logras alcanzar a comprender tu situación.\nTratas de recomponerte, y luego de un rato" \
                          " comienzas a recordar, esos bandidos se llevaron todo!\n\nSabías que venir a este reino no" \
                          " era buena idea, pero la invitación al Cuarto Real era muy tentadora para no aceptarla." \
                          "\nRecoges lo primero que encuentras entre la basura, y emprendes viaje para vengarte de " \
                          "aquellos que te hicieron daño.\n"

WORLD_PLAYER_DECIDE_WHAT_TO_DO = "Decide qué hacer:\n\n1. Viajar\n2. Inspeccionarse\n3. Guardar y salir\n"
WORLD_PLAYER_IS_IN_POI = "Ahora mismo te encuentras en:"
WORLD_AVAILABLE_POI = "Lugares disponibles:"
WORLD_TRAVEL_CONFIRMATION = "¿Deseas ir aquí? (si/no)"
WORLD_TRAVEL_GOING_TO_PLACE = "\nEstas en camino a:"
WARNING_MESSAGE_INVALID_TRAVEL_CHOICE = "No existe ese lugar, por favor selecciona una de las opciones."
WORLD_FORAGE_ITEM_FOUND = "\nHas encontrado algo! Encontraste:"
WORLD_FORAGE_NO_ITEM_FOUND = "\nNo has encontrado nada..."

# -------------------- Combat Related --------------------
# [ GENERAL OPTIONS & MESSAGES ]
COMBAT_OPTIONS = "Decide qué hacer:\n1. Ataque comun     2. Habilidades\n" \
                 "3. item                4. Huir\n"
SPECIAL_ATTACK_CONFIRM = "¿Deseas usar esta habilidad? (si/no)"
SOMEONE_ATTACKS = "ataca!"
SOMEONE_ATTACKS_AND_MISSES = "intentó atacar, pero falló!"
SOMEONE_RECEIVES_DAMAGE = "recibe daño:"
SOMEONE_FLED = "no pudo soportalo y salió corriendo!"
SOMEONE_FLED_AND_FAILED = "...pero no logró escapar."
SOMEONE_FLED_AND_SUCCEEDED = "...y escapó."
SOMEONE_is_DEFEATED = "no puede continuar, y es derrotado!"
PLAYER_USED_HEALING_MESSAGE_START = "Te curaste, recuperas"
PLAYER_USED_HEALING_MESSAGE_HP = "HP"
PLAYER_USED_MANA_MESSAGE_START = "Tomas una poción de mana, recuperas"
PLAYER_USED_MANA_MESSAGE_SK = "SK"
BASE_ACC = 70


# [ ARCHER ]
SPECIAL_ATTACK_ARCHER = "\nHabilidad\n1. Lluvia de flechas\n"
SPECIAL_ATTACK_DESC_ARCH = "Lluvia de flechas:\n+ Daña a un objetivo\n- Coste de Mana: Intermedio\n"

# [Wizard]
SPECIAL_ATTACK_WIZARD = "\nHabilidad:\n1.Bola de Fuego\n"
SPECIAL_ATTACK_DESC_WIZ = "Bola de Fuego:\n+ Mete mucho daño a un objetivo\n- Coste Mana : Intermedio\n"

# [Warrior]
SPECIAL_ATTACK_WARRIOR = "\nHabilidad:\n1.Multiple cortes\n"
SPECIAL_ATTACK_DESC_WARR = "Multilple Cortes:\n+ Provoca un daño intermedio a un objetivo \n- Coste de Mana: Bajo\n"

# [THIEF]
SPECIAL_ATTACK_THIEF = "\nHabilidad\n1.Golpe bajo\n"
SPECIAL_ATTACK_DESC_THIE = "Golpe Bajo:\n+ Provoca un daño intermedio a un objetivo golpeando en los puntos bajo \n- Coste de Mana: Bajo\n"

# [SORCERER]
SPECIAL_ATTACK_SORC = "\nHabilidad:\n1.Magia Control\n"
SPECIAL_ATTACK_DESC_SORC = "Magia Control :\n+ Controla por un breve momento al enemigo haciendo que se lastime el mismo \n- Coste de Mana: Intermedio\n"

# [Paladin]
SPECIAL_ATTACK_PAL = "\nHabilidad\n1.Sentencia\n"
SPECIAL_ATTACK_DESC_PAL = "Sentencia:\n+ Juzga al enemigo provocandole un daño con la espada sagrada \n- Coste Bajo de Mana\n"

# [NECROMANCER]
SPECIAL_ATTACK_NEC = "\nHabilidad:\n1.Invocacion NO-MUERTO \n"
SPECIAL_ATTACK_DESC_NEC = "Invoacion NO-MUERTO:\n+ Invoca personas sin vida para atacar a un objetivo \n- Coste de Mana :Intermedio\n"

# [TANK]
SPECIAL_ATTACK_TANK = "\nHabilidad:\n1.Power up\n"
SPECIAL_ATTACK_DESC_TANK = "Power UP:\n+ Hace que su ataque aumente \n- Coste de Mana: Intermedio \n"

# [BARD]
SPECIAL_ATTACK_BARD = "\nHabilidad:\n1.Inspiracion \n"
SPECIAL_ATTACK_DESC_BARD = "Ispiracion:\n+ Sube los stat de si mismo inspirandose \n- Coste de Mana: Intermedio\n"
