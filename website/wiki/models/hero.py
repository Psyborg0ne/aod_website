#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| hero.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:30:05
# Last Modified: Mo, January 29th 2024, 23:52:37

from .hero_base import HeroBase

class Hero(HeroBase):
    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Heroes"