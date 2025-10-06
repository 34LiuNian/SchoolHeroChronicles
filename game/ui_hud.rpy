## ========================================
## HUD 状态显示系统
## ========================================

## 游戏内状态栏，显示关键信息
screen hud_status():
    zorder 100
    
    # 只在游戏进行时显示，主菜单不显示
    if not main_menu:
        frame:
            xalign 0.98
            yalign 0.02
            xpadding 15
            ypadding 10
            background Frame("gui/frame.png", 10, 10)
            
            vbox:
                spacing 5
                
                # 周次显示
                text "第 [current_week] 周" size 20 color "#FFFFFF"
                
                # 学科熟练度
                hbox:
                    spacing 5
                    text "学科:" size 18 color "#FFD700"
                    text "[subject_skill]" size 18 color "#FFFFFF"
                
                # 压力值（根据压力值改变颜色）
                hbox:
                    spacing 5
                    text "压力:" size 18 color "#FF6B6B"
                    if stress < 7:
                        text "[stress]" size 18 color "#90EE90"
                    elif stress < 12:
                        text "[stress]" size 18 color "#FFD700"
                    else:
                        text "[stress]" size 18 color "#FF4444"
                
                # 李慕云好感度（如果在她的线路上）
                if current_route == "limuyun":
                    hbox:
                        spacing 5
                        text "慕云:" size 18 color "#FFB6C1"
                        text "[affection['limuyun']]" size 18 color "#FFFFFF"

## 自动显示 HUD
init python:
    config.overlay_screens.append("hud_status")


## ========================================
## 调试工具（开发用）
## ========================================

# 调试面板：按 Shift+D 显示（仅开发模式）
screen debug_panel():
    zorder 200
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 20
        background Frame("gui/frame.png", 10, 10)
        
        vbox:
            spacing 10
            
            text "调试工具" size 30 xalign 0.5
            
            null height 10
            
            textbutton "增加学科熟练度 +3":
                action SetVariable("subject_skill", subject_skill + 3)
            
            textbutton "减少压力 -5":
                action SetVariable("stress", max(0, stress - 5))
            
            textbutton "增加李慕云好感 +2":
                action Function(add_affection, "limuyun", 2)
            
            textbutton "跳到 Week 2":
                action [SetVariable("current_week", 2), Jump("week2_limuyun")]
            
            textbutton "跳到 Week 3":
                action [SetVariable("current_week", 3), Jump("week3_limuyun")]
            
            textbutton "跳到 Week 4":
                action [SetVariable("current_week", 4), Jump("week4_ending")]
            
            null height 20
            
            textbutton "关闭" action Hide("debug_panel")

# 快捷键绑定
init python:
    config.keymap['debug_panel'] = ['shift_K_d']
    config.underlay.append(renpy.Keymap(debug_panel=Show("debug_panel")))
