"""
web_build_patch.rpy

目的: 规避 GitHub Actions 上构建 web 版本时出现的
TypeError: expected str, bytes or os.PathLike object, not NoneType
追溯显示在 game/web.rpy build_web -> shutil.copy(os.path.join(WEB_PATH, fn), ...)
说明 WEB_PATH 在该阶段为 None。日志中还出现 /build.sh: declare: not found / [[ not found
推测 action 在 /bin/sh 下执行导致上游脚本中使用的 bash 语法分支未正确赋值 WEB_PATH。

策略: 在初始化早期补一个后备赋值，将 WEB_PATH 指向 SDK 内部的 web 模板目录。
若后续 Ren'Py 正常赋值将覆盖此值，不会影响本地运行。
"""

# 负优先级，尽量早于大多数自定义脚本。
init -1500 python:
    import os
    try:
        import renpy  # 引擎上下文
        # 仅当未定义或为 None 时提供后备。
        if 'WEB_PATH' not in globals() or WEB_PATH is None:
            fallback = os.path.join(renpy.config.renpy_base, 'web')
            if os.path.isdir(fallback):
                WEB_PATH = fallback  # 提供给后续 build_web 使用
    except Exception:
        # 安全失败，不中断本地开发
        pass

# 可选：禁用 progressive download（若仍报同类错误可再解开）
# init -1490 python:
#     try:
#         # 不同版本命名可能变化，保持 try 容忍
#         if hasattr(build, 'web_progressive'):
#             build.web_progressive = False
#     except Exception:
#         pass

