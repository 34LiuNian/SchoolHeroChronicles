# script.rpy

label start:
    scene bg room
    with dissolve

    "欢迎来到《校园英雄编年史》！"
    "在这个游戏中，你将体验到高三生活的挑战与成长。"

    jump prologue

# Include all week scripts
label prologue:
    call prologue

label week_01:
    call week_01

label week_02:
    call week_02

label week_03:
    call week_03

label week_04:
    call week_04

# End of the game
label end:
    "感谢你的游玩！期待再次相遇！"
    return