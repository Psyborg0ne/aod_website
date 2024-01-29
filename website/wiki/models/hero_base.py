#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| hero_base.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:30:00
# Last Modified: Mo, January 29th 2024, 22:46:37

from .wiki_base import Base

class HeroBase(Base):
    class Meta:
        verbose_name = "Hero Base"
        verbose_name_plural = "Heroes Base"
        abstract = True