import Item


class PointOfInterest:
    def __init__(self, name,
                 description,
                 possible_enemies,
                 possible_npcs,
                 possible_events,
                 possible_items,
                 connected_locations,
                 classification):
        self.name = name
        self.description = description
        self.possible_enemies = possible_enemies
        self.possible_npcs = possible_npcs
        self.possible_events = possible_events
        self.possible_items = possible_items
        self.connected_locations = connected_locations
        self.classification = classification


# -------------------- Villages (populated and safe areas) --------------------

Muldraugh = PointOfInterest("Muldraugh",
                            "\nUn reino gobernado por familias corruptas desde milenio y niveles"
                            " de crimenes que pondrían\nhasta al Paladin más fuerte preguntándose si de "
                            "verdad vale la pena vivir aquí.\nAl menos, las mercancías no decepcionan... "
                            "si se tiene un puñado de lo que tiene el rey, claro.\n",
                            possible_enemies=None,
                            possible_npcs=[],
                            possible_events=[],
                            possible_items=None,
                            connected_locations=[],
                            classification="safe"
                            )
Riverside = PointOfInterest("Riverside",
                            "\nUna pequeña villa con habitantes memorables y una hospitalidad no encontrada en"
                            " ningún otro reino.\nLuego de una disputa entre el rey y su mano derecha, esta villa nace "
                            "a modo de protesta contra las acciones y decisiones que el primero tomaba.\n\"Con un río y"
                            " dos manos no hay rey que haga falta\", demostró aquel segundo al mando."
                            "\nCuenta con todo lo que uno pueda necesitar para comenzar su aventura.\n",
                            possible_enemies=None,
                            possible_npcs=[],
                            possible_events=[],
                            possible_items=None,
                            connected_locations=[],
                            classification="safe"
                            )


# -------------------- Shops --------------------

RiversideAlchemist = PointOfInterest("Todd el Alquimista",
                                     "Un viejo alquimista dispuesto a ofrecer cualquier tipo de pociones que un "
                                     "aventurero pueda necesitar.\nTambién puedes vender pociones que no necesites.\n",
                                     possible_enemies=None,
                                     possible_npcs=None,
                                     possible_events=None,
                                     possible_items=[],
                                     connected_locations=[],
                                     classification="shop"
                                     )
RiversideBlacksmith = PointOfInterest("Howard el Herrero",
                                      "Un preciado herrero de la villa, joven,"
                                      " pero sus habilidades no deben ser subestimadas.\nPuedes comprar o vender "
                                      "cualquier tipo de armas aquí, solamente no esperes nada fuera del otro mundo.\n",
                                      possible_enemies=None,
                                      possible_npcs=None,
                                      possible_events=None,
                                      possible_items=[],
                                      connected_locations=[],
                                      classification="shop"
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
                                      connected_locations=[],
                                      classification="shop"
                                      )


# -------------------- Dungeons (unsafe areas) --------------------

ForestOFMagic = PointOfInterest("Bosque de la Magia",
                                "\nUn bosque caracterizado por su gran cantidad de recursos y enemigos leves.\n"
                                "Es posible encontrar enemigos, armamentos y protecciones comunes. No ofrece"
                                " mucho más que eso.\n",
                                possible_enemies=[],
                                possible_npcs=None,
                                possible_events=[],
                                possible_items=[],
                                connected_locations=[],
                                classification="unsafe"
                                )
ForestOFMagicForageableArea = PointOfInterest("Busqueda amplia de la zona",
                                              "\nPuedes buscar al rededor del bosque y encontrar oro, objetos, y por"
                                              " supuesto, compañia.\n",
                                              possible_enemies=[],
                                              possible_npcs=None,
                                              possible_events=[],
                                              possible_items=[],
                                              connected_locations=[],
                                              classification="searchable common"
                                              )
DeepRockCaverns = PointOfInterest("Cavernas de la Profunda Roca",
                                  "\nCuevas de hace mucho tiempo atrás, no es el lugar más seguro del planeta, pero "
                                  "quien se atreva a aventurarlo será recompensado.\nEs necesario atravesar las cuevas"
                                  " si se quiere llegar al reino de Muldraugh.\n",
                                  possible_enemies=[],
                                  possible_npcs=None,
                                  possible_events=[],
                                  possible_items=[],
                                  connected_locations=[],
                                  classification="unsafe"
                                  )
DeepRockCavernsForageableArea = PointOfInterest("Busqueda amplia de la zona",
                                              "\nPuedes buscar al rededor de la cueva y encontrar oro, "
                                              "objetos, y por supuesto, compañia.\n",
                                                possible_enemies=[],
                                                possible_npcs=None,
                                                possible_events=[],
                                                possible_items=[],
                                                connected_locations=[],
                                                classification="searchable uncommon"
                                                )
VengefulMountains = PointOfInterest("Montañas Vengativas",
                                    "\nAltas montañas que no perdonan incluso al más bondadoso de los juglares.\nGran"
                                    " peligro acecha por estas partes, pero quien salga vivo volverá con riquezas "
                                    "considerables.\n",
                                    possible_enemies=[],
                                    possible_npcs=None,
                                    possible_events=[],
                                    possible_items=[],
                                    connected_locations=[],
                                    classification="unsafe"
                                    )
VengefulMountainsForageableArea = PointOfInterest("Busqueda amplia de la zona",
                                                  "\nPuedes buscar al rededor de la cueva y encontrar oro, "
                                                  "objetos, y por supuesto, compañia.\n",
                                                  possible_enemies=[],
                                                  possible_npcs=None,possible_events=[],
                                                  possible_items=[],
                                                  connected_locations=[],
                                                  classification="searchable legendary"
                                                  )

# -------------------- Establishing Connections Between POIs --------------------

Riverside.connected_locations = [RiversideBlacksmith,
                                 RiversideAlchemist,
                                 ForestOFMagic,
                                 DeepRockCaverns]

Muldraugh.connected_locations = [DeepRockCaverns,
                                 MuldraughBlacksmith,
                                 VengefulMountains]

ForestOFMagic.connected_locations = [Riverside,
                                     ForestOFMagicForageableArea]

DeepRockCaverns.connected_locations = [Riverside,
                                       Muldraugh]

VengefulMountains.connected_locations = [Muldraugh]

ForestOFMagicForageableArea.connected_locations = [ForestOFMagic]
ForestOFMagicForageableArea.possible_items = Item.items_common
DeepRockCavernsForageableArea.connected_locations = [DeepRockCaverns]
DeepRockCavernsForageableArea.possible_items = Item.items_uncommon
VengefulMountainsForageableArea.connected_locations = [VengefulMountains]
VengefulMountainsForageableArea.possible_items = Item.items_legendary



