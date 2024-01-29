#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| item_admin.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 23:05:24
# Last Modified: Mo, January 29th 2024, 23:13:24

from django.contrib             import admin
from .wiki_admin                import BaseAdmin, ItemBaseAdmin

from wiki.models.item           import Item
from wiki.models.item_recipe    import ItemRecipe
from wiki.models.item_effect    import ItemEffect
from wiki.models.item_rarity    import ItemRarity
from wiki.models.item_type      import ItemType


@admin.register(Item)
class ItemAdmin(ItemBaseAdmin):
    pass

@admin.register(ItemRecipe)
class ItemRecipeAdmin(ItemBaseAdmin):
    fieldsets = ItemBaseAdmin.fieldsets + [("Materials", {"fields": ["materials"]})]

@admin.register(ItemEffect)
class ItemEffectAdmin(BaseAdmin):
    fieldsets = BaseAdmin.fieldsets + [
        ("Effect Values", {"fields": ["chance", "potency"]}),
    ]
    list_display = BaseAdmin.list_display + ["chance", "potency", "eff_description"]
    list_editable = BaseAdmin.list_editable + ("chance", "potency") 

@admin.register(ItemRarity)
class ItemRarityAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ["description"]

@admin.register(ItemType)
class ItemTypeAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ["description"]