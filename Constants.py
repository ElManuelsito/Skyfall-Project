#     print(INTRO_GAME)
# se deben guardar las constantes en un archivo "constant"
# INTRO_GAME = "INTRODUCCION AL JUEGO"
# MENU = "1- Entrar al juego" \
#        "2- Etc."
# MAX_PLAYERS = 5

# -- Testeando pickle --
import pickle

player_inv = {"weapon_1": False, "weapon_2": False, "helmet": False, "breastplate": False, "chausses": False,
              "gauntlets": False, "money": 0}
with open("savefile.pickle", "wb") as f:
    pickle.dump(player_inv, f, protocol=0)
f.close()

with open("savefile.pickle", "rb") as f:
    player_inv = pickle.load(f)
f.close()
print(player_inv.items())

# -- --

welcoming_message = "Bienvenido a Skyfall. Selecciona una opción ingresando su número por teclado.\n"
main_menu_options = "1. Nuevo juego\n2. Continuar\n3.Opciones\n4. Salir"




