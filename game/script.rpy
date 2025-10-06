# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")


# 游戏在此开始。

label start:
    # 初始化游戏状态
    $ start_limuyun_route()
    $ current_week = 1
    
    # 进入李慕云线路
    call week1_limuyun from _call_week1_limuyun
    
    # Week 2
    if current_week == 2:
        call week2_limuyun from _call_week2_limuyun
    
    # Week 3
    if current_week == 3:
        call week3_limuyun from _call_week3_limuyun
    
    # Week 4 结局
    if current_week == 4:
        call week4_ending from _call_week4_ending
    
    # 游戏结束
    return
