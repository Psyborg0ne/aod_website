#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| item_details.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Mo, January 29th 2024, 22:53:34
# Last Modified: Mo, January 29th 2024, 23:27:49

from django.shortcuts import get_object_or_404, render
from wiki.models.item import Item

def item_details(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    return render(request, "wiki/ItemTemplate.html", {"page_title": f"Wiki - {item.name}", "item": item})