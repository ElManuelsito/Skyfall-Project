class PointOfInterest:
    def __init__(self, name,
                 brief_description,
                 possible_enemies,
                 possible_npcs,
                 possible_events):
        self.name = name
        self.brief_description = brief_description
        self.possible_enemies = possible_enemies
        self.possible_npcs = possible_npcs
        self.possible_events = possible_events

    def triggerEvent(self):
        pass


Muldraugh = PointOfInterest("Muldraugh",
                            "Un reino gobernado por familias corruptas desde milenio y niveles"
                            " de crimenes que pondrían\nhasta a el Paladin más fuerte preguntandose si de "
                            "verdad vale la pena vivir aquí.\nAl menos, las mercancías no decepcionan... "
                            "si se tiene un puñado de lo que tiene el rey, claro.",
                            possible_enemies=[],
                            possible_npcs=[],
                            possible_events=[]
                            )
Riverside = PointOfInterest("Riverside",
                            "Una pequeña villa con habitantes memorables y una hospitalidad no encontrada en"
                            " ningún otro reino.\nLuego de una disputa entre el rey y su mano derecha, esta villa nace "
                            "a modo de protesta contra las acciones y decisiones que el primero tomaba.\n\"Con un río y"
                            " dos manos no hay rey que haga falta\", demostró aquel segundo al mando."
                            "\nCuenta con todo lo que uno pueda necesitar para comenzar su aventura.",
                            possible_enemies=[],
                            possible_npcs=[],
                            possible_events=[]
                            )
