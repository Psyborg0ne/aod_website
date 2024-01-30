#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| hero_base.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:30:00
# Last Modified: Tu, January 30th 2024, 21:05:46

from django.db import models
from .wiki_base import Base
from .wiki_tier import HeroTier
from filer.fields.image import FilerImageField
from django.utils.html import mark_safe

class HeroBase(Base):
    base_dmg    = models.IntegerField(name= "dmg", verbose_name= "Base Damage", blank= True, default= 0)
    base_armor  = models.IntegerField(name= "armor", verbose_name= "Base Armor", blank= True, default= 0)
    base_str    = models.IntegerField(name= "str", verbose_name= "Base STR", blank= True, default= 0)
    base_agi    = models.IntegerField(name= "agi", verbose_name= "Base AGI", blank= True, default= 0)
    base_int    = models.IntegerField(name= "int", verbose_name= "Base INT", blank= True, default= 0)

    htier  = models.ForeignKey(HeroTier, name="tier", verbose_name = "Hero Tier", on_delete= models.SET_NULL, null= True)
    bckgnd_img = FilerImageField(name= 'image', related_name= 'hero_image', null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Hero Base"
        verbose_name_plural = "Heroes Base"
        abstract = True

    def bckgnd(self):
        return mark_safe(f'<img height=100px width=200px src="{self.bckgnd_img.url}" />')
    
    bckgnd.short_description = 'Background'