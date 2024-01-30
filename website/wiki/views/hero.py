#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| hero.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Tu, January 30th 2024, 21:12:01
# Last Modified: Tu, January 30th 2024, 21:13:28



from django.shortcuts import get_object_or_404, render
from wiki.models.hero import Hero

def hero_details(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)

    return render(request, "wiki/HeroTemplate.html", {"page_title": f"Wiki - {hero.name}", "hero": hero})