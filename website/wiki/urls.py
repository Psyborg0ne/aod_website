#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| urls.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : Fr, January 12th 2024, 21:26:50
# Last Modified: Mo, January 29th 2024, 23:25:18



from django.urls import path
from wiki.views import item

# app_name = "wiki"
urlpatterns = [
    path("<int:item_id>/", item.item_details, name="details_item"),
]