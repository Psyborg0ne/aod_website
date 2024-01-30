#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| hero_class.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Tu, January 30th 2024, 20:01:59
# Last Modified: Tu, January 30th 2024, 21:06:12


from django.db import models
from .wiki_base import Base
from filer.fields.image import FilerImageField
from django.utils.html import mark_safe

class HeroClass(Base):
    classes = (
            ("DPS", "DPS"),
            ("TANK", "TANK"),
            ("HEAL", "HEAL"),
        )
    hclass = models.CharField(name= 'class', max_length = 15, choices= classes, default= "DPS")
    bckgnd_img= FilerImageField(name= 'image', related_name= 'class_image', null=True, blank=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = "Hero Class"
        verbose_name_plural = "Heroes Classes"

    def bckgnd(self):
        return mark_safe(f'<img height=100px width=200px src="{self.bckgnd_img.url}" />')
    
    bckgnd.short_description = 'Background'