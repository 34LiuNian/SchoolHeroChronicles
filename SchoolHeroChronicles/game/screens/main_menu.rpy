# main_menu.rpy

label main_menu:
    # Main menu screen
    scene bg main_menu_background
    with dissolve

    # Display the title
    text "School Hero Chronicles" at title_position

    # Start button
    textbutton "开始游戏" action Start()
    
    # Load button
    textbutton "加载游戏" action ShowMenu("load")

    # Options button
    textbutton "选项" action ShowMenu("preferences")

    # Quit button
    textbutton "退出" action Quit()

    # Background music
    play music "bgm/main_menu_theme.ogg" loop

    # Transition effect
    with fade

    # End of main menu label
    return