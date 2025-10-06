# This file contains the graphical user interface settings for the game, including menus, buttons, and other interface elements.

# Define the main menu style
define gui.main_menu_background = "images/backgrounds/main_menu.jpg"
define gui.main_menu_button = "images/buttons/main_menu_button.png"
define gui.main_menu_button_hover = "images/buttons/main_menu_button_hover.png"

# Define the text styles
define gui.text_style = TextStyle(
    size=30,
    color="#FFFFFF",
    font="fonts/YourFont.ttf"
)

# Define the button styles
define gui.button_style = ButtonStyle(
    text_style=gui.text_style,
    background=gui.main_menu_button,
    hover_background=gui.main_menu_button_hover,
    padding=(10, 5)
)

# Define the main menu screen
screen main_menu():
    tag menu
    add gui.main_menu_background
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        textbutton "开始游戏" action Start()
        textbutton "加载游戏" action ShowMenu("load")
        textbutton "设置" action ShowMenu("preferences")
        textbutton "退出" action Quit()

# Define other GUI elements as needed
# ...