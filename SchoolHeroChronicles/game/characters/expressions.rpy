# 表情定义文件

# 角色表情和情感状态定义

define e1 = Character("李慕云", color="#c8ffc8")

# 表情状态
image li_muyun_happy = "sprites/li_muyun_happy.png"
image li_muyun_sad = "sprites/li_muyun_sad.png"
image li_muyun_angry = "sprites/li_muyun_angry.png"
image li_muyun_surprised = "sprites/li_muyun_surprised.png"
image li_muyun_neutral = "sprites/li_muyun_neutral.png"

# 表情使用示例
label start:
    e1 "今天真是个好日子！"  # 使用默认表情
    show li_muyun_happy
    e1 "我感到非常开心！"
    
    show li_muyun_sad
    e1 "不过，有些事情让我有点难过。"
    
    show li_muyun_angry
    e1 "我真的很生气！"
    
    show li_muyun_surprised
    e1 "哇！这真让我惊讶！"
    
    show li_muyun_neutral
    e1 "我现在感觉还好。"