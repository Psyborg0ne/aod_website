#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| item_recipe.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:39:12
# Last Modified: Mo, January 29th 2024, 22:49:45


from django.db import models
from .item_base import ItemBase
from .item import Item

class ItemRecipe(ItemBase):
    materials = models.ManyToManyField(Item, name="materials", verbose_name="Materials")

    class Meta:
        verbose_name         = "Recipe Item"
        verbose_name_plural  = "Recipe Items"