
class location:
    def __init__(self, name, description, events=[]):
        self.name = name
        self.description = description
        self.events = events

    def enter(self):
        print(f"Te encuentras en {self.name}. {self.description}")
        for event in self.events:
            event.trigger()


class Event:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def trigger(self):
        print(f"Event: {self.name}\n{self.description}")


class Encounter:
    def __init__(self, name, description, outcome):
        self.name = name
        self.description = description
        self.outcome = outcome

    def resolve(self):
        print(f"Encuentro: {self.name}\n{self.description}")
        print(f"Resultado: {self.outcome}")


# Crear ubicaciones
location1 = Location("Bosque Encantado", "Un oscuro bosque con árboles altos y misteriosos.")
location2 = Location("Ciudad Perdida", "Una antigua ciudad en ruinas llena de tesoros ocultos.")
location3 = Location("Playa Solitaria", "Una playa de arena blanca con un mar turquesa y un faro al fondo.")

# Crear eventos
event1 = Event("Lluvia de meteoritos", "De repente, una lluvia de meteoritos ilumina el cielo nocturno.")
event2 = Event("Hallazgo de un mapa antiguo", "Encuentras un mapa antiguo que marca un tesoro en la Ciudad Perdida.")
event3 = Event("Tormenta en el horizonte", "Una tormenta se acerca desde el mar mientras estás en la Playa Solitaria.")

# Crear encuentros
encounter1 = Encounter("Bestia del Bosque", "Una bestia gigante emerge de la oscuridad del bosque.",
                       "Puedes huir o enfrentarla.")
encounter2 = Encounter("Guardianes de la Ciudad", "Dos guardianes mágicos bloquean la entrada a la Ciudad Perdida.",
                       "Debes resolver un enigma para pasar.")
encounter3 = Encounter("Náufragos varados", "Encuentras a un grupo de náufragos en la playa que necesitan ayuda.",
                       "Puedes ayudarlos o seguir tu camino.")

# Asignar eventos y encuentros a las ubicaciones
location1.events = [event1, encounter1]
location2.events = [event2, encounter2]
location3.events = [event3, encounter3]

# Simulación del juego
while True:
    print("Elige una ubicación para explorar:")
    print("1. Bosque Encantado")
    print("2. Ciudad Perdida")
    print("3. Playa Solitaria")
    choice = input("Ingresa el número de la ubicación (1/2/3) o 'q' para salir: ")

    if choice == 'q':
        break

    if choice == '1':
        location1.enter()
    elif choice == '2':
        location2.enter()
    elif choice == '3':
        location3.enter()
    else:
        print("Ubicación no válida. Elige una opción válida.")
