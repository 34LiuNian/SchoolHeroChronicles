# 游戏图片资源规划

## 目录结构

```
game/images/
├── bg/                 # 背景图片
│   ├── classroom.png   # 教室
│   ├── cafeteria.png   # 食堂
│   ├── arcade.png      # 电玩城
│   ├── apartment.png   # 李慕云家外观
│   ├── limuyun_room.png # 李慕云房间
│   └── rainy_street.png # 雨天街道
│
├── characters/         # 角色立绘
│   └── limuyun/
│       ├── happy.png       # 开心
│       ├── sad.png         # 悲伤
│       ├── worried.png     # 担忧
│       ├── tired.png       # 疲惫
│       ├── smile.png       # 微笑
│       └── determined.png  # 坚定
│
├── cg/                 # CG图片（特殊场景）
│   ├── hamburger_fight.png  # 抢汉堡场景
│   ├── arcade_game.png      # 打拳皇场景
│   ├── cookies_baking.png   # 烤饼干场景
│   └── rain_window.png      # 透过窗看雨
│
└── ui/                 # UI元素
    ├── week_banner.png     # 周次标题横幅
    └── ending_title.png    # 结局标题

```

## 图片尺寸建议

- 背景图：1920x1080 (16:9)
- 角色立绘：最高1200px，保持透明背景PNG
- CG：1920x1080 (16:9)

## 当前占位方案

目前使用 Ren'Py 默认图片（eileen）作为占位。
正式开发时，按照以上结构添加图片资源。

## 场景与图片对应关系

### Week 1: 雨天是城市的祭日

- bg classroom - 教室日常场景
- limuyun happy - 李慕云送饼干
- limuyun smile - 谈论食物
- bg cafeteria - 食堂场景
- cg hamburger_fight - 抢汉堡（可选CG）

### Week 2: 拳皇

- bg classroom - 考试后场景
- limuyun worried - 担心的表情
- bg arcade - 电玩城
- cg arcade_game - 打拳皇场景（可选）
- limuyun sad - 发现伤痕后
- bg classroom (雨天版) - 周二下午阴天
- limuyun tired - 疲惫坐在窗前

### Week 3: 家访

- bg apartment - 公寓外观
- bg limuyun_room - 李慕云房间
- limuyun determined - 下定决心
- cg cookies_baking - 烤饼干（可选）

### Week 4: 终局

- bg classroom (雨天) - 空座位
- bg rainy_street (好结局) - 雨中希望
- cg rain_window (坏结局) - 雨窗意象

## 图片定义（在脚本中使用）

```renpy
# 背景图片定义
image bg classroom = "images/bg/classroom.png"
image bg cafeteria = "images/bg/cafeteria.png"
image bg arcade = "images/bg/arcade.png"
image bg apartment = "images/bg/apartment.png"

# 角色立绘定义
image limuyun happy = "images/characters/limuyun/happy.png"
image limuyun sad = "images/characters/limuyun/sad.png"
image limuyun worried = "images/characters/limuyun/worried.png"
image limuyun tired = "images/characters/limuyun/tired.png"
image limuyun smile = "images/characters/limuyun/smile.png"
image limuyun determined = "images/characters/limuyun/determined.png"

# CG定义
image cg hamburger = "images/cg/hamburger_fight.png"
image cg arcade = "images/cg/arcade_game.png"
image cg cookies = "images/cg/cookies_baking.png"
```

## 待实现清单

### 优先级 1（核心必需）

- [ ] bg classroom (教室)
- [ ] limuyun happy/sad/worried (基本表情)
- [ ] bg rainy_street (结局背景)

### 优先级 2（增强体验）

- [ ] bg cafeteria (食堂)
- [ ] bg arcade (电玩城)
- [ ] bg apartment (公寓)
- [ ] limuyun tired/smile/determined

### 优先级 3（锦上添花）

- [ ] 各类CG图片
- [ ] UI装饰元素
- [ ] 周次横幅

## 临时方案

在图片资源未就绪前，可以：

1. 使用纯色背景 + 文字描述
2. 使用 Ren'Py 默认占位图
3. 使用简单的颜色渐变作为场景区分

示例代码：

```renpy
# 临时背景定义
image bg classroom = "#87CEEB"  # 天蓝色代表教室
image bg cafeteria = "#FFD700"  # 金色代表食堂
image bg arcade = "#9370DB"     # 紫色代表电玩城
```
