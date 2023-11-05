class PointOfInterest:
    def __init__(self, name,
                 description,
                 possible_enemies,
                 possible_npcs,
                 possible_events,
                 possible_items,
                 connected_locations):
        self.name = name
        self.description = description
        self.possible_enemies = possible_enemies
        self.possible_npcs = possible_npcs
        self.possible_events = possible_events
        self.possible_items = possible_items
        self.connected_locations = connected_locations

    def triggerEvent(self):
        pass


# -------------------- Villages (populated and safe areas) --------------------

Muldraugh = PointOfInterest("Muldraugh",
                            "Un reino gobernado por familias corruptas desde milenio y niveles"
                            " de crimenes que pondrían\nhasta a el Paladin más fuerte preguntandose si de "
                            "verdad vale la pena vivir aquí.\nAl menos, las mercancías no decepcionan... "
                            "si se tiene un puñado de lo que tiene el rey, claro.\n",
                            possible_enemies=None,
                            possible_npcs=[],
                            possible_events=[],
                            possible_items=None,
                            connected_locations=[]
                            )
Riverside = PointOfInterest("Riverside",
                            "Una pequeña villa con habitantes memorables y una hospitalidad no encontrada en"
                            " ningún otro reino.\nLuego de una disputa entre el rey y su mano derecha, esta villa nace "
                            "a modo de protesta contra las acciones y decisiones que el primero tomaba.\n\"Con un río y"
                            " dos manos no hay rey que haga falta\", demostró aquel segundo al mando."
                            "\nCuenta con todo lo que uno pueda necesitar para comenzar su aventura.\n",
                            possible_enemies=None,
                            possible_npcs=[],
                            possible_events=[],
                            possible_items=None,
                            connected_locations=[]
                            )


# -------------------- Shops --------------------

RiversideAlchemist = PointOfInterest("Todd el Alquimista",
                                     "Un viejo alquimista dispuesto a ofrecer cualquier tipo de pociones que un "
                                     "aventurero pueda necesitar.\nTambién puedes vender pociones que no necesites.\n",
                                     possible_enemies=None,
                                     possible_npcs=None,
                                     possible_events=None,
                                     possible_items=[],
                                     connected_locations=[]
                                     )
RiversideBlacksmith = PointOfInterest("Howard el Herrero",
                                      "Un preciado herrero de la villa, joven,"
                                      " pero sus habilidades no deben ser subestimadas.\nPuedes comprar o vender "
                                      "cualquier tipo de armas aquí, solamente no esperes nada fuera del otro mundo.\n",
                                      possible_enemies=None,
                                      possible_npcs=None,
                                      possible_events=None,
                                      possible_items=[],
                                      connected_locations=[]
                                      )
MuldraughBlacksmith = PointOfInterest("Andre el Legendario Herrero",
                                      "Un maestro de su arte, no hay explorador o viajero que no lo conozca.\nSe dice"
                                      " que ha vivido por siglos, y que incluso ayudó al gran \"Ser de la Ceniza\","
                                      " otro nombre importante dentro de la esfera aventurera, pero no lo reconoces.\n"
                                      "Objetos y armamentos de excelente calidad garantizados si se tiene el capital "
                                      "requerido.",
                                      possible_enemies=None,
                                      possible_npcs=None,
                                      possible_events=None,
                                      possible_items=[],
                                      connected_locations=[]
                                      )



# -------------------- Dungeons (unsafe areas) --------------------

ForestOFMagic = PointOfInterest("Bosque de la Magia",
                                "Un bosque caracterizado por su gran cantidad de recursos y enemigos leves.\n"
                                "Es posible encontrar enemigos, armamentos y protecciones comunes. No ofrece"
                                " mucho más que eso.\n",
                                possible_enemies=[],
                                possible_npcs=None,
                                possible_events=[],
                                possible_items=[],
                                connected_locations=[]
                                )
DeepRockCaverns = PointOfInterest("Cavernas de la Profunda Roca",
                                  "Cuevas de hace mucho tiempo atrás, no es el lugar más seguro del planeta, pero "
                                  "quien se atreva a aventurarlo será recompensado.\nEs necesario atravesar las cuevas"
                                  " si se quiere llegar al reino de Muldraugh.\n",
                                  possible_enemies=[],
                                  possible_npcs=None,
                                  possible_events=[],
                                  possible_items=[],
                                  connected_locations=[]
                                  )
VengefulMountains = PointOfInterest("Montañas Vengativas",
                                    "Altas montañas que no perdonan incluso al más bondadoso de los juglares.\nGran"
                                    " peligro acecha por estas partes, pero quien salga vivo volverá con riquezas "
                                    "considerables.\n",
                                    possible_enemies=[],
                                    possible_npcs=None,
                                    possible_events=[],
                                    possible_items=[],
                                    connected_locations=[]
                                    )

# -------------------- Establishing Connections Between POIs --------------------
Riverside.connected_locations = [RiversideBlacksmith,
                                 RiversideAlchemist,
                                 ForestOFMagic,
                                 DeepRockCaverns]

Muldraugh.connected_locations = [DeepRockCaverns,
                                 MuldraughBlacksmith,
                                 VengefulMountains]

ForestOFMagic.connected_locations = [Riverside]

DeepRockCaverns.connected_locations = [Riverside,
                                       Muldraugh]

VengefulMountains.connected_locations = [Muldraugh]


