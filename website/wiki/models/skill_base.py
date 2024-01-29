#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| skill_base.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:31:38
# Last Modified: Mo, January 29th 2024, 22:44:33

from django.db import models
from .wiki_base import Base
from .wiki_tier import SkillTier
from .skill_type import SkillType

class SkillBase(Base):
    skill_tier = models.ForeignKey(SkillTier, name="tier", verbose_name = "Skill Tier", on_delete= models.SET_NULL, null= True)
    skill_type = models.ManyToManyField(SkillType, name='types', verbose_name="Skill Types")
    class Meta:
        verbose_name = "Skill Base"
        verbose_name_plural = "Skill Base"
        abstract = True