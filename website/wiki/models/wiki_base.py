#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| wiki_base.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:20:00
# Last Modified: Mo, January 29th 2024, 22:47:30

from django.db import models
from django.contrib.auth.models import User
from filer.fields.image import FilerImageField
from django.utils.html import mark_safe

class Base(models.Model):
    name                = models.CharField(name= 'name', max_length= 50, blank= False)
    description         = models.CharField(name= 'description', blank= True, max_length=250, default= 'Placeholder description.')
    icon                = FilerImageField(name= 'icon', null=True, blank=True, on_delete=models.SET_NULL)
    
    modified_by         = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, name= "modified_by", verbose_name= "Modified By", editable= False)
    last_modified       = models.DateTimeField(auto_now= True, name="last_modified", verbose_name="Last modified on", editable= False)

    class Meta:
         abstract = True

    def __str__(self):
        return self.name
    
    def icon_thumb(self):
        return mark_safe(f'<img height=32px width=32px src="{self.icon.url}" />')
    
    icon_thumb.short_description = 'Icon Thumbnail'