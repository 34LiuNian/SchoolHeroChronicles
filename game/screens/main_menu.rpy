screen main_menu():
    tag menu
    add "gui/main_menu.png"

    frame:
        style "main_menu_frame"

    use navigation

    if gui.show_name:
        vbox:
            style "main_menu_vbox"
            text "School Hero Chronicles" at title_position
            text "[config.version]":
                style "main_menu_version"

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton "开始游戏" action Start()
        else:
            textbutton "历史" action ShowMenu("history")
            textbutton "保存" action ShowMenu("save")

        textbutton "加载游戏" action ShowMenu("load")
        textbutton "设置" action ShowMenu("preferences")

        if _in_replay:
            textbutton "结束回放" action EndReplay(confirm=True)
        elif not main_menu:
            textbutton "标题菜单" action MainMenu()

        textbutton "关于" action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton "帮助" action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton "退出" action Quit(confirm=not main_menu)
