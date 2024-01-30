#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| hero_admin.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 23:22:49
# Last Modified: Tu, January 30th 2024, 21:07:59

from django.contrib             import admin
from .wiki_admin                import BaseAdmin,HeroBaseAdmin

from wiki.models.hero           import Hero
from wiki.models.hero_class     import HeroClass
from wiki.models.wiki_tier      import HeroTier

@admin.register(Hero)
class HeroAdmin(HeroBaseAdmin):
    fieldsets = HeroBaseAdmin.fieldsets + [(None, {"fields": ["class", "image"]}),
                                                ("Base Stats", {"fields": ["str", "agi", "int"]}), 
                                                ("Other Stats", {"fields": ["dmg", "armor"]}), 
                                                ]
    list_display = HeroBaseAdmin.list_display + [ "class", "tier", "str", "agi", "int", "dmg", "armor"]
    list_editable = ["class", "tier", "str", "agi", "int", "dmg", "armor"]


@admin.register(HeroClass)
class HeroClassAdmin(BaseAdmin):
    fieldsets = BaseAdmin.fieldsets + [(None, {"fields": ["class", "image"]})]

@admin.register(HeroTier)
class HeroTierAdmin(BaseAdmin):
    fieldsets = BaseAdmin.fieldsets + [(None, {"fields": ["tier_number"]})]
    list_display = BaseAdmin.list_display + ["hero_tier_description"]