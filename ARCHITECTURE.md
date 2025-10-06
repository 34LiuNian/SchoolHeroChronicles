# 《市中英雄传》游戏架构文档

## 项目概述

这是一个基于 Ren'Py 引擎的视觉小说游戏，讲述高三学生与同学李慕云之间的故事。游戏通过选择影响剧情走向，最终导向不同的结局。

## 核心玩法系统

### 数值系统

1. **学科熟练度** (subject_skill)
   - 通过学习与考试获得
   - 影响毕业结局评级
   - 阈值：15(优秀) / 10(良好) / 3(及格)

2. **压力值** (stress)
   - 学习行为增加压力
   - ≥14 触发崩坏结局
   - 需要平衡学习强度

3. **好感度** (affection)
   - 通过对话选择影响
   - ≥6 进入角色线路
   - 决定角色结局

### 周次结构

游戏分为 4 周，每周推进剧情：

- Week 1: 雨天是城市的祭日（建立关系）
- Week 2: 拳皇（关键选择点）
- Week 3: 家访（帮助or放弃）
- Week 4: 终局（好/坏结局分支）

## 文件结构

```
game/
├── script.rpy              # 主入口脚本
├── variables.rpy           # 全局变量与系统函数
├── characters.rpy          # 角色定义
├── limuyun_route.rpy       # 李慕云线路完整剧情
├── ui_hud.rpy             # HUD状态显示与调试工具
├── audio_system.rpy        # 音频系统封装
├── flow_test.rpy          # 测试流程（已弃用）
│
├── gui.rpy                # GUI配置（Ren'Py生成）
├── options.rpy            # 游戏设置（Ren'Py生成）
├── screens.rpy            # UI屏幕定义（Ren'Py生成）
│
├── images/                # 图片资源目录（待添加）
├── audio/                 # 音频资源目录（待添加）
└── tl/                    # 翻译文件目录
```

## 核心系统说明

### 1. 变量系统 (variables.rpy)

**全局常量：**

```python
STAT_SUBJECT_EXCELLENT = 15      # 优秀毕业阈值
STRESS_BREAKPOINT = 14           # 压力崩坏阈值
AFFECTION_ENDING_THRESHOLD = 6   # 角色线阈值
```

**运行时变量：**

```python
subject_skill = 0                # 学科熟练度
stress = 0                       # 压力值
current_week = 1                 # 当前周数
affection = {"limuyun": 0}       # 角色好感度字典
limuyun_week2_accepted_invitation # Week2关键选择
limuyun_week3_helped             # Week3是否帮助
```

**核心函数：**

- `add_affection(char_id, value)` - 增加好感度
- `start_limuyun_route()` - 开始李慕云线路
- `study_and_exam(choice)` - 学习考试系统（备用）

### 2. 角色系统 (characters.rpy)

```python
define lmy = Character("李慕云", color="#FFB6C1")
define me = Character("我", color="#87CEEB")
define teacher = Character("班主任")
define lmy_mom = Character("李慕云妈妈")
```

### 3. 剧情系统 (limuyun_route.rpy)

**关键Label：**

- `week1_limuyun` - Week 1 完整剧情
- `week2_limuyun` - Week 2 + 关键选择
- `week3_limuyun` - Week 3 家访（条件触发）
- `week4_ending` - 结局分支
- `limuyun_good_ending` - 好结局
- `limuyun_bad_ending` - 坏结局

**分支逻辑：**

```
Week 2 邀请选择：
├─ 接受邀请 → Week 3 家访
│   ├─ 提供帮助 → 好结局（母女获救）
│   └─ 未提供帮助 → 坏结局
└─ 拒绝邀请 → 跳过Week 3 → 坏结局（悲剧）
```

### 4. UI系统 (ui_hud.rpy)

**HUD状态栏：**

- 实时显示周次、学科、压力、好感度
- 压力值颜色分级提示
- 自动叠加显示（zorder 100）

**调试面板：**

- 按 `Shift+D` 打开
- 可调整数值、跳转章节
- 仅用于开发测试

### 5. 音频系统 (audio_system.rpy)

**封装函数：**

- `play_bgm(track, fadein, fadeout)` - 播放BGM
- `stop_bgm(fadeout)` - 停止BGM
- `play_sfx(sfx)` - 播放音效
- `play_ambient(ambient, volume)` - 播放环境音

**音频分类：**

- BGM: 背景音乐（循环）
- SFX: 音效（单次）
- Ambient: 环境音（循环，独立通道）

## 运行流程

```
启动游戏
  ↓
script.rpy: label start
  ↓
初始化（start_limuyun_route）
  ↓
Week 1 → Week 2 → Week 3 → Week 4
  ↓                 ↓
选择分支      条件触发
  ↓                 ↓
好结局 / 坏结局
  ↓
return (游戏结束)
```

## 开发指南

### 添加新角色线路

1. 在 `variables.rpy` 添加好感度键值
2. 在 `characters.rpy` 定义角色
3. 创建新的 `xxx_route.rpy` 文件
4. 在 `script.rpy` 添加路线选择逻辑
5. 在 HUD 中添加显示支持

### 添加新场景

1. 在对应的 `xxx_route.rpy` 中创建 `label`
2. 使用 `scene bg xxx` 切换背景
3. 使用 `show character expression` 显示角色
4. 使用 `menu` 创建选择分支
5. 通过 `$ variable = value` 修改变量

### 测试流程

1. 运行游戏，按 `Shift+D` 打开调试面板
2. 跳转到指定周次测试
3. 调整变量观察分支效果
4. 使用 HUD 监控实时数值

## 待完善内容

### 高优先级

- [ ] 添加背景图片资源
- [ ] 添加角色立绘
- [ ] 添加核心BGM音乐
- [ ] 完善存档/读档测试

### 中优先级

- [ ] 添加CG特殊场景图
- [ ] 添加音效和环境音
- [ ] 优化对话框样式
- [ ] 添加更多角色线路

### 低优先级

- [ ] 成就系统
- [ ] 回想模式
- [ ] 多语言支持
- [ ] 额外剧情分支

## 技术规范

### 代码风格

- 使用 4 空格缩进（不使用Tab）
- Label命名：小写+下划线
- 变量命名：小写+下划线
- 常量命名：大写+下划线

### 注释规范

```python
## 大段注释使用双井号
# 单行注释使用单井号

"""
多行文档字符串
用于函数说明
"""
```

### 文件编码

- 所有脚本文件使用 UTF-8 编码
- 支持中文字符
- 使用 `SourceHanSansLite.ttf` 作为中文字体

## 常见问题

**Q: 如何重新开始游戏？**
A: 主菜单 → 开始游戏，或删除存档文件夹

**Q: 如何跳过已读文本？**
A: 按住 Ctrl 键或点击快进按钮

**Q: 调试面板快捷键不生效？**
A: 确保是英文输入法，按 Shift+D（大写D）

**Q: 如何查看当前变量值？**
A: 右上角HUD显示，或使用调试面板

## 版本历史

### v0.1.0 - 基础架构搭建

- 建立核心变量系统
- 实现李慕云线路完整剧情
- 添加HUD状态显示
- 创建音频系统封装
- 完成好/坏结局分支

---

**项目状态：** 架构完成，等待资源补充
**最后更新：** 2025年10月6日
