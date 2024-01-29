#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| item_base.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:17:38
# Last Modified: Mo, January 29th 2024, 22:49:21


from django.db import models
from .wiki_base import Base
from .item_rarity import ItemRarity
from .item_type import ItemType
from .item_effect import ItemEffect

class ItemBase(Base):
    strength        = models.IntegerField(name= "str", verbose_name= "STR", blank= True, default= 0)
    agility         = models.IntegerField(name= "agi", verbose_name= "AGI", blank= True, default= 0)
    intelligence    = models.IntegerField(name= "int", verbose_name= "INT", blank= True, default= 0)

    damage          = models.IntegerField(name= "dmg", verbose_name= "Damage", blank= True, default= 0)
    armor           = models.IntegerField(name="armor", verbose_name= "Armor", blank= True, default= 0)  

    souls           = models.IntegerField(name="souls", verbose_name="Soul Essence", blank= True, default= 0)
    souls_divine    = models.IntegerField(name="souls_divine", verbose_name= "Divine Essence", blank= True, default= 0)
    
    rarity          = models.ForeignKey(ItemRarity, name = "rarity", verbose_name = "Item Rarity", on_delete=models.SET_NULL, null= True)
    type            = models.ForeignKey(ItemType, name="type", verbose_name = "Item Type", on_delete= models.SET_NULL, null= True)

    effects         = models.ManyToManyField(ItemEffect, name='effects', verbose_name="Item Effects")
    
    class Meta:
        verbose_name        = "Item Base"
        verbose_name_plural = "Item Bases"
        unique_together = ("name", "rarity", "type" )
        abstract = True