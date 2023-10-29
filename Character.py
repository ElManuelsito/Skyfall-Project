
# donde:
#       name = nombre del personaje
#       health = salud
#       armor = armadura    disminuirá el daño entrante
#       str = fuerza        multiplicador a la hora de atacar
#       agi = agilidad      multiplicador a la hora de atacar primero/intentar huir
#       int = inteligencia  multiplicador a la hora de atacar con magia
#       faith = fé          multiplicador a la hora de usar hechizo/habilidad especial
#       acc = puntería      multiplicador a la hora de atacar a distancia (arco)
#       res_magic = resistencia magica      reduce el daño entrante de ataques magicos
#       res_physc = resistencia fisica      reduce el daño entrante de ataques fisicos
#       money = dinero del personaje
#       lvl = nivel actual  si jugador sube de nivel adquiere 1 punto a invertir en una de los rasgos anteriores
#       exp = experiencia   al llegar a un cierto valor, aumenta el nivel en 1 y la experiencia vuelve a 0
#
#       armor_items_on = cantidad de items de armadura equipados, no puede tener más de 3 a la vez y deben ser de
#       distinto tipo (jugador no puede tener 2 pecheras a la vez)
#
#       weapon_items_on = cantidad de armas equipadas, no puede tener más de una cierta cantidad de armas y deben ser
#       de distinto tipo (no puede tener dos escudos a la vez, por ejemplo)


class Character:
    def __init__(self, name, health, armor, str, agi, int, faith,
                 acc, res_magic, res_phys, money, lvl, exp, armor_items_on, weapon_items_on):
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

    def takeDamage(self, enemy):
        self.health = self.health - (enemy.dmg - (enemy.dmg * (self.armor / 200)))
