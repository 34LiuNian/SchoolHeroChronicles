# 市中英雄传 架构与系统规划（AGENTS Documentation）

本文件描述当前项目的基础数据结构、脚本分层约定、未来扩展点以及协作指引。适用于：

- 新加入的脚本编写者
- 负责数值/剧情/系统扩展的维护者
- 后续接手重构或多语言、本地化与性能优化的成员

---

## 目录

1. 目标与设计哲学
2. 脚本分层结构
3. 全局数据与命名规范
4. 核心系统说明
5. 事件/剧情组织建议
6. UI / 屏幕架构扩展点
7. 音频系统规划
8. 本地化策略
9. 结局与解锁机制
10. 调试与开发模式建议
11. 后续迭代路线建议

---

## 1. 目标与设计哲学

- 最小可运行：先保证可循环（天/周）与数值变化，逐步挂载剧情。
- 数据可追踪：所有可变游戏状态（如属性、好感、天数）使用 `default`，常量使用 `define`。
- 模块清晰：剧情 label 不直接写复杂逻辑，逻辑放入函数或系统文件，剧情只“调用+展示”。
- 易扩展：结局、角色线、事件触发采用条件函数 + 数据驱动，可方便添加新角色或数值。

---

## 2. 脚本分层结构（现状与推荐）

| 层级 | 文件/目录 | 作用 |
|------|-----------|------|
| 基础定义 | `variables.rpy` | 全局数值、常量、系统函数（学习、考试、好感、日期推进、评估） |
| 角色定义 | `characters.rpy` | 全部 `Character()` 定义与角色标签映射 |
| 流程/测试 | `flow_test.rpy` | 测试循环，不含正式剧情 |
| 主入口 | `script.rpy` | `start` 入口，后期仅做启动分派 |
| UI | `screens.rpy`, `gui.rpy` | 现有 Ren'Py 默认 GUI，可扩展 HUD/弹窗 |
| 未来建议 | `time_system.rpy` | 天/周/时间段（早/午/晚）控制（待建） |
| 未来建议 | `affection.rpy` | 好感增减封装、角色事件 hook（待建） |
| 未来建议 | `events_weekX.rpy` | 分周/章节的剧情块 |
| 未来建议 | `endings.rpy` | 结局计算、展示与解锁标记 |
| 未来建议 | `audio.rpy` | 音频播放封装（BGM/SE/环境） |
| 未来建议 | `dev_tools.rpy` | 调试面板/命令 |

---

## 3. 全局数据与命名规范

- 常量：`STAT_` / `STRESS_` / `AFFECTION_` 前缀。
- 可变属性：纯小写+下划线，如：`subject_skill`, `stress`, `current_week`。
- 集合：`unlocked_endings`（`set()`）。
- 角色好感：字典 `affection = {"erin": 0}`；扩展时直接新增 key。
- 函数命名：动宾结构，如 `study_and_exam`, `evaluate_academic_result`, `add_affection`。
- 结局类别返回值：`excellent | good | hard | expelled`。

---

## 4. 核心系统说明

### 学习与考试
`study_and_exam(choice)` 函数：

- 依据 `choice`（`STUDY_SERIOUS` / `STUDY_CASUAL` / `STUDY_LUCK`）计算：
  - 学科熟练度增量
  - 压力增量
  - 随机通过判定（50% / 20%）
- 返回：`{"passed": bool, "gained": int, "choice": str}`

### 压力崩坏

- 阈值：`STRESS_BREAKPOINT = 14`
- 检测：`_check_stress_break()`，若超限调用 `stress_break_end`。

### 学业结果评估

`evaluate_academic_result()`：返回 4 类，用于结局分支与是否允许进入角色线。

### 角色线进入判定

`can_character_route(char_id)`：好感达到阈值且未被开除。

---

## 5. 事件/剧情组织建议

- 推荐一个“日期驱动”调度：在每个时间点调用一个事件收集函数，返回可触发事件/标签列表。
- 事件数据结构建议：

```python
# 伪结构
EVENTS = [
    {"id": "erin_intro", "week": 1, "day": 2, "cond": lambda: affection["erin"] < 2, "label": "event_erin_intro"},
]
```

- 统一一个 `trigger_events()` 函数在每日开始或阶段切换时执行。

---

## 6. UI / 屏幕架构扩展点

建议新增：

- `screen hud_status`：显示：周/日、学科熟练度、压力条（颜色：正常/警戒/危险）、好感按钮。
- `screen study_choice`：替代直接 `menu`，可展示概率说明与结果回放。
- `screen affection_panel`：列出所有角色头像+好感值+状态（是否可进线）。
- 统一状态颜色：
  - 压力 < 8：绿色
  - 8–13：黄色
  - ≥14：红色（闪烁）

---

## 7. 音频系统规划（未来）

- 目录按：`audio/bgm`, `audio/se`, `audio/amb`。
- 封装函数：`play_bgm(name, fade=1.0)`, `stop_bgm(fade=1.0)`, `play_se(name)`。
- 背景音乐切换策略：同曲目重复调用忽略；不同曲目淡出+淡入。

---

## 8. 本地化策略

- 文本逐步用 `_()` 包裹；分语种放入 `tl/<lang>`。
- 对系统消息（如结局描述）集中放入一个 `i18n.rpy` 以便翻译统一管理。
- 避免在逻辑函数中直接写硬编码文本（返回 key，由展示层映射）。

---

## 9. 结局与解锁机制

- 建议在第 3 周末统一调用 `label evaluate_final_endings`：
  1. 学科结果分类
  2. 过滤可进入的角色线（好感达标）
  3. 若被开除 -> 开除结局
  4. 若角色线候选>1：可给玩家选择优先 or 依据最高好感自动决策
  5. 记录：`unlocked_endings.add(ending_id)`
- 可添加结局展示画廊：`screen ending_gallery`。

---

## 10. 调试与开发模式建议

- `dev_tools.rpy`：快捷键（如 Shift+F1）打开调试面板：加/减压力、加好感、跳日/跳周、打印当前数值。
- `debug_log` 列表保留最近 100 条内存日志，必要时写入磁盘（可选）。

---

## 11. 后续迭代路线建议（优先顺序）

1. HUD 与学习选择 screen 替换 menu
2. 时间段（早/午/晚）与事件调度框架
3. 角色事件触发表数据化
4. 第三周结算+结局骨架 + 结局展示
5. 音频封装与基础 BGM
6. 本地化抽取 `_()`
7. 调试面板（加速制作效率）
8. 角色立绘与情感 State 管理（show 表达式）

---

## 常见注意事项

- 不在剧情 label 里直接写复杂 if/概率逻辑，尽量调用函数。
- 修改全局变量需确保用 `global` 或可变结构（dict/list）操作。
- 新增变量请统一放入 `variables.rpy` 顶部区域（或拆出专门系统文件后迁移）。

---
若需引入新系统（如体力/金钱/道具），建议：

1. 先在 `variables.rpy` 定义数据结构 + 常量阈值
2. 写增减/判定函数
3. 添加 HUD 显示
4. 在事件脚本中调用，而不是直接操作底层数值

---
（文档版本：v0.1，可随迭代更新）
