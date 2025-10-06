# This file defines the different routes and branches in the game, affecting the story's development.

# Define the routes for the game
define route_1 = "李慕云线"
define route_2 = "其他角色线"

# Function to handle route selection
label start:
    menu:
        "选择你的路线":
            "李慕云线":
                jump li_muyun_route
            "其他角色线":
                jump other_character_route

label li_muyun_route:
    # Add specific events and choices for 李慕云线
    "你选择了李慕云线。"
    # Continue with the story...
    return

label other_character_route:
    # Add specific events and choices for 其他角色线
    "你选择了其他角色线。"
    # Continue with the story...
    return