#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| item_type.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:24:41
# Last Modified: Mo, January 29th 2024, 22:27:34

from .wiki_base import Base

class ItemType(Base):
     class Meta:
          verbose_name          = "Item Type"
          verbose_name_plural   = "Item Types"