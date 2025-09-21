## 测试用基础流程，不含正式剧情。
## 入口：在 start label 里可 call 或 jump 到 test_main 进行验证。

label test_main:
    scene bg room
    show eileen happy
    e "测试流程开始：当前周=[current_week] 日=[current_day] 学科=[subject_skill] 压力=[stress]"

    call test_day_loop

    e "测试流程结束：学科=[subject_skill] 压力=[stress] 学业结果=[evaluate_academic_result()]"
    return

## 单日循环：演示学习->考试->推进日期
label test_day_loop:
    if current_week > 1:
        return

    e "今天是第 [current_week] 周 第 [current_day] 天。请选择学习方式。"
    menu:
        "认真复习 (+3学科 +3压力 100%通过)":
            $ result = study_and_exam(STUDY_SERIOUS)
        "大致浏览 (+2学科? +2压力 50%)":
            $ result = study_and_exam(STUDY_CASUAL)
        "听天由命 (+1学科? +0压力 20%)":
            $ result = study_and_exam(STUDY_LUCK)

    if result["passed"]:
        e "考试通过，获得 [result['gained']] 点学科熟练度。当前=[subject_skill]"
    else:
        e "考试未通过，没有获得学科熟练度。当前=[subject_skill]"

    if stress >= STRESS_BREAKPOINT:
        return

    $ next_day()
    jump test_day_loop
