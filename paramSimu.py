from bodies import Planet
from random import *
### CONSTANTES ###

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 50)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
ORANGE = (255, 165, 50)
PURPLE = (148, 0, 211)
GREY = (128, 128, 128)

FPS = 120

# Constantes astronomiques
G = -6.67384e-11

# Intervalle de temps (en secondes)
dt = 7.2e4  # correspond à environ 1 jour (86400 secondes approximées à moins car simulation trop lente sinon)
SPACE_X = 1e5
SPACE_Y = 1e5
UNIVERSE_CENTER = (SPACE_X//2,SPACE_Y//2)
ECHELLE_RAYON = 1


### PLANETES ###
solarSystem = [] #Initialisation de la liste de planètes


""" COMMENT CREER UNE PLANETE :
solarSystem.append(Planet(
    nom="PLANETE",
    masse = 0 # Masse en kg
    rayon = 0 # Masse en m
    position = [0,0] # Position dans l'Espace
    vitesse = [0, 0] # Vitesse initiale
    acceleration=[0, 0] # Accélération initiale
    couleur=WHITE
))

"""

# Création des planètes
    # Mercure

for i in range(0,10):
    solarSystem.append(Planet(
    nom="Planete{}".format(str(i)),
    masse=randint(1e3,1e5),  
    rayon=randint(SPACE_X//100,SPACE_X//50),  
    position=[uniform(SPACE_X/4,3*SPACE_X/4) - SPACE_X//2, uniform(SPACE_Y/4,3*SPACE_Y/4) - SPACE_Y//2],  
    vitesse=[0,0],  
    acceleration=[0, 0],
    couleur=(randint(0,255),randint(0,255),randint(0,255))
    ))
