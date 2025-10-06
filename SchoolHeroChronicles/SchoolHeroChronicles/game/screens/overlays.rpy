# This file defines the overlay screens for the game, such as message boxes and notifications.

screen overlay_message(message, title="提示"):
    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text title:
            style "overlay_title"

        text message:
            style "overlay_message"

        textbutton "确定":
            action Hide("overlay_message")