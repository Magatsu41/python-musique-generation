# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:37:24 2021

@author: Magatsu
"""


# Imports
from mingus.containers.note import Note
from mingus.containers import Bar
from mingus.midi import fluidsynth
from random import randrange
import sys
import time

# **************
# Classes
# **************

# Class MyNote
class MyNote:
    note = ""
    pod = 0.0
    def __init__(self, n, p):
        self.note = n
        self.pod = p

# Defining variables
fluidsynth.init("path/to/your/FluidR3_GM.sf2")
gamme = []
gammeIn = 0
tempo = 0
chiffrage = 0
mesure_count = 0
max_note = 0
dur_count = 0
dur_list = []

# INIT SCRIPT
print("Démarrage du créateur de musique de Magatsu v0.1a")
print(" ")
print("Saisissez le tempo (en bpm) de la mélodie, exemple : 120")
print(" ")
tempo = input("Bpm : ")
tempo = int(tempo)
print(" ")
print("Choisissez un métrique pour votre morceau :")
print(" ")
print("1 : 4/4")
print(" ")
chiffrage = input("Métrique : ")
chiffrage = int(chiffrage)

if chiffrage==1:
    chiffrage=4
    dur_list = [1, 2, 4]
    dur_count = 3
    print(" ")
    print("Vous avez sélectionné le métrique 4/4")
else:
    print(" ")
    sys.exit("Vous n'avez pas choisi une option correcte. Veillez recommencer.")

print(" ")
print("Veuillez choisir le nombre de mesure à jouer :")
mesure_count = input("- ")
mesure_count = int(mesure_count)
print(" ")
print(str(mesure_count)+" seront jouées")

print(" ")
print("Quelle gamme voulez vous utiliser ?")
print(" ")
print("1 : Gamme de DO complete (12 notes, 4ème octave)")
print("2 : Gamme de Jerome (6 notes, 4ème octave)")
print("3 : Gamme de Do (8 notes, 4ème octave)")
print(" ")
gammeIn = input("Gamme : ")
gammeIn = int(gammeIn)

if gammeIn==1:
    gamme.append(MyNote("C-4", 1.0))
    gamme.append(MyNote("C#-4", 1.5))
    gamme.append(MyNote("D-4", 2.0))
    gamme.append(MyNote("D#-4", 2.5))
    gamme.append(MyNote("E-4", 3.0))
    gamme.append(MyNote("F-4", 3.5))
    gamme.append(MyNote("F#-4", 4.0))
    gamme.append(MyNote("G-4", 4.5))
    gamme.append(MyNote("G#-4", 5.0))
    gamme.append(MyNote("A-4", 5.5))
    gamme.append(MyNote("A#-4", 6.0))
    gamme.append(MyNote("B-4", 6.5))
    max_note = 12
    print(" ")
    print("Vous avez choisi la gamme : "+str(gamme))
elif gammeIn==2:
    gamme.append(MyNote("C-4", 1.0))
    gamme.append(MyNote("D-4", 2.0))
    gamme.append(MyNote("D#-4", 2.5))
    gamme.append(MyNote("F-4", 3.5))
    gamme.append(MyNote("G-4", 4.5))
    gamme.append(MyNote("G#-4", 5.0))
    gamme.append(MyNote("A#-4", 6.0))
    gamme.append(MyNote("C-5", 7.0))
    max_note = 8
    print(" ")
    print("Vous avez choisi la gamme : "+str(gamme))
elif gammeIn==3:
    gamme.append(MyNote("C-4", 1.0))
    gamme.append(MyNote("D-4", 2.0))
    gamme.append(MyNote("E-4", 3.0))
    gamme.append(MyNote("F-4", 3.5))
    gamme.append(MyNote("G-4", 4.5))
    gamme.append(MyNote("A-4", 5.5))
    gamme.append(MyNote("B-4", 6.5))
    gamme.append(MyNote("C-5", 7.0))
    max_note = 8
    print(" ")
    print("Vous avez choisi la gamme : "+str(gamme))
else:
    print(" ")
    sys.exit("Vous n'avez pas choisi une option correcte. Veillez recommencer.")

print(" ")
print("Initialisation du script terminé, la génération va commencer...")
print(" ")

time.sleep(1.1)

# ******************
# FUNCTIONS
# ******************

# generate music
def gen_song():
    i=0
    last_pod = 0.0
    ronde = False
    while i<mesure_count:
        t=0.0
        b = Bar()
        b.set_meter((chiffrage,4))
        while t<chiffrage:
            if t==0.0:
                dur = dur_list[int(randrange(dur_count))]
                if ronde==True:
                    dur=4
                    ronde=False
                if dur==1:
                    ronde=True
                mote = gamme[int(randrange(max_note))]
                is_good = False
                while is_good==False:
                    mote = gamme[int(randrange(max_note))]
                    is_good = check_tone(mote.pod, last_pod)
                b.place_notes(mote.note, dur)
                last_pod = mote.pod
                t=le_temps(dur)
                print("Ajout de la note "+mote.note+" sur "+str(le_temps(dur))+" temp(s)")
            else:
                is_good = False
                dur = 0
                while is_good==False:
                    dur = dur_list[int(randrange(dur_count))]
                    is_good=check_tim(le_temps(dur), t)
                mote = MyNote("C-4", 1.0)
                is_good = False
                while is_good==False:
                    mote = gamme[int(randrange(max_note))]
                    is_good = check_tone(mote.pod, last_pod)
                b.place_notes(mote.note, dur)
                last_pod = mote.pod
                t=t+le_temps(dur)
                print("Ajout de la note "+mote.note+" sur "+str(le_temps(dur))+" temp(s)")
        i=i+1
        print("En train de jouer la mesure "+str(i))
        fluidsynth.play_Bar(b, 1, tempo)
    time.sleep(3.0)
    return

def le_temps(durdur):
    if durdur==1:
        return 4.0
    elif durdur==2:
        return 2.0
    elif durdur==4:
        return 1.0

def check_tim(titi, timo):
    if timo+titi>chiffrage:
        return False
    else:
        return True

def check_tone(t1, t2):
    if (t1!=t2) and (abs(t1-t2)==3):
        return False
    if tempo<300:
        if (t1!=t2) and (abs(t1-t2)<1.5):
            return False
        elif (t1!=t2) and (abs(t1-t2)>4.5):
            return False
    else:
        return True

gen_song()
