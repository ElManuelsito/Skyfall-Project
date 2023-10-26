
# donde: name es el nombre del personaje
#       health es la salud
#       armor es el valor de armadura, el cual disminuirá el daño entrante
#       str la fuerza, multiplicador a la hora de atacar
#       agi la agilidad, multiplicador a la hora de atacar primero y huir
#       int la inteligencia, multiplicador a la hora de atacar con magia
#       faith la fé, multiplicador a la hora de usar hechizo/habilidad especial
#       acc la puntería, multiplicador a la hora de usar un arma de rango (arco)
#       res_magic la resistencia magica, reduce el daño entrante de ataques magicos
#       res_physc la resistencia fisica, reduce el daño entrante de ataques fisicos
#       money el dinero del personaje
#       lvl el nivel actual, si jugador sube de nivel adquiere 1 punto a invertir en una de los rasgos anteriores
#       exp la experiencia, al llegar a un cierto valor, aumente el nivel en 1 y la experiencia vuelve a 0.
#       armor_items_on la cantidad de items de armadura equipados, no puede tener más de 3 a la vez y deben ser de
#       distinto tipo (jugador no puede tener 2 pecheras a la vez)
#
#       weapon_items_on la cantidad de armas equipadas, no puede tener más de una cierta cantidad de armas y deben ser
#       de distinto tipo (no puede tener dos escudos a la vez, por ejemplo)


class Character:
    def __init__(self, name="", health=0, armor=0, str=0, agi=0, int=0, faith=0,
                 acc=0, res_magic=0, res_phys=0, money=0, lvl=0, exp=0, armor_items_on=0, weapon_items_on=0):
        self.name = name
        self.health = health
        self.armor = armor
        self.str = str
        self.agi = agi
        self.int = int
        self.faith = faith
        self.acc = acc
        self.res_magic = res_magic
        self.res_phys = res_phys
        self.money = money
        self.lvl = lvl
        self.exp = exp
        self.armor_items_on = armor_items_on
        self.weapon_items_on = weapon_items_on


