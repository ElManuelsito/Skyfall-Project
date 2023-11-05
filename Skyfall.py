# Ejecutable del juego, no cumple otra función más comenzarlo
import pickle
import time
import Item
import os
import ClassesRPG.Archer as Cl_Archer

# cualquier otra cosa que no sean estas 3 de abajo hay que borrarlas despues lol
from GameManager import GameManager
Manager = GameManager()
Manager.initializeGame()


# os.remove("savefile.pickle")
# Player = Cl_Archer.Archer("Manu")
# player_info = {"weapon_1": Item.sword_bahvagraba,
#                "weapon_2": False,
#                "helmet": False,
#                "breastplate": Item.armor_breastplate_silenthills,
#                "chausses": False,
#                "gauntlets": False,
#                "money": 0,
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