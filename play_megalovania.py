# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 08:47:29 2021

@author: Magatsu
"""

# Imports
from mingus.containers.note import Note
from mingus.containers import Bar
from mingus.midi import fluidsynth
import time

# Defining variables
fluidsynth.init("path/to/your/FluidR3_GM.sf2")
tempo=250
b = Bar()
b.set_meter((4,4))

print(" ")
print("Playing Megalovania")
print(" ")

time.sleep(1.1)

b.place_notes("E-5", 4)
b.place_notes("E-5", 4)
b.place_notes("E-6", 7/3)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("B-5", 8/3)
b.place_rest(4)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("A#-5", 7/3)
b.place_rest(16)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("A#-5", 8/3)
b.place_rest(16)
b.place_notes("G-5", 3)
b.place_rest(16)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("E-5", 4)
b.place_notes("G-5", 4)
b.place_notes("A-5", 7/3)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("D-5", 4)
b.place_notes("D-5", 4)
b.place_notes("E-6", 7/3)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("B-5", 8/3)
b.place_rest(4)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("A#-5", 7/3)
b.place_rest(16)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("A#-5", 8/3)
b.place_rest(16)
b.place_notes("G-5", 3)
b.place_rest(16)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("E-5", 4)
b.place_notes("G-5", 4)
b.place_notes("A-5", 7/3)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("Cb-5", 4)
b.place_notes("Cb-5", 4)
b.place_notes("E-6", 7/3)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("B-5", 8/3)
b.place_rest(4)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("A#-5", 7/3)
b.place_rest(16)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("A#-5", 8/3)
b.place_rest(16)
b.place_notes("G-5", 3)
b.place_rest(16)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("E-5", 4)
b.place_notes("G-5", 4)
b.place_notes("A-5", 7/3)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("C-5", 4)
b.place_notes("C-5", 4)
b.place_notes("E-6", 7/3)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("B-5", 8/3)
b.place_rest(4)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("A#-5", 7/3)
b.place_rest(16)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("A#-5", 8/3)
b.place_rest(16)
b.place_notes("G-5", 3)
b.place_rest(16)

fluidsynth.play_Bar(b, 1, tempo)
b.empty()

b.place_notes("E-5", 4)
b.place_notes("G-5", 4)
b.place_notes("A-5", 7/3)

fluidsynth.play_Bar(b, 1, tempo)
