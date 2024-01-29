#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| skill.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:31:48
# Last Modified: Mo, January 29th 2024, 22:38:10


from django.db import models
from .skill_base import SkillBase

class Skill(SkillBase):
    keybinds = (
        ("PASSIVE", "Passive"),
        ("Q", "Q"),
        ("W", "W"),
        ("E", "E"),
        ("R", "R"),
        ("D", "D"),
        ("F", "F"),
    )
    activation = models.CharField(max_length = 15, choices= keybinds, default= "PASSIVE")
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"