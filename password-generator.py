# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:40:14 2021

@author: Jonathan D
"""

import random

# voir correspondance avec la table ASCII
depart = 33
fin = 126

reponse = int(input('Nombre de caractère du mot de passe : ' ))

pwd_gen = str()

for i in range(reponse):
    pwd_gen = pwd_gen + chr(random.randint(depart, fin))

print(pwd_gen)