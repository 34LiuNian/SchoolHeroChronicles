## 基础变量与系统常量（规划阶段骨架）
## 说明：此文件只放与全局游戏进程、数值系统相关的“数据与函数”，不写剧情。

## ------------------------------
## 阈值常量（使用 define：编译期常量，不会进存档差异对比）
define STAT_SUBJECT_EXCELLENT = 15      # 优秀毕业生
define STAT_SUBJECT_GOOD_LOW  = 10      # 顺利毕业下界
define STAT_SUBJECT_PASS_LOW  = 3       # 艰难毕业下界

define STRESS_BREAKPOINT = 14           # 压力崩坏阈值（>= 强制结束）

define AFFECTION_ENDING_THRESHOLD = 6   # 角色线进入阈值

## 学习方式标记（枚举风格）
define STUDY_SERIOUS = "serious"   # 认真复习：+3 学科，+3 压力，100% 通过
define STUDY_CASUAL  = "casual"    # 大致浏览：+2 学科或 +0（未过），+2 压力，50% 通过
define STUDY_LUCK    = "luck"      # 听天由命：+1 学科或 +0（未过），+0 压力，20% 通过

## ------------------------------
## 默认运行期变量（使用 default：可被存档追踪，首次新开局初始化）
default subject_skill = 0           # 学科熟练度（总）
default stress = 0                  # 压力值
default current_week = 1            # 周数（从 1 开始）
default current_day = 1             # 当周日序（自行约定 1~7）
default schedule_phase = "idle"     # 当前阶段：idle / study / exam / free 等

## 角色好感（按代号键值）—— 初期只有占位，后面扩展
default affection = {
    "limuyun": 0,   # 李慕云
}

## 李慕云线关键选择标记
default limuyun_week2_accepted_invitation = False  # Week 2是否接受家访邀请
default limuyun_week3_helped = False               # Week 3是否提供有效帮助
default limuyun_week2_arcade_visited = False       # Week 2是否去了电玩城
default limuyun_noticed_bruises = 0                # 注意到伤痕的次数

## 已解锁的结局标记（集合/列表）
default unlocked_endings = set()

## 测试统计/日志（调试用，可后期移除或加 dev flag）
default debug_log = []

## 当前进行的角色线路
default current_route = None  # None / "limuyun" / 其他## ------------------------------
## 工具函数区域
init python:
    import random

    def _log(msg):
        """内部调试记录。"""
        debug_log.append(msg)
        renpy.log(msg)

    def study_and_exam(choice):
        """执行一次学习 + 考试流程。
        choice: STUDY_SERIOUS / STUDY_CASUAL / STUDY_LUCK
        返回字典 {passed: bool, gained: int, choice: str}
        """
        global stress, subject_skill, schedule_phase
        schedule_phase = "exam"

        if choice == STUDY_SERIOUS:
            stress += 3
            passed = True
            gain = 3
        elif choice == STUDY_CASUAL:
            stress += 2
            passed = random.random() < 0.5
            gain = 2 if passed else 0
        elif choice == STUDY_LUCK:
            # 无压力增加
            passed = random.random() < 0.2
            gain = 1 if passed else 0
        else:
            raise Exception("未知学习方式: " + str(choice))

        subject_skill += gain
        _log(f"[DAY {current_week}-{current_day}] choice={choice} passed={passed} +{gain} skill, stress={stress}")
        _check_stress_break()
        return {"passed": passed, "gained": gain, "choice": choice}

    def add_affection(char_id, value):
        global affection
        if char_id not in affection:
            affection[char_id] = 0
        affection[char_id] += value
        _log(f"affection[{char_id}] -> {affection[char_id]}")

    def next_day():
        """推进日期。到达 7 结束则进入下一周。"""
        global current_day, current_week, schedule_phase
        current_day += 1
        schedule_phase = "idle"
        if current_day > 7:
            current_day = 1
            current_week += 1
        _log(f"Advance to week {current_week} day {current_day}")

    def _check_stress_break():
        if stress >= STRESS_BREAKPOINT:
            renpy.call_in_new_context("stress_break_end")

    def evaluate_academic_result():
        """根据 subject_skill 返回学科结果类别字符串。"""
        s = subject_skill
        if s >= STAT_SUBJECT_EXCELLENT:
            return "excellent"
        elif s >= STAT_SUBJECT_GOOD_LOW:
            return "good"
        elif s >= STAT_SUBJECT_PASS_LOW:
            return "hard"
        else:
            return "expelled"

    def can_character_route(char_id):
        return affection.get(char_id, 0) >= AFFECTION_ENDING_THRESHOLD and evaluate_academic_result() != "expelled"
    
    def get_week_label():
        """返回当前周对应的剧情入口 label 名称。"""
        if current_week == 1:
            return "week1_limuyun"
        elif current_week == 2:
            return "week2_limuyun"
        elif current_week == 3:
            return "week3_limuyun"
        elif current_week == 4:
            return "week4_ending"
        else:
            return None
    
    def start_limuyun_route():
        """开始李慕云线路。"""
        global current_route
        current_route = "limuyun"
        _log("Started Li Muyun route")

## ------------------------------
## 结局 / 强制结束 label（测试用占位）
label stress_break_end:
    scene black with fade
    centered "压力过高导致崩坏，测试流程结束 (stress = [stress])" with dissolve
    return

