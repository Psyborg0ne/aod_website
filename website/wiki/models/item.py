#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| item.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:30:11
# Last Modified: Mo, January 29th 2024, 22:49:36

from .item_base import ItemBase

class Item(ItemBase):
    class Meta:
        verbose_name         = "Item"
        verbose_name_plural  = "Items"