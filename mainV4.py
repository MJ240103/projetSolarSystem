import pygame
import sys
from bodies import Planet
from bodies import runge_kutta
from collections import defaultdict
from bouton import Bouton
from paramSimu import *

# Initialisation de Pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Gravity simulation (SPACE: show orbits, '
                           'keypad +/- : zoom in/out)')
clock = pygame.time.Clock()

# Mire qui indique le centre de la fenêtre d'affichage et qui permet d'observer le mouvement du Soleil
# Couleur de la croix
CROSS_COLOR = (0, 0, 0)  # Blanc

# Position du centre de la fenêtre
center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2

# Longueur des bras de la croix
cross_length = 10

# Dessiner la croix
def draw_centered_cross(window, center_x, center_y, cross_length, color):
    # Ligne horizontale
    pygame.draw.line(window, color, (center_x - cross_length, center_y), (center_x + cross_length, center_y), 2)
    # Ligne verticale
    pygame.draw.line(window, color, (center_x, center_y - cross_length), (center_x, center_y + cross_length), 2)

facteurDistance = 5.0e11  # Facteur d'échelle des distances
facteurRayon = 1.0e8  # Facteur d'échelle des rayons

def realToDisplay(x,y,window_x,window_y,space_x,space_y):
    x = x*window_x/space_x
    y = y*window_y/space_y
    return x,y

# Création du bouton pause
#pause_bouton = Bouton(SCREEN_WIDTH - 150, SCREEN_HEIGHT - 850, 100, 40, "pause", WHITE, GREY, GREY)



keysPressed = defaultdict(bool)

zoom = 1.0

# Position de la caméra (coordonnées du centre de la vue)
#camera_x = 0
#camera_y = 0

# Boucle principale
running = True
#paused = False  # Variable pour suivre l'état de pause
# Variable pour contrôler l'affichage des trajectoires
show_orbits = False

window.fill(BLACK)
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si la fenêtre d'animation est fermée
            running = False  # Termine la boucle principale
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_PLUS:
                zoom /= 0.99  # Augmenter le zoom pour rapprocher
            elif event.key == pygame.K_KP_MINUS:
                zoom *= 0.99  # Réduire le zoom pour éloigner
            elif event.key == pygame.K_SPACE:
                show_orbits = not show_orbits  # Bascule de l'affichage des trajectoires
            elif event.key == pygame.K_ESCAPE:
                running = False  # Quitte la simulation

    # Mettre le fond en noir uniquement si les orbites ne sont pas affichées
    if not show_orbits:
        window.fill(BLACK)
            # Si le bouton pause est implémenté, ajouter ici la gestion de la touche de pause.
    
        # Si le bouton est cliqué alterner entre pause et reprise
        #if pause_bouton.is_clicked(event): # Vérifie si le bouton pause à été cliqué
            #paused = not paused #Si l'animation est en pause elle reprend, sinon elle se "pause " :)
            #pause_bouton.toggle_pause() #Lorsque l'on passe de l'état "pause" à "lancer" le texte change

        # Redessinez le bouton après modification
        #pause_bouton.draw(window)

    # Ajuster les échelles en fonction du zoom
    echelleDistances = SCREEN_HEIGHT * 2.0e-12 * zoom
    echelleRayonSoleil = SCREEN_HEIGHT * 3.0e-11 * zoom
    echelleRayonsPlanete = SCREEN_HEIGHT * 1.0e-6 * zoom

    
    # Mise à jour des planètes avec Runge-Kutta
    #if not paused:
    runge_kutta(solarSystem, G, dt)
    #print(solarSystem[0].position)
    for planet in solarSystem:
        #planet.selfVanish(solarSystem, soleil.position, soleil.rayon)
        
        planet.selfDraw(window, ECHELLE_RAYON, UNIVERSE_CENTER, SCREEN_WIDTH, SCREEN_HEIGHT, lambda x, y: realToDisplay(x, y, SCREEN_WIDTH, SCREEN_HEIGHT, SPACE_X * zoom, SPACE_Y* zoom))
    
    # Dessiner la croix au centre
    draw_centered_cross(window, center_x, center_y, cross_length, CROSS_COLOR)

    pygame.display.flip()
    
    # Afficher le bouton pause
    #pause_bouton.draw(window) 
    
    # Mettre à jour l'affichage
    pygame.display.update()

    clock.tick(FPS)

# Fermeture de PyGame à la fin de l'execution
pygame.quit()
sys.exit()
