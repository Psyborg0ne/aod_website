#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| hero_admin.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 23:22:49
# Last Modified: Mo, January 29th 2024, 23:24:39

from django.contrib             import admin
from .wiki_admin                import BaseAdmin, HeroBaseAdmin

from wiki.models.hero           import Hero

@admin.register(Hero)
class HeroAdmin(HeroBaseAdmin):
    pass