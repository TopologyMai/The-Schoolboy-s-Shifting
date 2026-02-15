################################################################################
## 初始化
################################################################################

init offset = -1


################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内屏幕
################################################################################


## 对话屏幕 ########################################################################
##
## 对话屏幕用于向用户显示对话。它需要两个参数，who 和 what，分别是叙述角色的名字
## 和所叙述的文本。（如果没有名字，参数 who 可以是 None。）
##
## 此屏幕必须创建一个 id 为 what 的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为 who 和 id 为 window 的可视控件来应用样式属性。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#say

screen say(who, what):
    # 对话框底
    $ ui_img_path, ui_alpha = get_ui_data()
    window:
        id "window"
        background "images/gui/chatbox/chatbox.png"
        xalign 0.5
        xsize 1792  
        ypos 1000

        # --- UI 动态底图逻辑 ---
        if ui_img_path:
            add ui_img_path:
                pos (40, 40)
                alpha ui_alpha

        # 文字层
        text what id "what":
            # font "fusion-pixel.ttf"
            # 整体居中
            xcenter 0.5
            # 设置固定宽度
            xsize 900 
            # 文本左对齐
            text_align 0.0  # 文本内容左对齐

    # 头像系统
    if who is not None:
        # style "namebox"
        if who == "高超":
            fixed:
                xpos 1580
                ypos 750
                xsize 100 
                ysize 100 
        
                # 头像框在最底层
                add "images/gui/chatbox/avator_box.png":
                    xalign 0.5
                    yalign 0.5

                if gc_face == "wuyu":
                    add "images/gui/face/gaochao_wuyu.png":
                        xalign 0.5
                        yalign 0.5
                        zoom 0.7 
                elif gc_face == "smile":
                    add "images/gui/face/gaochao_smile.png":
                        xalign 0.5
                        yalign 0.5
                        zoom 0.7 
                elif gc_face == "fear":
                    add "images/gui/face/gaochao_fear.png":
                        xalign 0.5
                        yalign 0.5
                        zoom 0.7 
                else:
                    add "images/gui/chatbox/gaochao.png":
                        xalign 0.5
                        yalign 0.5
                        zoom 0.7 

                # 名牌
                add "images/gui/chatbox/gaochao_nametag.png":
                    xalign 0.5
                    ypos 200  

        elif who == "高越":
            fixed:
                xpos 250
                ypos 750
                xsize 100  
                ysize 100  
        
                # 头像框在最底层
                add "images/gui/chatbox/avator_box.png":
                    xalign 0.5
                    yalign 0.5

                if gy_face == "smile":
                    add "images/gui/face/gaoyue_smile.png":
                        xalign 0.5
                        yalign 0.5
                        zoom 0.7  
                elif gy_face == "surprise":
                    add "images/gui/face/gaoyue_surprise.png":
                        xalign 0.5
                        yalign 0.5
                        zoom 0.7 
                elif gy_face == "xinxu":
                    add "images/gui/face/gaoyue_xinxu.png":
                        xalign 0.5
                        yalign 0.5
                        zoom 0.7 
                else:
                    add "images/gui/chatbox/gaoyue.png":
                        xalign 0.5
                        yalign 0.5
                        zoom 0.7 

                # 名牌
                add "images/gui/chatbox/gaoyue_nametag.png":
                    xalign 0.5
                    ypos 200
        else:
            # 其他角色 - 统一空名字牌在左上角
            fixed:
                pos(-800,200)
                
                # 空名字牌背景
                add "images/gui/chatbox/empty_nametag.png":
                    xalign 0.5
                    yalign 0.5
                
                # 角色名字文字
                text who:  # 直接显示角色名
                    font "fusion-pixel.ttf"
                    size 24
                    color "#FFFFFF"
                    kerning 5
                    xalign 0.5
                    yalign 0.5
                   


    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。prompt 参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为 input 的输入可视控件来接受各种输入参数。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由 menu 语句生成的游戏内选项。参数 items 是一个对象列表，每个对
## 象都有字幕和动作字段。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption:
                action i.action
                style "choice_button_custom"

# 自定义选择按钮样式
style choice_button_custom is default
style choice_button_custom:
    # 按钮大小
    xsize 718
    ysize 88
    xalign 0.5  # 按钮本身居中
    
    # 背景图片
    background "images/gui/button/choice.png"
    hover_background "images/gui/button/choice.png"  # 建议准备一个悬停状态的图片
    selected_background "images/gui/button/choice.png"  # 选中状态
    
    # 内边距 - 根据你的图片调整
    padding (50, 40, 50, 20)  # 左、上、右、下
    
    # 鼠标悬停效果
    hover_sound "audio/se/hover.ogg"  # 可选
    activate_sound "audio/se/click.ogg"  # 可选

# 自定义选择按钮文字样式
style choice_button_custom_text:
    # 文字居中
    xalign 0.5
    yalign 0.5
    kerning 3
    
    # 文字样式
    font "fusion-pixel.ttf"
    size 32
    color "000000"
    
    # 悬停时文字颜色变化
    hover_color "#607D8B"  # 金色
    selected_color "#FFD700"


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing 70

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他屏幕之上，
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("回退") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')


## 此代码确保只要用户没有主动隐藏界面，就会在游戏中显示 quick_menu 屏幕。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 0.96

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    size 30
    idle_color "#000000"  # 平时黑色
    hover_color "#ffffff"  # 悬停白色
    selected_color "#FFD700"  # 选中金色


################################################################################
## 标题和游戏菜单屏幕
################################################################################

## 导航屏幕 ########################################################################
##
## 该屏幕包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    if main_menu and renpy.get_screen("main_menu"):
        
        # 开始游戏
        imagebutton:
            pos (480, 750) 
            idle "images/gui/button/start_idle.png"
            hover im.MatrixColor("images/gui/button/start_idle.png", im.matrix.brightness(0.5))
            action Start()
            
        # 继续游戏
        imagebutton:
            pos (740, 750) 
            idle "images/gui/button/load_idle.png"
            hover im.MatrixColor("images/gui/button/load_idle.png", im.matrix.brightness(0.5))
            action ShowMenu("load")
                
        # 关于
        imagebutton:
            pos (1000, 750) 
            idle "images/gui/button/about_idle.png"
            hover im.MatrixColor("images/gui/button/about_idle.png", im.matrix.brightness(0.5))
            action ShowMenu("about")

        # 结局收集
        imagebutton:
            pos (1260, 750) 
            idle "images/gui/button/ending_idle.png"
            hover im.MatrixColor("images/gui/button/ending_idle.png", im.matrix.brightness(0.5))
            action ShowMenu("ending_gallery")

    else:
        ## --- 游戏内菜单（完全保留原样，不影响内部布局） ---
        textbutton _("历史") action ShowMenu("history")
        textbutton _("保存") action ShowMenu("save")
        textbutton _("读取游戏") action ShowMenu("load")
        textbutton _("设置") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("结束回放") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("标题菜单") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("退出") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#main-menu

screen main_menu():

    # 此语句可确保替换掉任何其他菜单屏幕。
    tag menu

    if persistent.ending_A or persistent.ending_B or persistent.ending_C or persistent.ending_D or persistent.true_ending_unlocked :
        # 1. 先加底图
        add "images/gui/main_menu2.jpg" 
        # 2. 再叠加标题
        add "images/gui/title.png":
            ypos -70
    
    else:
        # 一周目：使用原本的那张完整大图
        add gui.main_menu_background

    # === 关键：播放菜单音乐 ===
    on "show" action Play("music", "audio/bgm/cover.ogg", loop=True, fadein=3.0)

    ## 此空框可使标题菜单变暗。
    #frame:
    #    style "main_menu_frame"

    ## use 语句将其他的屏幕包含进此屏幕。标题屏幕的实际内容在导航屏幕中。
    use navigation

    #if gui.show_name:

    #    vbox:
    #       style "main_menu_vbox"

    #        text "[config.name!t]":
    #            style "main_menu_title"

    #       text "[config.version]":
    #            style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单屏幕 ######################################################################
##
## 此屏幕列出了游戏菜单的基本共同结构。可使用屏幕标题调用，并显示背景、标题和导
## 航菜单。
##
## scroll 参数可以是 None，也可以是 viewport 或 vpgrid。此屏幕旨在与一个或多个子
## 屏幕同时使用，这些子屏幕将被嵌入（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background None

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## 关于屏幕 ########################################################################
##
## 此屏幕提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此屏幕没有什么特别之处，因此它也可以作为一个例子来说明如何制作一个自定义屏
## 幕。

# 初始化当前页码
default about_page = 1

screen about():
    tag menu
    
    # 1. 背景层
    add "images/gui/main_menu_nofont.jpg"
    add Solid("#000000aa") 

    # 2. 内容判定区域
    if about_page == 1:
        # --- 第一页：原作信息 ---
        vbox:
            align (0.5, 0.35)
            spacing 80
            
            null height 20
            text "原作：双高胎" xalign 0.5 size 50 color "#FFFFFF" font "fusion-pixel.ttf"
            text "CP：高超 x 高越" xalign 0.5 size 50 color "#FFFFFF" font "fusion-pixel.ttf"
            text "本作品为同人作品，请勿私自上传线上平台。" xalign 0.5 ypos 100 size 30 color "#FFFFFF" font "fusion-pixel.ttf"

    elif about_page == 2:
        # --- 第二页：核心 STAFF ---
        vbox:
            align (0.5, 0.45)
            spacing 12
            label "STAFF" xalign 0.5:
                text_color "#FFF8DC"
                text_size 50
                text_font "fusion-pixel.ttf"

            null height 10
            text "策划 / 文案 / 数值 / 开发：莓果麦片" xalign 0.5 text_align 0.5 color "#FFFFFF" font "fusion-pixel.ttf"
            text "美术：追追发卡" xalign 0.5 text_align 0.5 color "#FFFFFF" font "fusion-pixel.ttf"
            text "BGM & 音效：隔夜茶" xalign 0.5 text_align 0.5 color "#FFFFFF" font "fusion-pixel.ttf"
            text "测试：隔夜茶 楼梯间 沐 茉莉 丽" xalign 0.5 text_align 0.5 color "#FFFFFF" font "fusion-pixel.ttf"
            text "鸣谢：南山 今天不熬夜" xalign 0.5 text_align 0.5 color "#FFFFFF" font "fusion-pixel.ttf"
            null height 30
            text "感谢游玩！任何感想、repo，请 @游泳池见闻。" xalign 0.5 size 28 color "#FFFFFF" font "fusion-pixel.ttf"
            text "（不放匿名提问箱因为怕挨骂，哈哈。）" xalign 0.5 size 25 italic True color "#B0B0B0" font "fusion-pixel.ttf"


    elif about_page == 3:
        # --- 第三页：素材信息 ---
        vbox:
            align (0.5, 0.4)
            spacing 15
            label "素材来源" xalign 0.5:
                text_color "#FFF8DC"
                text_size 50
                text_font "fusion-pixel.ttf"

            text "美术素材：Unsplash" xalign 0.5 color "#FFFFFF" font "fusion-pixel.ttf"
            text "音乐音效：\nfreesound.org\near0.com\nincompetech.com" xalign 0.5 text_align 0.5 color "#FFFFFF" font "fusion-pixel.ttf"
            text "部分音乐素材：\nFarizki - Fallen Down (Slowed)\nBeethoven - Sonata No. 8 in C Minor, Op. 13\nJune de Toth - Three Burlesques, Op. 8c： Quarrel\nRavel - Miroirs, M.43：3. Une barque sur l'océan" xalign 0.5 text_align 0.5 color "#FFFFFF" font "fusion-pixel.ttf"
    # 3. 翻页控制按钮
    hbox:
        align (0.5, 0.15)
        spacing 800
        
        if about_page > 1:
            textbutton "← 上一页":
                text_font "fusion-pixel.ttf"
                text_size 30
                text_color "#FFFFFF"
                action SetVariable("about_page", about_page - 1)
        else:
            null width 110
            
        if about_page < 3:
            textbutton "下一页 →":
                text_font "fusion-pixel.ttf"
                text_size 30
                text_color "#FFFFFF"
                action SetVariable("about_page", about_page + 1)
        else:
            null width 110

    # 4. 返回按钮 (重置页码并关闭)
    textbutton _("返回"):
        style "return_button"
        align (0.95, 0.92)
        action [SetVariable("about_page", 1), Return()]

# 确保返回按钮样式正确
style return_button_text:
    font "fusion-pixel.ttf"
    size 35
    idle_color "#FFFFFF"  # 平时是白色
    hover_color "#607D8B" # 鼠标放上去变金色

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存屏幕 #####################################################################
##
## 这些屏幕负责让用户保存游戏并能够再次读取。由于它们几乎完全一样，因此这两个屏
## 幕都是以第三个屏幕 file_slots 来实现的。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#save https://doc.renpy.cn/zh-
## CN/screen_special.html#load

screen save():
    tag menu

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    add "images/gui/main_menu_nofont.jpg"
    add Solid("#000000aa")

    fixed:
        ## 返回按钮 - 固定位置
        textbutton _("返回"):
            style "return_button"
            align (0.95, 0.92)
            action Return()

        ## 返回开始页 - 固定位置
        textbutton _("开始页"):
            align (0.05, 0.92)
            style "return_button"
            action MainMenu()
        
        ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
        order_reverse True

        ## 页面名称...
        button:
            style "page_label"
            key_events True
            xalign 0.5
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## 存档位网格...
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"
            xalign 0.5
            yalign 0.5
            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):
                $ slot = i + 1
                button:
                    action FileAction(slot)
                    has vbox
                    add FileScreenshot(slot) xalign 0.5
                    text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                        style "slot_time_text"
                    text FileSaveName(slot):
                        style "slot_name_text"
                    key "save_delete" action FileDelete(slot)

        ## 用于访问其他页面的按钮...
        vbox:
            style_prefix "page"
            xalign 0.5
            yalign 1.0
            hbox:
                xalign 0.5
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                key "save_page_prev" action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()
                key "save_page_next" action FilePageNext()


screen load():

    tag menu

    use file_slots(_("读取游戏"))

    textbutton _("返回"):
        style "return_button"
        align (0.95, 0.92)
        action Return()


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    # 自定义背景
    add "images/gui/main_menu_nofont.jpg"
    add Solid("#000000aa")

    fixed:

        ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
        order_reverse True

        ## 页面名称，可以通过单击按钮进行编辑。
        button:
            style "page_label"

            key_events True
            xalign 0.5
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## 存档位网格。
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## 用于访问其他页面的按钮。
        vbox:
            style_prefix "page"

            xalign 0.5
            yalign 1.0

            hbox:
                xalign 0.5

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()
                key "save_page_prev" action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) 给出 1 到 9 之间的数字。
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
                key "save_page_next" action FilePageNext()

            if config.has_sync:
                if CurrentScreenName() == "save":
                    textbutton _("上传同步"):
                        action UploadSync()
                        xalign 0.5
                else:
                    textbutton _("下载同步"):
                        action DownloadSync()
                        xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## 设置屏幕 ########################################################################
##
## 设置屏幕允许用户配置游戏，使其更适合自己。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#preferences

screen preferences():
    tag menu

    # 背景：使用游戏主菜单的底图 + 半透明遮罩
    add "images/gui/main_menu_nofont.jpg"
    add Solid("#000000aa")

    fixed:
        ## 返回按钮 - 固定位置
        textbutton _("返回"):
            style "return_button"
            align (0.95, 0.92)
            action Return()

        ## 返回开始页 - 固定位置
        textbutton _("开始页"):
            align (0.05, 0.92)
            style "return_button"
            action MainMenu()

    # 标题：设置
    label "设置":
        xalign 0.5
        ypos 50
        text_color "#FFF8DC"
        text_size 50
        text_font "fusion-pixel.ttf"

    # 设置选项区域 - 居中，没有滚动条
    frame:
        xalign 0.5 
        ypos 120   
        xsize 1600 
        background None 
        
        # 直接放置vbox，不要viewport
        vbox:
            spacing 30  # 选项组之间的间距
            
            # 第一行：显示模式和快进选项
            hbox:
                box_wrap True
                spacing 50  # 两个vbox之间的水平间距
                
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        xpos 50
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")
                
                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续") action Preference("after choices", "toggle")
                    textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))
            
            # 间距
            null height (2 * gui.pref_spacing)
            
            # 第二行：音量设置
            hbox:
                style_prefix "slider"
                box_wrap True
                spacing 100
                
                # 文字速度设置
                vbox:
                    xpos 50
                    label _("文字速度")
                    bar value Preference("text speed")
                    label _("自动前进时间")
                    bar value Preference("auto-forward time")
                
                # 音量设置
                vbox:
                    xpos 150
                    if config.has_music:
                        label _("音乐音量")
                        hbox:
                            bar value Preference("music volume")
                    
                    if config.has_sound:
                        label _("音效音量")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)
                                      
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## 历史屏幕 ########################################################################
##
## 这是一个向用户显示对话历史的屏幕。虽然此屏幕没有什么特别之处，但它必须访问储
## 存在 _history_list 中的对话历史记录。
##
## https://doc.renpy.cn/zh-CN/history.html

screen history():
    tag menu
    
    # 背景：和about保持一致
    #add "images/gui/main_menu_nofont.jpg"
    #add Solid("#000000cc")
    # 背景：深蓝灰色纯色
    add Solid("#2c3e50")
    
    # 标题：历史
    label "历史":
        xalign 0.5
        ypos 50
        text_color "#FFF8DC"
        text_size 50
        text_font "fusion-pixel.ttf"
    
    # 返回按钮 - 右下角（和about一致）
    textbutton _("返回"):
        style "return_button"
        align (0.95, 0.92)
        action Return()
    
    # 返回开始页 - 左下角
    textbutton _("返回开始页"):
        align (0.05, 0.92)
        style "return_button"
        action MainMenu()
    
    # 历史内容区域
    frame:
        background None
        xpos 750
        ypos 120
        xsize 950
        ysize 500
        
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            ysize 750
            
            vbox:
                xsize 850
                spacing 25
                
                # 遍历历史记录
                for h in _history_list:
                    frame:
                        background None
                        xfill True
                        
                        vbox:
                            spacing 8
                            xfill True
                            
                            # 说话人
                            if h.who:
                                $ who_color = h.who_args.get("color", "#E0E0E0")
                                text h.who:
                                    size 38
                                    color who_color
                            
                            # 对话/旁白内容
                            $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                            text what:
                                font "AlibabaPuHuiTi-2-75-SemiBold.ttf"
                                size 30
                                color "#FFFFFF"
                                line_spacing 8
                                outlines [ (1, "#000000", 0, 0) ]
                                text_align 0.0
                                layout "tex"
                
                # 空状态
                if not _history_list:
                    text "尚无对话历史记录。":
                        font "fusion-pixel.ttf"
                        size 35
                        color "#FFFFFF"
                        xalign 0.5
                        outlines [ (1, "#000000", 0, 0) ]


## 此代码决定了允许在历史记录屏幕上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助屏幕 ########################################################################
##
## 提供有关键盘和鼠标映射信息的屏幕。它使用其它屏幕（keyboard_help、mouse_help
## 和 gamepad_help）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("在没有选择的情况下推进对话。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("键盘")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("上一页")
        text _("回退至先前的对话。")

    hbox:
        label _("下一页")
        text _("向前至后来的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://doc.renpy.cn/zh-CN/self_voicing.html}机器朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至后来的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至后来的对话。")

    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导，B/右键")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## 其他屏幕
################################################################################


## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问用户有关确定或取消的问题时，会调用确认屏幕。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复 no（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## 快进指示屏幕 ######################################################################
##
## skip_indicator 屏幕用于指示快进正在进行中。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“▸”（黑色右旋小三角）字形的字体。
    font "DejaVuSans.ttf"


## 通知屏幕 ########################################################################
##
## 通知屏幕用于向用户显示消息。（例如，当游戏快速保存或进行截屏时。）
##
## https://doc.renpy.cn/zh-CN/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式屏幕 ####################################################################
##
## 此屏幕用于 NVL 模式的对话和菜单。
##
## https://doc.renpy.cn/zh-CN/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在 vpgrid 或 vbox 中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 显示菜单，如果给定的话。如果 config.narrator_menu 设置为 True，则菜单
        ## 可能显示不正确。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## 对话气泡屏幕 ######################################################################
##
## 对话气泡屏幕用于以对话气泡的形式向玩家显示对话。对话气泡屏幕的参数与 say 屏幕
## 相同，必须创建一个 id 为 what 的可视控件，并且可以创建 id 为 namebox、who 和
## window 的可视控件。
##
## https://doc.renpy.cn/zh-CN/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

style quick_button_text:
    # 默认颜色（如果不在对话界面）
    idle_color "#FFFFFF"
    # 悬停时的颜色
    hover_color "#2f4f4f"
    size 26 # 根据需要调整大小

## 由于可能没有鼠标，我们将快捷菜单替换为一个使用更少、更大按钮的版本，这样更容
## 易触摸。
screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            style "quick_menu"
            
            # 逻辑判断：如果在 say 界面，默认文字为黑色，否则为白色
            $ is_say = renpy.get_screen("say")
            $ current_idle_color = "#000000" if is_say else "#FFFFFF"
            $ current_hover_color = "#2f4f4f" # 您指定的灰绿色
            
            textbutton _("回退"):
                action Rollback()
                text_idle_color current_idle_color
                text_hover_color current_hover_color

            textbutton _("历史"):
                action ShowMenu('history')
                text_idle_color current_idle_color
                text_hover_color current_hover_color

            textbutton _("快进"):
                action Skip() alternate Skip(fast=True, confirm=True)
                text_idle_color current_idle_color
                text_hover_color current_hover_color

            textbutton _("自动"):
                action Preference("auto-forward", "toggle")
                text_idle_color current_idle_color
                text_hover_color current_hover_color

            textbutton _("保存"):
                action ShowMenu('save')
                text_idle_color current_idle_color
                text_hover_color current_hover_color

            textbutton _("快存"):
                action QuickSave()
                text_idle_color current_idle_color
                text_hover_color current_hover_color

            textbutton _("快读"):
                action QuickLoad()
                text_idle_color current_idle_color
                text_hover_color current_hover_color

            textbutton _("设置"):
                action ShowMenu('preferences')
                text_idle_color current_idle_color
                text_hover_color current_hover_color


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

# 结局收集画面
screen ending_gallery():
    tag menu
    add "images/gui/main_menu_nofont.jpg"
    # 半透明遮罩层
    add Solid("#000000cc") 

    vbox:
        align (0.5, 0.5)
        spacing 30

        text "结局收集":
            size 50
            xalign 0.5
            ypos -150
            color "#ffffff"
            font "fusion-pixel.ttf" # 沿用像素字体

        # 结局按钮组
        grid 3 2:
            spacing 60
            xalign 0.5

            # 结局 A
            textbutton "结局 A：" + ("平稳收场" if persistent.ending_A else "？？？"):
                action If(persistent.ending_A, Replay("ending_a", scope={}, locked=False), None)
                text_idle_color ( "#ffffff" if persistent.ending_A else "#555555" )

            # 结局 B
            textbutton "结局 B：" + ("溺爱深渊" if persistent.ending_B else "？？？"):
                action If(persistent.ending_B, Replay("ending_b", scope={}, locked=False), None)
                text_idle_color ( "#ffffff" if persistent.ending_B else "#555555" )

            # 结局 C
            textbutton "结局 C：" + ("缓慢窒息" if persistent.ending_C else "？？？"):
                action If(persistent.ending_C, Replay("ending_c", scope={}, locked=False), None)
                text_idle_color ( "#ffffff" if persistent.ending_C else "#555555" )

            # 结局 D（虚无）
            textbutton "结局 D：" + ("无力黑暗" if persistent.ending_D else "？？？"):
                action If(persistent.ending_D, Replay("ending_d", scope={}, locked=False), None)
                text_idle_color ( "#ffffff" if persistent.ending_D else "#555555" )

            # 真结局 (A+B+C解锁)
            $ can_unlock_true = persistent.ending_A and persistent.ending_B and persistent.ending_C
            if can_unlock_true or persistent.true_ending_unlocked:
                textbutton "真结局：" + ("镜中的倒影" if persistent.true_ending_unlocked else "？？？"):
                    text_idle_color "#FFD700"
                    action Replay("true_ending", scope={}, locked=False)
            else:
                textbutton "真结局：？？？":
                    action None
                    text_idle_color "#555555"

            # 隐藏结局
            if persistent.hidden_ending:
                textbutton "隐藏结局":
                    action Replay("hidden_ending_1", scope={}, locked=False)
                    text_idle_color "#E24A4A" # 隐藏结局用红色区分
            else:
                textbutton "？？？":
                    action None
                    text_idle_color "#333333"

    # 4. 返回按钮
    textbutton _("返回"):
        style "return_button"
        align (0.95, 0.92)
        action Return()
