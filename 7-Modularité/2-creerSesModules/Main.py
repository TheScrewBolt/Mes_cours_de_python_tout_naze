#coding:utf-8
"""
Nos modul s'appel de la meme facon que les modules natif
"""
import Modules

Modules.parler("Screw", "Me suis tapé ta soeur")
Modules.auRevoir("Screw")

#--------------------------------------------------#

import fonctions_sup.mod_2

fonctions_sup.mod_2.adition(1,3)

#--------------------------------------------------#

import fonctions_sup.mod_2 as mod_2

mod_2.adition(6,8)
