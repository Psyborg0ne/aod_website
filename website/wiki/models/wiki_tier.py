#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| tier.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:43:34
# Last Modified: Tu, January 30th 2024, 21:09:50

from django.db import models
from .wiki_base import Base

class TierBase(Base):
    tier_number = models.IntegerField(name= "tier_number", verbose_name= "Tier", blank= True, default= 0)

    def save(self, *args, **kwargs):
        self.description = 'T{}'
        super(TierBase, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Tier Base"
        verbose_name_plural = "Tier Base"
        abstract = True

class HeroTier(TierBase):
    def __str__(self):
        return self.hero_tier_description()
    
    def hero_tier_description(self):
            return self.description.format(self.tier_number) 
    hero_tier_description.short_description = "Tier Description"

    class Meta:
        verbose_name = "Hero Tier"
        verbose_name_plural = "Hero Tiers"

class SkillTier(TierBase):
    def __str__(self):
        return self.skill_tier_description()
    
    def skill_tier_description(self):
            return self.description.format(self.tier_number) 
    skill_tier_description.short_description = "Tier Description"
    
    class Meta:
        verbose_name = "Skill Tier"
        verbose_name_plural = "Skill Tiers"