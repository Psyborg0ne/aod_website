#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| skill_admin.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 23:14:20
# Last Modified: Mo, January 29th 2024, 23:24:48

from django.contrib             import admin
from .wiki_admin                import BaseAdmin

from wiki.models.skill          import Skill
from wiki.models.skill_type     import SkillType
from wiki.models.wiki_tier      import SkillTier

@admin.register(Skill)
class SkillAdmin(BaseAdmin):
    fieldsets = BaseAdmin.fieldsets + [(None, {"fields": [("activation", "tier", "types")]})]
    list_display = BaseAdmin.list_display + ["tier", "activation"]
    list_editable = BaseAdmin.list_editable + ("tier",)

@admin.register(SkillType)
class SkillTypeAdmin(BaseAdmin):
    pass

@admin.register(SkillTier)
class SkillTierAdmin(BaseAdmin):
    fieldsets = BaseAdmin.fieldsets + [(None, {"fields": ["tier_number"]})]
    list_display = BaseAdmin.list_display + ["skill_tier_description"]



