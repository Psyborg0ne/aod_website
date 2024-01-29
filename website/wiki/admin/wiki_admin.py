#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| wiki_admin.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 23:05:44
# Last Modified: Mo, January 29th 2024, 23:36:37

from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "description", "icon"]}),
    ]

    list_display = ["icon_thumb", "name"]
    list_display_links = ["name"]
    search_fields = ["name"]

class ItemBaseAdmin(BaseAdmin):
    fieldsets = BaseAdmin.fieldsets + [
        ("Item", {"fields": [("type", "rarity")]}),
        ("Base Stats", {"fields": ["str", "agi", "int"]}),
        ("Additional Stats", {"fields": [("dmg", "armor")]}),
        ("Cost", {"fields": [("souls", "souls_divine")]}),
        ("Effects", {"fields": ["effects"]})
    ]
    list_display = BaseAdmin.list_display + ["rarity", "type", "str", "agi", "int", "souls", "souls_divine"]
    list_editable = ["rarity", "type", "str", "agi", "int", "souls", "souls_divine"]
    search_fields = BaseAdmin.search_fields + ["rarity"]

class HeroBaseAdmin(BaseAdmin):
    pass