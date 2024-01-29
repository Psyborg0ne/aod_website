#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| skill_type.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:35:20
# Last Modified: Mo, January 29th 2024, 22:35:27

from .wiki_base import Base

class SkillType(Base):
    class Meta:
        verbose_name = "Skill Type"
        verbose_name_plural = "Skill Types"