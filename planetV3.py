import math
import pygame

class Planet:
    def __init__(self, nom, masse, rayon, position, vitesse, acceleration, couleur):
        self.nom = nom
        self.masse = masse
        self.rayon = rayon
        self.position = position  # (x, y)
        self.vitesse = vitesse  # (vx, vy)
        self.acceleration = acceleration  # (ax, ay)
        self.couleur = couleur

    def gravite(self, autres_planetes, G):
        """Calcule l'accélération en fonction des autres planètes et du Soleil."""
        ax, ay = 0, 0
        for autre_planete in autres_planetes:
            if autre_planete != self:
                dx = autre_planete.position[0] - self.position[0]
                dy = autre_planete.position[1] - self.position[1]
                print(dx, dy)
                distance = math.sqrt(dx**2 + dy**2)
                force = G * autre_planete.masse / distance**2
                ax += force * dx / distance
                ay += force * dy / distance
        return ax, ay

    def runge_kutta_step(self, autres_planetes, G, dt):
        """Exécute une étape de Runge-Kutta 4 pour mettre à jour la position et la vitesse. Remplace setPosition"""
        
        # k1 pour la position et la vitesse
        k1_vx, k1_vy = self.acceleration
        k1_px, k1_py = self.vitesse
        
        # Appliquer la gravité pour k1
        ax1, ay1 = self.gravite(autres_planetes, G)

        # k2
        vx2 = self.vitesse[0] + 0.5 * dt * ax1
        vy2 = self.vitesse[1] + 0.5 * dt * ay1
        px2 = self.position[0] + 0.5 * dt * k1_px
        py2 = self.position[1] + 0.5 * dt * k1_py
        
        ax2, ay2 = self.gravite(autres_planetes, G)

        # k3
        vx3 = self.vitesse[0] + 0.5 * dt * ax2
        vy3 = self.vitesse[1] + 0.5 * dt * ay2
        px3 = self.position[0] + 0.5 * dt * k1_px
        py3 = self.position[1] + 0.5 * dt * k1_py

        ax3, ay3 = self.gravite(autres_planetes, G)

        # k4
        vx4 = self.vitesse[0] + dt * ax3
        vy4 = self.vitesse[1] + dt * ay3
        px4 = self.position[0] + dt * k1_px
        py4 = self.position[1] + dt * k1_py
        
        ax4, ay4 = self.gravite(autres_planetes, G)

        # Mise à jour finale
        self.vitesse[0] += (dt / 6) * (ax1 + 2*ax2 + 2*ax3 + ax4)
        self.vitesse[1] += (dt / 6) * (ay1 + 2*ay2 + 2*ay3 + ay4)
        
        self.position[0] += (dt / 6) * (k1_px + 2*px2 + 2*px3 + px4)
        self.position[1] += (dt / 6) * (k1_py + 2*py2 + 2*py3 + py4)
    
    def selfVanish(self, solarSystem, position_soleil, rayon_soleil):
        """Supprime la planète si elle est recouverte par le Soleil."""
        dx = self.position[0] - position_soleil[0]
        dy = self.position[1] - position_soleil[1]
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance < (self.rayon + rayon_soleil):
            solarSystem.remove(self)

    def selfDraw(self, window, echelle_distance, echelle_rayon, centrage, SCREEN_WIDTH, SCREEN_HEIGHT, convertFun):
        """Affiche une planète dans la fenêtre Pygame."""

        rayon = convertFun(self.rayon, self.rayon)[0]/(echelle_rayon)
        x_affiche,y_affiche = convertFun(centrage[0] + self.position[0], centrage[1] + self.position[1])
        x_affiche,y_affiche = centrage[0] + x_affiche, centrage[1] + y_affiche
        
        #print(x_affiche,y_affiche, centrage)
        #realToDisplay(x,y,1000,1000,1e13,1e13)
        
        # Ne dessiner que si la planète est dans la fenêtre
        pygame.draw.circle(window, self.couleur, (x_affiche, y_affiche), rayon)