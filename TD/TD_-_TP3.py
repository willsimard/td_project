from tkinter import *
import time
import math
from helper import Helper as HP


class Vue:
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()  # Cet objet est responsable de tout l'interface graphique
        self.creer_page_jeu()
        self.creeps = []
        self.id = 0
        self.tourPoison = []
        self.tourProjectile = []
        self.tourEclaire = []
        # self.afficher_debut()

    def creer_page_jeu(self):
        self.cadre_jeu = Frame(self.root)
        self.cadre_jeu.pack()
        self.canevas = Canvas(self.cadre_jeu, width=self.modele.largeur_grille * self.modele.taille_case,
                              height=self.modele.hauteur_grille * self.modele.taille_case)
        self.canevas.pack()

        # Dessiner le sentier
        self.sentier = [
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CC", "CV", "CV", "CC", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CC", "CC", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CC", "CC", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CC", "CC", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"]]

        for p in range(self.modele.hauteur_grille):
            for i in range(self.modele.largeur_grille):
                x = i * self.modele.taille_case
                y = p * self.modele.taille_case
                if self.sentier[p][i] == "CV":
                    self.canevas.create_rectangle(x, y, x + self.modele.taille_case, y + self.modele.taille_case,
                                                  fill="palegreen4", )

                elif self.sentier[p][i] == "CS":
                    self.canevas.create_rectangle(x, y, x + self.modele.taille_case, y + self.modele.taille_case,
                                                  fill="wheat1", )

                elif self.sentier[p][i] == "CC":
                    self.canevas.create_rectangle(x, y, x + self.modele.taille_case, y + self.modele.taille_case,
                                                  fill="darkgray", outline="gold")

        # buttons et labels
        self.label_chrono = Label(self.cadre_jeu, text="Chrono", font=("Arial", 13))
        self.label_chrono.place(x=self.modele.taille_case * 2, y=self.modele.taille_case * 20,
                                height=self.modele.taille_case * 2 - 1, width=self.modele.taille_case * 2)

        self.label_vague = Label(self.cadre_jeu, text="Vague", font=("Arial", 13))
        self.label_vague.place(x=self.modele.taille_case * 2, y=self.modele.taille_case * 22,
                               height=self.modele.taille_case * 2, width=self.modele.taille_case * 2)

        # self.label_choix_tour = tkinter.LabelFrame(self.cadre_jeu, text="Choix de tours", font=("Arial", 13))
        # self.label_choix_tour.pack(fill="both", expand="yes")
        # self.label_choix_tour.place(x=self.modele.taille_case * 5, y=self.modele.taille_case * 20)

        self.boutton_pro = Button(self.cadre_jeu, text="Projectile", font=("Arial", 13))
        self.boutton_pro.place(x=self.modele.taille_case * 7, y=self.modele.taille_case * 21.5,
                               height=self.modele.taille_case * 1.5, width=self.modele.taille_case * 3)

        self.boutton_ecl = Button(self.cadre_jeu, text="Éclair", font=("Arial", 13))
        self.boutton_ecl.place(x=self.modele.taille_case * 11, y=self.modele.taille_case * 21.5,
                               height=self.modele.taille_case * 1.5, width=self.modele.taille_case * 3)

        self.boutton_poi = Button(self.cadre_jeu, text="Poison", font=("Arial", 13))
        self.boutton_poi.place(x=self.modele.taille_case * 15, y=self.modele.taille_case * 21.5,
                               height=self.modele.taille_case * 1.5, width=self.modele.taille_case * 3)

        ## self.boutton_upgrade = Button(self.cadre_jeu, text="Amélioration", font=("Arial", 13))
        ##self.boutton_upgrade.place(x=self.modele.taille_case * 19, y=self.modele.taille_case * 21.5,
        ## height=self.modele.taille_case * 1.5, width=self.modele.taille_case * 3)

        self.label_nbr_vies = Label(self.cadre_jeu, text="Nbr de vies\n" + str(self.modele.vie), font=("Arial", 13))
        self.label_nbr_vies.place(x=self.modele.taille_case * 25, y=self.modele.taille_case * 21,
                                  height=self.modele.taille_case * 1, width=self.modele.taille_case * 3)

        self.label_argent = Label(self.cadre_jeu, text="Argent\n" + str(self.modele.argent), font=("Arial", 13))
        self.label_argent.place(x=self.modele.taille_case * 25, y=self.modele.taille_case * 22.5,
                                height=self.modele.taille_case * 1, width=self.modele.taille_case * 3)

        self.boutton_pro.bind("<ButtonRelease-1>", lambda event: (self.afficher_tour_projectile()))
        self.boutton_ecl.bind("<ButtonRelease-1>", lambda event: (self.afficher_tour_eclaire()))
        self.boutton_poi.bind("<ButtonRelease-1>", lambda event: (self.afficher_tour_poison()))

    # self.boutton_upgrade.bind("<ButtonRelease-1>", lambda event: (self.afficher_amelioration()))

    def afficher_vie(self):
        self.label_nbr_vies.config(text="Nbr de vies\n" + str(self.modele.vie))

    def afficher_argent(self):
        self.label_argent.config(text="Argent\n" + str(self.modele.argent))

    def afficher_creep(self):
        for creep in self.creeps:
            self.canevas.delete(creep)
        self.creeps = []
        taille_case = self.modele.taille_case
        for creep in self.modele.creeps:
            x = creep.x
            y = creep.y
            self.creeps.append(
                self.canevas.create_rectangle(x - taille_case / 2, y - taille_case / 2, x + taille_case /2,
                                              y + taille_case /2 , fill="blue"))

    def afficher_cadrier(self):
        for i in range(self.modele.largeur_grille + 1):
            x = i * self.modele.taille_case
            self.canevas.create_line(x, 0, x, self.modele.largeur_grille * self.modele.taille_case)

        for i in range(self.modele.hauteur_grille + 1):
            y = i * self.modele.taille_case
            self.canevas.create_line(0, y, self.modele.largeur_grille * self.modele.taille_case, y)

    def afficher_temps(self, temps):
        self.label_chrono.config(text=str(temps))

    def afficher_vague(self):
        self.label_vague.config(text=f"Vague\n{str(self.modele.niveau)}")

    def bind_escape(self):
        self.root.bind("<Escape>", self.on_escape)
        self.root.after(10000, lambda: (self.root.unbind("<Escape>")))

    def on_escape(self, event):
        self.root.unbind("<Escape>")
        self.modele.start_round()

    def bind_start_game(self):
       self.root.bind("<space>", self.parent.start_game)

    def bind_upgrade(self):
        self.root.bind('a', lambda event: self.afficher_amelioration())

    def afficher_debut(self):
        self.label_debut = Label(self.root, text="Bienvenue à Tower Defense!", font=("Arial", 25))
        self.label_debut.pack()
        self.boutton_debut = Button(self.root, text="Jouer", font=("Arial", 25))
        self.boutton_debut.pack()
        self.boutton_debut.bind("<ButtonRelease-1>", lambda event: (self.creer_page_jeu(), self.boutton_debut.forget(), self.label_debut.forget()))

    def afficher_projectiles(self):
        self.canevas.delete("projectile")
        taille_projectile = 3
        for projectile in self.modele.projectiles:
            if projectile.alive:
                projectile_tag = "projectile{}".format(id(projectile))
                self.canevas.create_oval(
                    projectile.x - taille_projectile,
                    projectile.y - taille_projectile,
                    projectile.x + taille_projectile,
                    projectile.y + taille_projectile,
                    fill="red",
                    tags=(projectile_tag, "projectile")
                )

    def on_press(self, event):
        start_x = self.canevas.canvasx(event.x)
        start_y = self.canevas.canvasy(event.y)
        self.canevas.data = {'start_x': start_x, 'start_y': start_y}

    def on_drag(self, event):
        cur_x = self.canevas.canvasx(event.x)
        cur_y = self.canevas.canvasy(event.y)
        self.canevas.move(self.tour, cur_x - self.canevas.data['start_x'], cur_y - self.canevas.data['start_y'])
        self.canevas.data['start_x'] = cur_x
        self.canevas.data['start_y'] = cur_y

    def on_release(self,event):
        self.canevas.tag_unbind(self.tour, '<ButtonPress-1>')
        self.canevas.tag_unbind(self.tour, '<B1-Motion>')
        self.canevas.tag_unbind(self.tour, '<ButtonRelease-1>')
        self.canevas.tag_unbind(self.tour, '<Button-3>')
        self.tourProjectile.append(self.tour)
        self.modele.tours.append(Tour(self.modele,event.x / self.modele.taille_case,event.y / self.modele.taille_case,"standard",30,300))
    def afficher_tour_poison(self):
        if self.modele.argent >= self.modele.cout_init_poi:
            self.modele.argent -= self.modele.cout_init_poi
            self.afficher_argent()
            taille_case = self.modele.taille_case


            x = 15 * taille_case
            y = 19 * taille_case
            self.tour = self.canevas.create_rectangle(x - taille_case / 2, y - taille_case / 2,
                                                          x + taille_case / 2, y + taille_case / 2,
                                                          fill="DarkGoldenrod1")

            self.canevas.tag_bind(self.tour, '<ButtonPress-1>', lambda e: self.on_press(e))
            self.canevas.tag_bind(self.tour, '<B1-Motion>', lambda e: self.on_drag(e))
            self.canevas.tag_bind(self.tour, '<ButtonRelease-1>', lambda e: self.on_release(e))
            self.canevas.tag_bind(self.tour, '<Button-3>', lambda e: self.afficher_amelioration())

    def afficher_tour_projectile(self):
        if self.modele.argent >= self.modele.cout_init_pro:
            self.modele.argent -= self.modele.cout_init_pro
            self.afficher_argent()
            taille_case = self.modele.taille_case


            x = 15 * taille_case
            y = 19 * taille_case

            self.tour = self.canevas.create_rectangle(x + taille_case / 2, y + taille_case / 2,
                                                      x + taille_case * 1.5,
                                                      y + taille_case * 1.5, fill="Red")
            self.canevas.tag_bind(self.tour, '<ButtonPress-1>', lambda e: self.on_press(e))
            self.canevas.tag_bind(self.tour, '<B1-Motion>', lambda e: self.on_drag(e))
            self.canevas.tag_bind(self.tour, '<ButtonRelease-1>', lambda e: self.on_release(e))
            self.canevas.tag_bind(self.tour, '<Button-3>', lambda e: self.afficher_amelioration())

    def afficher_tour_eclaire(self):
        if self.modele.argent >= self.modele.cout_init_ecl:
            self.modele.argent -= self.modele.cout_init_ecl
            self.afficher_argent()
            taille_case = self.modele.taille_case


            x = 15 * taille_case
            y = 19 * taille_case
            self.tour = self.canevas.create_rectangle(x - taille_case / 2, y - taille_case / 2,
                                                          x + taille_case /2 ,
                                                          y + taille_case /2, fill="deep sky blue")

            self.canevas.tag_bind(self.tour, '<ButtonPress-1>', lambda e: self.on_press(e))
            self.canevas.tag_bind(self.tour, '<B1-Motion>', lambda e: self.on_drag(e))
            self.canevas.tag_bind(self.tour, '<ButtonRelease-1>', lambda e: self.on_release(e))
            self.canevas.tag_bind(self.tour, '<Button-3>', lambda e: self.afficher_amelioration())

    def afficher_amelioration(self):
        taille_case = self.modele.taille_case
        x = taille_case
        y = taille_case
        self.canvas2 = Canvas(self.canevas, width=400, height=150, bg="old lace")
        self.canevas.create_window(200, 75, window=self.canvas2)

        self.boutton_close = Button(self.canvas2, text="X", font=("Arial", 13), bg="Red")
        self.boutton_close.place(x=380, y=0)
        self.carre = self.canvas2.create_rectangle(20, 50, x + taille_case*1.5, y + taille_case*3, fill="deep sky blue")

        self.canvas2.create_text(200,15, text="Améliorations", fill="black", font="Arial")
        self.canvas2.create_text(40,65, text="Cout", fill="black", font="Arial")

        self.force = Button(self.canvas2, text="+ Force", font=("Arial", 10))
        self.force.place(x=20, y=80)
        self.range = Button(self.canvas2, text="+ Etendu", font=("Arial", 10))
        self.range.place(x=20, y=110)
        self.force.bind("<ButtonRelease-1>", lambda event: "")
        self.boutton_close.bind("<ButtonRelease-1>", lambda event: self.canvas2.destroy())
        #self.canvas2.pack()



class Projectile:
    def __init__(self, parent, cible, force, empoisone, vitesse, type):
        self.parent = parent
        self.x, self.y = parent.x * self.parent.parent.taille_case, parent.y * self.parent.parent.taille_case
        self.cible = cible
        self.empoisone = empoisone
        self.vitesse = vitesse
        self.type = type

        self.cibleX = cible.x
        self.cibleY = cible.y
        self.alive = True
        self.cible = 0

    def deplacer_vers_cible(self):

        if self.alive:
            direction_x = self.cibleX - self.x
            direction_y = self.cibleY - self.y

            distance = math.sqrt(direction_x ** 2 + direction_y ** 2)

            if distance != 0:
                direction_x /= distance
                direction_y /= distance

            taille_case = (self.parent.parent.taille_case / 2)

            self.x += direction_x * self.vitesse
            self.y += direction_y * self.vitesse
            # verifie quil ne touche pas un creep
            for creep in self.parent.parent.creeps:
                if creep.x + taille_case > self.x and creep.x - taille_case < self.x:
                    if creep.y + taille_case > self.y and creep.y - taille_case < self.y:
                        self.cible = creep
                        self.alive = False
                        break

            # Vérifier si le projectile a atteint sa cible (ou à proximité)

            if HP.calcDistance(self.cibleX,self.cibleY,self.x,self.y) < self.vitesse:
                self.x, self.y = self.cibleX,self.cibleY
                self.alive = False

        else:
            taille_case = (self.parent.parent.taille_case / 2)


            self.parent.delete_projectile(self)
            if self.cible:
                self.parent.parent.creeps.remove(self.cible)


class Tour:
    def __init__(self, parent, x, y, type, cout_amelioration, range):
        self.parent = parent
        self.x = x  # case
        self.y = y  # case
        self.type = type
        self.niveau = 1
        self.cout_amelioration = cout_amelioration
        self.range = range  # radius (diametre/2)
        self.dernier_tir = 0
        self.intervalle_tir = 2
        self.force = 10
        self.empoisone = False
        self.vitesse = 10
        self.type_projectile = "standard"

        self.force = 1

    def peut_tirer(self):
        return time.time() - self.dernier_tir >= self.intervalle_tir

    def attacker(self):
        if self.peut_tirer():
            cible = self.trouver_cible()
            if cible != False:  # si cible non nul
                projectile = Projectile(self, cible, self.force, self.empoisone, self.vitesse, self.type_projectile)
                self.parent.ajouter_projectile(projectile)
                self.dernier_tir = time.time()

    def ameliorerForce(self):
        self.force += 2
        self.cout_amelioration -= 10

    def trouver_cible(self):
        for creep in self.parent.creeps:

            distance = math.sqrt(
                (creep.x - self.x * self.parent.taille_case) ** 2 + (creep.y - self.y * self.parent.taille_case) ** 2)
            if distance <= self.range:
                return creep
        return False


    def delete_projectile(self, projectile):
        self.parent.projectiles.remove(projectile)


class Creep:
    def __init__(self, parent, x, y, mana):
        self.parent = parent
        self.x = x
        self.y = y
        self.mana = mana
        self.empoisone = False
        self.temps_empoisone = 0
        self.speed = 5
        self.creep_check_points = [(4, 18), (10, 18), (10, 6), (26, 6), (26, 11), (16, 11), (16, 18), (28, 18)]
        for i, point in enumerate(self.creep_check_points):
            self.creep_check_points[i] = (point[0] * self.parent.taille_case, point[1] * self.parent.taille_case)
        self.start = 0
        self.cible = self.creep_check_points[0]
        self.cible_i = 0
        self.angle = HP.calcAngle(self.x, self.y, self.cible[0], self.cible[1])

    def deplacer(self):
        cx, cy = self.cible
        distance = HP.calcDistance(self.x, self.y, cx, cy)
        if distance <= self.speed:
            self.cible_i += 1
            if self.cible_i <= len(self.creep_check_points) - 1:
                self.cible = self.creep_check_points[self.cible_i]
                self.angle = HP.calcAngle(self.x, self.y, self.cible[0], self.cible[1])
            else:
                self.parent.lose_life(self)
        self.x, self.y = HP.getAngledPoint(self.angle, self.speed, self.x, self.y)


class Modele:
    def __init__(self, parent):
        self.game_over = False
        self.parent = parent
        self.tours = []
        self.creep_par_round = 20

        self.mana_init = 20
        self.pause_cree = True
        self.creeps = []
        self.projectiles = []
        # amelioration = 1.5^(niveau_tour) * cout_init_tour
        self.cout_init_pro = 30
        self.cout_init_ecl = 50
        self.cout_init_poi = 40
        self.rayon_pro = 5
        self.rayon_ecl = 3
        self.rayon_poi = 4
        self.taille_case = 35
        self.largeur_grille = 32
        self.hauteur_grille = 24
        self.argent = 100
        self.vie = 20
        self.niveau = 1
        self.round_started = False
        self.start = 0
        self.projectiles = []
        self.argent_par_creep = 15


    def deplacer_creeps(self):
        for creep in self.creeps:
            creep.deplacer()

    def creer_creep(self):
        case_x = 4
        case_y = 0
        self.creeps.append(
            Creep(self, case_x * self.taille_case, case_y * self.taille_case, self.mana_init * self.niveau))
        self.creep_cree -= 1

    def delete_creep(self, creep):
        self.creeps.remove(creep)
        self.argent += self.argent_par_creep

    def lose_life(self, creep):
        self.vie -= 1
        self.parent.vue.afficher_vie()
        self.creeps.remove(creep)
        if self.vie <= 0:
            self.parent.game_over()

    def finish_round(self):
        self.round_started = False
        self.time_round_ended = time.time()
        self.niveau += 1

    def start_round(self):
        self.round_started = True
        self.creep_cree = self.creep_par_round
        self.creer_creep()

    def ajouter_projectile(self, projectile):
        self.projectiles.append(projectile)

    def delete_projectile(self, projectile):
        self.projectiles.remove(projectile)


class Controler:
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.afficher_creep()
        self.vue.bind_start_game()
        self.vue.bind_upgrade()
        self.tick = 0
        self.interval_time = 30
        self.ms_before_next_creep = 400
        # self.vue.afficher_demarrage()
        # self.boucler()

    def start_loop(self):
        if not self.modele.game_over:
            if self.modele.creep_cree > 0 and self.modele.round_started:
                self.tick += self.interval_time
                if self.tick >= self.ms_before_next_creep:
                    self.tick = 0
                    self.modele.creer_creep()
            elif not self.modele.creeps and self.modele.round_started:
                self.modele.finish_round()
                self.vue.afficher_vague()
            if not self.modele.round_started:
                if time.time() - self.modele.time_round_ended <= 10:
                    self.vue.bind_escape()
                else:
                    self.modele.start_round()
            for tour in self.modele.tours:
                if self.modele.creeps:
                    tour.attacker()
            self.vue.afficher_temps(f"{time.time() - self.modele.start:0.2f}")
            self.modele.deplacer_creeps()
            self.vue.afficher_creep()
            self.vue.afficher_argent()
            self.vue.id = self.vue.root.after(self.interval_time, self.start_loop)
            for projectile in self.modele.projectiles:
                projectile.deplacer_vers_cible()
            self.vue.afficher_projectiles()

    def start_game(self, event):
        self.vue.root.unbind("<space>")
        self.modele.start = time.time()
        self.modele.start_round()
        self.vue.afficher_vague()
        self.start_loop()

    def game_over(self):
        self.modele.game_over = True
        self.vue.root.after_cancel(self.vue.id)


if __name__ == '__main__':
    c = Controler()
    c.vue.root.mainloop()
