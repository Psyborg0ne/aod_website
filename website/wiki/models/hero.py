#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| hero.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:30:05
# Last Modified: Tu, January 30th 2024, 20:16:45

from django.db import models
from .hero_base import HeroBase
from .hero_class import HeroClass

class Hero(HeroBase):
    hclass = models.ForeignKey(HeroClass, name = "class", verbose_name = "Hero Class", on_delete=models.SET_NULL, null= True)

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Heroes"