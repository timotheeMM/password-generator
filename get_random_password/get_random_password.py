# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:40:14 2021

@author: Jonathan D
"""

import random

def get_random_password(nb_caracteres):
    # voir correspondance avec la table ASCII
    depart = 33
    fin = 126

    pwd_gen = str()

    for i in range(nb_caracteres):
        pwd_gen = pwd_gen + chr(random.randint(depart, fin))

    return pwd_gen
