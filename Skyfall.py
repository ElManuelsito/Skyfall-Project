# Ejecutable del juego, no cumple otra función más comenzarlo
# import pickle
# import time
# import Item
# import os
# import ClassesRPG.Archer as Cl_Archer
import random

# cualquier otra cosa que no sean estas 3 de abajo hay que borrarlas después lol
from GameManager import GameManager
Manager = GameManager()
Manager.initializeGame()


# os.remove("savefile.pickle")
# Player = Cl_Archer.Archer("Manu")
# player_info = {"weapon_1": Item.BowNewborn,
#                "helmet": False,
#                "breastplate": False,
#                "chausses": False,
#                "gauntlets": False,
#                "backpack_items": {"weapons": [],
#                                   "potions": [],
#                                   "armors": []},
#                "location": None}
#
# with open("savefile.pickle", "wb") as f:
#     pickle.dump(player_info, f, protocol=0)
#     pickle.dump(Player, f, protocol=0)
#     f.close()
# with open("savefile.pickle", "rb") as f:
#     player_info = pickle.load(f)
#     Player = pickle.load(f)
#     f.close()
#Hola