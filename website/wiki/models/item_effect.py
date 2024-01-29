#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| item_effects.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:24:50
# Last Modified: Mo, January 29th 2024, 22:27:30

from django.db import models
from .wiki_base import Base

class ItemEffect(Base):
    effect_chance = models.IntegerField(name= "chance", verbose_name= "Chance", blank= True, default= 0)
    effect_potency = models.IntegerField(name= "potency", verbose_name= "Potency", blank= True, default= 0)

    class Meta:
        verbose_name          = "Item Effect"
        verbose_name_plural   = "Item Effects"
        unique_together = ("name","chance","potency" )

    def __str__(self):
        return self.eff_description()
    
    def eff_description(self):
        if(self.chance != 0 and self.potency != 0):
            return self.description.format(self.chance, self.potency) 
        elif(self.chance != 0 and self.potency == 0):
            return self.description.format(self.chance) 
        elif(self.chance == 0 and self.potency != 0):
            return self.description.format(self.potency) 
    eff_description.short_description = "Effect Description"