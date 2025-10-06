## ========================================
## 音频系统规划与封装
## ========================================

## BGM（背景音乐）命名规范：
## - main_menu.ogg/mp3     主菜单音乐
## - daily_life.ogg        日常校园场景
## - tension.ogg           紧张/冲突场景
## - sadness.ogg           悲伤场景
## - hope.ogg              希望/温暖场景
## - arcade.ogg            电玩城场景
## - rain.ogg              雨天氛围
## - ending_good.ogg       好结局
## - ending_bad.ogg        坏结局

## 音效（SFX）命名规范：
## - notification.ogg      通知/消息提示
## - page_turn.ogg         翻页音效
## - button_click.ogg      按钮点击
## - thunder.ogg           雷声
## - door_knock.ogg        敲门声
## - phone_vibrate.ogg     手机震动

## 环境音（Ambient）命名规范：
## - rain_light.ogg        小雨声
## - rain_heavy.ogg        大雨声
## - classroom_chatter.ogg 教室喧闹
## - cafeteria_crowd.ogg   食堂人群声
## - arcade_ambience.ogg   电玩城环境音

## ========================================
## 音频控制函数
## ========================================

init python:
    def play_bgm(track_name, fadein=1.0, fadeout=1.0):
        """播放背景音乐，带淡入淡出效果。
        
        Args:
            track_name: 音乐文件名（不含路径）
            fadein: 淡入时间（秒）
            fadeout: 淡出时间（秒）
        """
        track_path = "audio/" + track_name
        if fadeout > 0:
            renpy.music.play(track_path, channel="music", fadein=fadein, fadeout=fadeout, loop=True)
        else:
            renpy.music.play(track_path, channel="music", fadein=fadein, loop=True)
        _log(f"Playing BGM: {track_name}")
    
    def stop_bgm(fadeout=1.0):
        """停止背景音乐。"""
        renpy.music.stop(channel="music", fadeout=fadeout)
        _log("Stopped BGM")
    
    def play_sfx(sfx_name, volume=1.0):
        """播放音效。
        
        Args:
            sfx_name: 音效文件名
            volume: 音量（0.0-1.0）
        """
        sfx_path = "audio/" + sfx_name
        renpy.sound.play(sfx_path, channel="sound")
        _log(f"Playing SFX: {sfx_name}")
    
    def play_ambient(ambient_name, volume=0.5, fadein=2.0):
        """播放环境音。
        
        Args:
            ambient_name: 环境音文件名
            volume: 音量（0.0-1.0）
            fadein: 淡入时间（秒）
        """
        ambient_path = "audio/" + ambient_name
        renpy.sound.play(ambient_path, channel="ambient", fadein=fadein, loop=True)
        renpy.sound.set_volume(volume, channel="ambient")
        _log(f"Playing Ambient: {ambient_name}")
    
    def stop_ambient(fadeout=2.0):
        """停止环境音。"""
        renpy.sound.stop(channel="ambient", fadeout=fadeout)
        _log("Stopped Ambient")

## ========================================
## 音频通道配置
## ========================================

init python:
    # 注册额外的音频通道
    renpy.music.register_channel("ambient", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True)

## ========================================
## 音频占位符（实际使用时替换为真实音频文件）
## ========================================

## 目前使用 Ren'Py 默认音频作为占位
## 实际开发时，将音频文件放入 game/audio/ 目录

# 示例：定义音频别名（可选）
# define audio.main_theme = "audio/main_menu.ogg"
# define audio.rain_sound = "audio/rain_light.ogg"

## ========================================
## 场景音频触发示例
## ========================================

## 在剧情脚本中使用示例：
## 
## # 播放日常BGM
## $ play_bgm("daily_life.ogg", fadein=2.0)
##
## # 播放雨声环境音
## $ play_ambient("rain_light.ogg", volume=0.4)
##
## # 播放音效
## $ play_sfx("phone_vibrate.ogg")
##
## # 停止BGM
## $ stop_bgm(fadeout=3.0)
##
## # 停止环境音
## $ stop_ambient()

## ========================================
## 待办：音频资源需求清单
## ========================================

## 优先级 1（核心场景）：
## - daily_life.ogg          日常校园BGM
## - tension.ogg             紧张场景BGM
## - rain_light.ogg          小雨环境音
## - ending_good.ogg         好结局BGM
## - ending_bad.ogg          坏结局BGM

## 优先级 2（增强体验）：
## - arcade.ogg              电玩城BGM
## - hope.ogg                温暖场景BGM
## - sadness.ogg             悲伤场景BGM
## - phone_vibrate.ogg       手机震动音效
## - thunder.ogg             雷声音效

## 优先级 3（细节打磨）：
## - classroom_chatter.ogg   教室环境音
## - cafeteria_crowd.ogg     食堂环境音
## - arcade_ambience.ogg     电玩城环境音
## - door_knock.ogg          敲门音效
## - button_click.ogg        UI音效
