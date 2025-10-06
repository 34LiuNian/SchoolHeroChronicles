# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")


# 游戏在此开始。

label start:
    # 初始化游戏状态
    $ start_limuyun_route()
    $ current_week = 1
    
    # 进入李慕云线路
    call week1_limuyun
    
    # Week 2
    if current_week == 2:
        call week2_limuyun
    
    # Week 3
    if current_week == 3:
        call week3_limuyun
    
    # Week 4 结局
    if current_week == 4:
        call week4_ending
    
    # 游戏结束
    return

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "占位开场：进入测试循环。"
    call test_main
    e "返回主 start label，测试完成。"
    return
