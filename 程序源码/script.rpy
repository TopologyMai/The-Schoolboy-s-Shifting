# ---------- 初始数值 ----------
default resonance = 5.0
default control = 5.0

# 初始状态开启 UI 显示
default show_value_ui = True

# 表情差分默认
default gc_face = "normal"
default gy_face = "normal"

# ---------- 路线选择 ----------
default current_route = None

# ---------- 结局 ----------
default persistent.ending_A = False
default persistent.ending_B = False
default persistent.ending_C = False
default persistent.ending_D = False
default persistent.hidden_ending = False
default persistent.true_ending_unlocked = False  # 用于保存真结局是否通关

default persistent.ending_hint_shown = False # 记录是否已经弹出过提示

default branch_choice = None # 是否从选项14去b结局

default persistent.seen_opening = False # 是否看过开头的meta文字

# 分支14循环次数
default branch_14_loop_count = 0

# ---------- 旁白文本 ----------
default normal_narrator_texts = []  # 普通旁白
default fullscreen_narrator_texts = []  # 全屏旁白

# --- 数值UI演示动画 ---
transform alpha_demo:
    alpha 0.0
    linear 0.2 alpha 0.9
    pause 0.8
    linear 0.3 alpha 0.0

screen value_hint(img):
    zorder 999
    add img:
        xalign 0.5
        ypos 750
        at alpha_demo

# ---------- 角色 ----------
define gc = Character("高超", color="#4A90E2", cps = 15)
define gy = Character("高越", color="#E24A4A", cps = 20)
define teacher = Character("物理老师", color="#ffffff", cps = 13)
define mom = Character("妈妈", color="#ffffff", cps = 18)
define zhuren = Character("教导主任", color="#ffffff", cps = 18)
define narrator_hidden = Character(None,  # 透明角色用于历史记录
    what_color="#ffffff",
    window_background=None,
    what_size=35,
    what_text_align=0.0)

# ---------- 背景 ----------
image bg warning = "images/bg/warning.jpg"
image bg classroom = "images/bg/classroom.jpg"
image bg memory = "images/bg/memory.jpg"
image bg corridor = "images/bg/corridor.jpg"
image bg staircase = "images/bg/staircase.jpg"
image bg staircase2 = "images/bg/staircase2.jpg"
image bg musicroom = "images/bg/musicroom.jpg"
image bg basketball = "images/bg/basketball.jpg"
image bg rooftop1 = "images/bg/rooftop1.jpg"
image bg rooftop2 = "images/bg/rooftop2.jpg"
image bg swimming1 = "images/bg/swimming1.jpg"
image bg swimming2 = "images/bg/swimming2.jpg"
image bg swimming3 = "images/bg/swimming3.jpg"
image bg observatory = "images/bg/observatory.jpg"
image bg starsky = "images/bg/starsky.jpg"
image bg starsky2 = "images/bg/starsky2.jpg"
image bg true = "images/bg/true.jpg"

# ---------- bgm ----------
define audio.bgm_cover = "audio/bgm/cover.ogg"
define audio.bgm_meta = "audio/bgm/meta.ogg"
define audio.bgm_classroom = "audio/bgm/classroom.ogg"
define audio.bgm_funny = "audio/bgm/funny.ogg"
define audio.bgm_aimei = "audio/bgm/aimei.ogg"
define audio.bgm_beichuang = "audio/bgm/beichuang.ogg"
define audio.bgm_hechang = "audio/bgm/hechang.ogg"
define audio.huajigangqin = "audio/bgm/huajigangqin.ogg"
define audio.bgm_chongtu = "audio/bgm/chongtu.ogg"
define audio.bgm_soft = "audio/bgm/soft.ogg"
define audio.bgm_horror = "audio/bgm/horror.ogg"
define audio.bgm_swim_horror = "audio/bgm/swim_horror.ogg"
define audio.bgm_swimpool = "audio/bgm/swimpool.ogg"
define audio.bgm_universe = "audio/bgm/universe.ogg"
define audio.bgm_endingb = "audio/bgm/endingb.ogg"
define audio.bgm_sad = "audio/bgm/sad.ogg"
define audio.bgm_mirror = "audio/bgm/mirror.ogg"


# ---------- 音效 ----------

define audio.se_chanming = "audio/se/chanming.ogg"          # 蝉鸣
define audio.se_rooftop = "audio/se/rooftop.ogg"        # 屋顶风声
define audio.se_pool_shower = "audio/se/pool_shower.ogg"        # 冲水声
define audio.se_pool_swim = "audio/se/pool_swim.ogg"        # 游泳声
define audio.se_jumpwater = "audio/se/jumpwater.ogg"        # 跳水声
define audio.se_destroy = "audio/se/destroy.ogg"        # 倒塌
define audio.se_laugh = "audio/se/laugh.ogg"        # 嘲笑
define audio.se_magic = "audio/se/magic.ogg"        # 魔法
define audio.se_bonus = "audio/se/bonus.ogg"        # 通关音效

# ---------- 公共函数 ----------
init python:
    import math
    def show_narrator(text):
        """显示普通旁白"""
        global normal_narrator_texts
        
        # 添加新段落
        normal_narrator_texts.append(text)

        # 直接将文本添加到历史记录，不显示任何内容
        narrator.add_history(kind="adv", who = "", what = text)
        
        # 显示旁白屏幕 
        renpy.show_screen("narration_screen")
        renpy.restart_interaction()

    def show_fullscreen_narrator(text):
        """显示全屏旁白"""
        global fullscreen_narrator_texts
        
        # 添加新段落
        fullscreen_narrator_texts.append(text)

        # 直接将文本添加到历史记录，不显示任何内容
        narrator.add_history(kind="adv", who = "", what = text)
        
        # 显示全屏旁白屏幕
        renpy.show_screen("fullscreen_narration")
        renpy.restart_interaction()
    
    def clear_narration():
        """清除普通旁白"""
        global normal_narrator_texts
        normal_narrator_texts = []
        renpy.hide_screen("narration_screen")
        renpy.restart_interaction()
    
    def clear_fullscreen_narration():
        """清除全屏旁白"""
        global fullscreen_narrator_texts
        fullscreen_narrator_texts = []
    
        # 确保完全清除
        renpy.hide_screen("fullscreen_narration")
        renpy.restart_interaction()

    # 生成乱码
    def generate_corrupted_text(text, corruption_level=0.5):
        import random
        corruption_chars = "!@#$^&*()_+-=[]{}|;:,.<>?/~`qwertyuiopasdfghjklzxcvbnm"
        result = ""
    
        # 将文本分成几个部分
        words = list(text)
    
        for i, char in enumerate(words):
            # 每个字符有30%的概率完全保留
            if random.random() < 0.3:
                result += char
            # 40%的概率变成乱码
            elif random.random() < 0.4:
                result += random.choice(corruption_chars)
            # 30%的概率变成乱码+原字符组合
            else:
                result += random.choice(corruption_chars) + char
    
        # 在开头和结尾随机添加一些乱码
        if random.random() < 0.5:
            result = random.choice(corruption_chars) * random.randint(1, 2) + result
    
        if random.random() < 0.5:
            result = result + random.choice(corruption_chars) * random.randint(1, 2)
    
        return result

    def get_ui_data():
        if not store.show_value_ui:
            return None, 0.0
    
        diff = store.resonance - store.control
        abs_diff = abs(diff)
    
        # 默认值：不显示任何图
        img = None
        alpha = 0.0
    
        # 共鸣 > 掌控
        if diff > 0:
            img = "images/gui/value_UI/resonance.png"
            if abs_diff >= 8:
                alpha = 0.6
            elif abs_diff >= 6:
                alpha = 0.4
            elif abs_diff >= 4:
                alpha = 0.2
    
        # 掌控 > 共鸣
        elif diff < 0:
            img = "images/gui/value_UI/control.png"
            if abs_diff >= 8:
                alpha = 0.6
            elif abs_diff >= 6:
                alpha = 0.4
            elif abs_diff >= 4:
                alpha = 0.26
    
        # diff == 0 不显示任何图
        return img, alpha

# ---------- 全屏旁白 ----------
screen fullscreen_narration():
    # 覆盖整个屏幕
    zorder 100
    
    frame:
        background None
        xalign 0.5
        ypos 0.1
        xsize 0.7
        ysize 0.7
        
        vbox:
            spacing 25
            
            # 显示所有文本段落
            for line in fullscreen_narrator_texts:
                text line:
                    font "fusion-pixel.ttf"
                    first_indent 60
                    size 35
                    color "#ffffff"
                    text_align 0.0

# ---------- 旁白 Screen ----------
screen narration_screen():
    layer "screens"
    
    frame:
        background "images/gui/narration.png"
        pos (474, 161)

        padding (30, 30, 20, 30) 
        xsize 1028
        ysize 446
        
        vbox:
            spacing 15
            xfill True
            
            # 显示所有文本段落
            for line in normal_narrator_texts:
                text line:
                    # font "fusion-pixel.ttf"
                    size 27
                    color "#000000"  # 字体颜色改为黑色
                    text_align 0.0
                    # xalign 0.5
                  
                    # --- 排版细节 ---
                    # justify True
                    line_spacing 1   # 行间距：9
                    kerning 0        # 字间距：0
                    first_indent 30  # 首行缩进：按照字号大小，7的话建议设为字号的1-2倍

label flash_effect:
    # 单层柔和闪光
    show pure_white as flash:
        alpha 0.0
        linear 0.2 alpha 0.6
        pause 0.3
        linear 0.5 alpha 0.0
    
    pause 1.0
    return

label check_all_endings:
    # 检查 A, B, C 是否都已达成，且提示还没出现过
    if persistent.ending_A and persistent.ending_B and persistent.ending_C and not persistent.true_ending_unlocked and not persistent.ending_hint_shown:
        $ persistent.ending_hint_shown = True  # 以后再也不会进这个判断了
        $ persistent.true_ending_unlocked = True # 正式解锁真结局权限
        
        play sound audio.se_bonus # 播放通关音效

        "恭喜你集齐 A / B / C 三个结局！"
        "真结局已在“结局收集”中解锁，快去看看吧。"
    return
                    
# ===============================
# 游戏开始
# ===============================
label splashscreen:
    scene black
    with None

    show bg warning:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(3)
    return

label start:
    # 如果玩过了就不要显示meta段了
    # 第0幕：游戏启动
    stop music fadeout 4.0
    pause 3.0

    if persistent.seen_opening:
        jump scene_classroom

    play music meta fadein 4.0

    $ show_fullscreen_narrator("喜剧节目断更的某个周五，百无聊赖的你从电脑的download文件夹里找到一个游戏。名字叫《坏小子》，难道和某个知名漫才组合有关？点开后，才发现是个又臭又短的小作坊文字游戏。既没有小说的正式，也没有文字游戏的简洁，只有胡乱的叙述和滑稽的剧情。") 
    pause 
    
    $ show_fullscreen_narrator("点开的瞬间，你的意识逐渐变得虚无，脑袋里只剩下一句：\n") 
    pause 

    with Dissolve(1.0)
    $ show_fullscreen_narrator("其实我是你的双胞胎哥哥啊……")
    pause
   
    
    $ show_fullscreen_narrator("\n分级：") 
    $ show_fullscreen_narrator(" (令人不安地, ) 15+") 
    pause 
    
    $ show_fullscreen_narrator("\n标签：") 
    $ show_fullscreen_narrator(" 校园/兄弟/纯爱") 
    pause 
    
    $ show_fullscreen_narrator(" 写在readme里的宣传文案：") 
    $ show_fullscreen_narrator(" 没有得到金棕榈、奥斯卡、诺贝尔、菲尔茨或任何知名奖项的小众神作。豆瓣均分2.8的不口碑作品！混乱的青春校园，禁忌的兄弟恋情，胡闹的魔法奇幻，都不在此作品里体现。不喜欢上学？那就让你的双胞胎弟弟为你解决吧！只要一点点爱的佐料，小越会为你做到120%～❤️") 
    pause
    $ clear_fullscreen_narration()
    
    $ show_fullscreen_narrator("人物介绍")
    pause
    $ show_fullscreen_narrator(" 【高超】：还未成为知名喜剧演员。只是一个普通的高中生。有一个双胞胎弟弟。性格稳重沉默，内敛敏感。正处在青春期，是最不愿意承认自己是弟控的年纪。") 
    $ show_fullscreen_narrator(" 【高越】：还未成为知名喜剧演员。只是一个淘气的高中生。有一个双胞胎哥哥，性格活泼好动，开朗外向。正处在青春期，其实能坦然承认自己的兄控身份，却因为照顾高超而假装恶心。\n") 
    pause 
  
    
    $ show_fullscreen_narrator("玩法介绍")
    pause
    $ show_fullscreen_narrator(" 数值系统：") 
    $ show_fullscreen_narrator("   【共鸣】：作为生物学和社会学上都高度相似的双子，同时也是相亲相爱的兄弟，甚至是亲密的玩伴、同学，乃至未来的同事，或是更亲密的关系。总之，兄长不可避免地会对弟弟产生怜爱和疼惜的想法。【共鸣】便是这部分共感、怜爱的数值体现。") 
    $ show_fullscreen_narrator("   【掌控】：也许出于父母的教导，也许出于社会的习俗，甚至是出于某人的性癖…？不管是行为的约束还是规则的引导，总之，哥哥管教弟弟天经地义。【掌控】便是这部分教习、引导的数值体现。\n") 
    pause

    $ show_fullscreen_narrator("……都是什么乱七八糟的。") 
    pause

    $ clear_fullscreen_narration()
    $ show_fullscreen_narrator(" 选项指引")
    pause
    $ show_fullscreen_narrator("   不同的选项不仅会导致数值的变化，也可能进入新的分支，甚至进入隐藏结局。最终的数值会决定结局走向：如果溺爱太过，教习不足，便容易双双跌入深渊（也许并不是坏事…？）；如果束缚过多，宠爱不足，则可能让弟弟灰心丧气；如果两者平衡，则会进入背后的真实世界，了解更多秘密。") 
    pause
    $ show_fullscreen_narrator("\n   不过，如果只考虑数值，忽略了高超的真实个性，也有可能被他跳出来指责。这点也请务必小心。") 
    pause
    
    $ show_fullscreen_narrator("\n {b}揣摩着高氏兄弟的少男心思，尝试收集全结局吧❤️{/b}")
    with Dissolve(1.0)
    pause 
    
    $ show_fullscreen_narrator("\n玩家的初始属性：") 
    $ show_fullscreen_narrator(" 【共鸣】：5；【掌控】：5") 
    pause
    $ clear_fullscreen_narration()
    
    menu: 
        "姑且玩一玩吧…": 
            $ clear_fullscreen_narration()
            $ persistent.seen_opening = True   # 标记已看过
            jump scene_classroom

    label scene_classroom: 
        scene bg classroom: 
            zoom 1.5 
            xalign 0.5 
            yalign 0.5 
        with fade
        stop music fadeout 4.0

     # —— 旁白阶段 ——
    pause 4.0
    play sound chanming fadein 2.0

    $ clear_fullscreen_narration()
    $ show_narrator("倒数第二排靠窗位置。传说中的嘎拉给木专属男主座位，可惜高超不怎么玩儿文字游戏。他还是玩操作类的更多，英雄联盟，CSGO之类的。")
    pause
    
    $ show_narrator("…不过CSGO玩得没高越好就是了。")
    pause
    
    $ show_narrator("教室里无人专心听讲。窗外蝉鸣阵阵，伴着潮湿炎热的风传进耳边。高超撑着头向外看，天蓝得一丝白云也没有，晴朗辉煌，给他烦躁的心平添忧郁。视线向下，能看到楼下有几个人在打篮球，还有国际班学生在草坪上推动除草机，再仔细听，远处的音乐教室里传来的乐声。钢琴声断断续续，并不很流畅。")
    pause

    $ clear_narration()

    $ show_narrator("今天物理老师似乎格外宽容，不揪着高超骂，说他出神发呆，只自顾自拿个三角板在黑板上比比画画，嘴里念念有词，讲一道天体物理题。说着说着，又聊到最近的天文发现。")
    pause

    teacher "最近有一则新闻：鼎鼎大名的明亮星体参宿四，在2026年终于被发现还有一颗很小很小的伴星。而这颗伴星的存在，解释了此前参宿四运行规律的所有可疑之处。"
    teacher "这就是我们常说的双星系统。"
    teacher "无论数量级如何，引力和斥力并存，相互吸引也相互排斥，平衡才是双星系统可以长久运作下去的根本。我们计算引力的公式是什么？诶，对了，是——"
    # —— 选项前隐藏旁白 ——
    hide screen narration_screen

    #分支0
    menu:
        "F = G × (m₁m₂)/r²":
            $ resonance -= 0.5
            $ control += 1
            "答出了正确的公式。对高越的掌控增加，而彼此的共鸣减少。"
            $ renpy.show_screen("value_hint", img="images/gui/value_UI/control.png")
            $ renpy.pause(1.0)
            $ renpy.hide_screen("value_hint")
            $ gc_face = "wuyu"
            gc "...好像得到了什么galgame作弊器。可以感觉到高越的态度。"
            $ gc_face = "normal"

        "……高越在干嘛呢？":
            $ resonance += 0.5
            $ control -= 0.5
            "出神地思念高越。和高越的共鸣增加，但对他的掌控减少。"

            $ renpy.show_screen("value_hint", img="images/gui/value_UI/resonance.png")
            $ renpy.pause(1.0)
            $ renpy.hide_screen("value_hint")
            $ gc_face = "wuyu"
            gc "...好像得到了什么galgame作弊器。可以感觉到高越的态度。"
            $ gc_face = "normal"

    
    # —— 回到旁白 ——
    window hide
    $ clear_narration()

    $ show_narrator("高超打了个哈欠，眼角泛起泪光。")
    pause

    $ show_narrator("高越就是在这时出现在窗户外。")
    pause
    stop sound fadeout 4.0

    play music classroom

    $ show_narrator("高超一下子回过神来。他看着眼前人和他如出一辙似的蠢脸——不对，怎么能说自己这张脸蠢！蠢的是高越才对。他的双胞胎弟弟留着一头清爽的短发，眉上刘海微微被汗沾湿，毛茸茸地搭在额头上。高越变戏法似的蹦到他眼前，表情很夸张地打招呼。高超烦闷而倦怠的脸立刻有了松动。顾不上掩饰，他赶紧向高越搭话。") 
    pause 

    gc "你来干什么啊？" 

    $ show_narrator("此时正是高一的第二学期。") 
    pause 

    $ show_narrator("…也是高超和高越不再时时刻刻黏在一起的第八个月") 
    pause 

    # 回忆闪回转场
    scene bg memory:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(3)

    play sound chanming

    $ clear_narration()

    $ show_narrator("一年前，妈妈领着他俩来教务处交学费。嘱咐高超看好弟弟后，妈妈独自进了校门。") 
    pause 

    $ show_narrator("高超紧紧牵着高越的手。高越举了根老冰棍使劲儿地舔，眼睛滴溜溜地看着人来人往的校门。傻子，高超心满意足地想着。我去里面去上个厕所，站这儿别动啊。") 
    pause 

    $ show_narrator("从卫生间回来路上，高超听见妈妈和教导主任说话。他按耐不住好奇，放慢了脚步。") 
    pause 

    mom "我家这对双儿，能不能不分在同一个班？他俩从小到大没分开过。再这样黏在一起，恐怕不利于他俩社交。"

    $ clear_narration()
    $ show_narrator("哥哥妈妈都在里面，高越好奇心止不住地飞，奈何答应了哥不乱跑，只好眼睛四处乱瞟，从大门瞟到女生的领结，又望到篮球服和足球鞋，心想，听说这学校有个不错的体育场。而高超冲出来，紧紧抱住他，冲得高越背痛。高越还举着冰棍，伏在他怀里舔着。") 
    pause

    $ gy_face = "surprise"
    gy "怎么了？"
    $ gy_face = "normal"
    gc "……" 

    $ show_narrator("高超不回话。高超骂人挺难听的，高越第二讨厌挨他骂，和挨打同等讨厌。最讨厌的，还是他不说话的时候。高越没办法了，把冰棍塞他嘴里，凉得高超一激灵。") 
    pause

    # 回忆结束，闪回转场
    scene bg classroom:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(2)
    $ show_narrator("高超浑身猛地一抖。他赶紧转头看老师，老师还在专心地画他的天体示意图。") 
    pause 

    
    gy "想什么呢？" 
    gc "你赶紧回去。" 
    gy "没事的。你看我一眼。高超！看我一眼。不会有人骂你的。"

    $ clear_narration()    
    $ show_narrator("高超狐疑地望去。他鼓起勇气抬头，飞快地看一眼，高越还穿着那件校服：浅蓝色短袖，上面系了一条黑色短领带，除了因为毛手毛脚而格外皱巴以外，和高超的并无区别。") 
    pause 

    gy "你看哪儿啊！这才是重点。" 

    $ show_narrator("高越在他眼前挥手，高超定睛一看：一支玉桂狗联名按动水性笔。仔细看来，玉桂狗眼下还有一颗小痣。想必是高越无聊的时候点的。高超仔细盯着那支圆珠笔，只觉得那痣圆融得仿佛天生。怎么回事，谁允许对玉桂狗进行二创了。这符合版权法吗？") 
    pause 

    $ show_narrator("高越得意洋洋。") 
    pause 

    $ gy_face = "smile"
    gy "这是我的魔法棒。"
    $ gy_face = "normal"

    hide screen narration_screen

    # 分支1选项 
    menu: 
        "你又借人文具不还……": 
            $ resonance -= 1 
            $ control += 2
            $ gy_face = "xinxu"
            gy "没——有——。高超嗷嗷嗷你怎么污蔑你弟弟啊！"
            gc "你就说干没干过吧。" 
            gy "真没有！！"
            $ gy_face = "normal"
        "叹口气": 
            $ resonance += 0.5 
            $ control += 1
            $ gy_face = "xinxu"
            gy "……又叹什么气呢。"
            $ gy_face = "normal"
            gc "谁做你哥哥都这样。" 
        "你高兴就好": 
            $ resonance += 2 
            $ control -= 1
            $ gy_face = "xinxu"
            gy "…嗯嗯？"
            $ gy_face = "normal"
            gy "什么意思，我都有点不习惯了。" 

    $ gy_face = "surprise"
    gy "我真有魔法棒！不是，我真会魔法！！" 
    gy "魔法。麦吉克！"
    $ gy_face = "normal"
    $ clear_narration()  
    $ show_narrator("高越还是小孩子心性（其实高超也是，但他已经是中学生了。故他不承认。），一急就随地大小闹，当即在窗外开始跺脚哼唧，甚至有就地躺下撒泼的趋势。") 
    pause 

    $ show_narrator("高超吓一大跳，而物理老师仿佛被什么迷住了一般，仍在专心致志地画图。") 
    pause 

    $ show_narrator("高超低头看题，不过几根线组成的图像，可老师怎么也不满意，画了又擦，擦了又画，偶尔还停下来对着黑板发呆，抱着手臂出神，仿佛在打磨一副艺术品。") 
    pause 

    $ show_narrator("高超终于觉察出不对来。") 
    pause

    stop music fadeout(4.0)

    $ clear_narration()

    $ show_narrator("纪律委员是个锅盖头男生，总是眯着小眼睛巡视班级。他今天怎么没来？而高越抬起那只蓝色水性笔，小拇指很诡异地翘起，笔顶上的玉桂狗在空气里转了一圈。班里第二讨厌的副班长哞地一声倒在课桌上，睡得很香。") 
    pause

    play sound magic fadeout(0.5)
    gy "相信了吗？高超，说话！"

    hide screen narration_screen

    # 分支2选项 
    menu: 
        "…好吧": 
            $ resonance += 1.5 
            $ control -= 1
            jump continue_story

        "（摇头）":
            $ resonance -= 2 
            $ control += 0.5
            jump check_disbelief 

label check_disbelief: 
    gy "真不相信？"
    
    menu: 
        "（摇头）":
            $ resonance -= 1
            $ control += 0.5
            gy "还是不相信？"
            
            menu:
                "（摇头）":
                    gy "高超，你都不相信我…？" 
                    jump hidden_ending_1 
                "…行了":
                    $ resonance += 0.5
                    $ control -= 0.5
                    jump continue_story
        "…行了": 
            $ resonance += 0.5 
            $ control -= 0.5
    jump continue_story
    
label continue_story:
    $ gy_face = "smile"
    gy "嘿嘿。我也没明白怎么回事呢。就是普通地上着老王的课，就我们班那英语老师。什么how are you thank you and you的，听得我眼皮直打架。" 
    gy "我就想，如果我有魔法就好了，就能光明正大地逃课。反正我也听不明白，坐这儿干嘛？" 
    gy "想着想着，我忽然就有勇气了。于是以上厕所为借口，走出教室。结果，高超，你猜怎么着！二十分钟了，没人管我，也没人惦记我。就像忘记我了一样。肯定是坏孩子的神听到了我的祈祷…" 
    gy "既然如此，咱俩不干点什么吗？说不定过了12点就失效了。我们得抓住机会呀！" 

    gc "谁跟你说12点失效的。"
    $ gy_face = "normal"
    gy "动画片里都这样演！"
    $ gc_face = "wuyu"
    gc "那个是白雪公主！"

    $ show_narrator("如愿以偿地听到了哥哥的吐槽，高越心满意足地朝哥伸出手。他的手并不算骨节分明，还在发育的中段，像从泥土里拔节而出的树根，有茁壮的趋势，却还没有实体。教室窗户外有护栏，而高越的手刚好能穿过期间的缝隙。高超假装不在意地握住那只手，轻描淡写地回握。") 
    pause

    $ clear_narration()

    $ show_narrator("{size=+10}魔法，正式生效。{/size}")
    pause

    $ clear_narration()     

    # 第二幕开始
    scene bg classroom: 
        zoom 1.5 
        xalign 0.5 
        yalign 0.5 
    with fade
    play music classroom fadein 2.0
    $ show_narrator("头顶的风扇在空转。") 
    pause 

    $ show_narrator("青岛的夏天比不上南方，但温度仍然不低。空气里传来咸咸的气味，不是海风，只是汗味。高超只是坐着，头上和背上就起了一层薄汗。高越的出现毫无疑问激发了他逃课的愿望。他愈发坐不住了。") 
    pause 

    $ show_narrator("高越百无聊赖地站在窗户外，让高超出来和自己一起玩儿。") 
    pause 

    gy "高超嗷嗷嗷嗷嗷嗷，别装好孩子了。出来玩会儿呗。老师不会发现的！"

    gc "你小声点。没看见老师眼睛一直往这边瞟吗！"
    $ gc_face = "normal"

    $ show_narrator("确实如此。即使同学们都对高越站在窗外的事置若罔闻，老师仍然时不时往窗户方向扫上几眼，把高超吓得更烦躁了。高越看他不理会，明白这事需要徐徐图之。他转移方向，对着高超的背，故作嫌弃。") 
    pause 

    gy "哥，你衣服都湿了。汗流浃背了吧！"

    hide screen narration_screen
    $ clear_narration()
    
    # 分支3选项 
    menu: 
        "所以？": 
            $ resonance -= 1 
            $ control += 1.5 
            gy "你这人没劲！" 
        "那你帮我弄干吧。": 
            $ resonance += 2 
            $ control += 1
            $ gy_face = "xinxu"
            gy "……嗯？"
            $ gy_face = "normal"
        "？想干嘛": 
            $ resonance += 0.5 
            $ control -= 1
            $ gy_face = "smile"
            gy "嘻嘻，不想干嘛。"
            $ gy_face = "normal"

    gy "这点小事，就让小魔法师越大师为你解决吧！" 

    $ show_narrator("说完，他又以那个笨拙而诡异的姿势挥动他的玉桂狗圆珠笔。高超盯着他得意洋洋的讨打神色，惊奇地发现衣服真的干了。他又用手背碰额头，肌肤相贴时传来了清爽的触感。一切都提醒高超，这并非高越的恶作剧。\n") 
    pause

    play sound magic fadeout(0.5)

    $ show_narrator("但老师却忽然发现了什么一般，点高超起来回答问题。他走神那么久，自然说不出任何。物理老师叹口气，说既然心思不在教室，就去外面凉快凉快吧。高超蹭地一下站起身，一声不吭地走出教室。高越站在他身边，安抚地拿肩膀蹭他的肩膀。") 
    pause

    $ clear_narration()

    scene bg corridor:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(3)

    $ show_narrator("他们身量类似，身高也相差无几。这个蹭蹭动作精准得像对齐两行公式。高超吸吸鼻子，一言不发地往高越那边又靠了靠。") 
    pause 

    gy "之前那个，说你以后就在街头演小品的，就是这老头？"
    gc "……嗯。"

    $ show_narrator("苦涩的回忆袭来。") 
    pause

    $ clear_narration()

    $ show_narrator("被发现在物理课上背台词的事纯属意外。那是他和高越在新年联欢要演的节目，赵本山和宋丹丹的经典小品。高超没想过老师如此斤斤计较，更不知道他们在外学曲艺的事他也知道。这老头真够闲的，高越后来点评道。") 
    pause 

    $ show_narrator("而高超只有铺天盖地的委屈。高越不在他身边，他好像失去肌肤屏障的透明人。免疫系统被强行剥离，既没有底气，也没有回击的欲望。") 
    pause 

    gy "唉，怎么又不高兴了。"
    $ gy_face = "smile"
    gy "魔法是什么时候用的？诶，就是这种时候。"
    $ gy_face = "normal"
    gc "……你别乱来。老头一直不喜欢我。" 
    gy "那他更该死了。" 
    gy "你不想惩罚他吗？他对你那么坏。" 
    stop music fadeout 3.0
    hide screen narration_screen

    # 分支4选项 
    menu: 
        "想啊。": 
            $ resonance += 2 
            $ control -= 1.5
            $ gy_face = "smile"
            gy "对喽！你就瞧好吧。"
            $ gy_face = "normal"
            gc "你这么一说，我开始担心了。" 
            gy "操那么多心呢。你就是操心太多才累。"
            jump ezuoju
        "要不还是算了": 
            $ resonance -= 2 
            $ control += 1 
            gy "算不了。哪能让这事算了。" 
            gc "…" 
            gy "你放心吧，高超。绝对安全可控，相信我。行吗？" 
            menu: 
                "行吧…": 
                    jump ezuoju 
                "不行": 
                    $ resonance -= 0.5 
                    $ control += 1 
                    jump buezuoju
        "…你打算怎么做": 
            $ resonance += 1.5 
            $ control -= 1 
            gy "放心吧，不会出什么大事的。" 
            gc "你保证？" 
            "高越举起右手发誓。高超赶紧打掉他的手。"
            $ gy_face = "xinxu"
            gy "知道知道。不会乱来的"
            $ gy_face = "normal"
            jump ezuoju

label ezuoju: 
    "高越又晃动他的塑料魔法棒，这次高超甚至听到了施法的音效。"
    play sound magic fadeout(0.5)
    play music funny fadein 1.0
    "那秃头老师还在台上喋喋不休，五分钟后，他疲惫地喝了一口茶，随即剧烈地咳嗽起来。物理老师的嘴唇被白色粉笔灰糊满，白色粉末随着咳嗽四处喷射，前排的好几个同学都被喷了一脸。"

    teacher "谁！谁干的！" 
    
    "高超高越在门口笑弯了腰。"
    "高越得意洋洋，近乎狂妄了。虽然不想让高越太得意，但说不高兴是假的。他笑眼弯弯，想和高越多说几句话，却在看清高越身后的人后马上变了神色。他努努嘴让高越转身。"

    $ gc_face = "wuyu"
    gc "高越，后面。"
    $ gy_face = "surprise"
    gy "什么啊…？"

    "高越疑惑地转身，发现教导主任在往这边走。"

    jump houxu 

label buezuoju: 
    "高越有点讪讪的样子。"

    gc "知道你为我打抱不平。但还是别乱来了。你忘记上次逃晚自习，咱爸怎么抽你来着。"
    $ gy_face = "xinxu"
    gy "…啊啊啊啊啊，别提了别提了。"
    $ gy_face = "normal"

    play music funny fadein 1.0

    "高超看他上蹿下跳，扶着脑袋说屁股大开花的事不必再提！！他嘴角上扬却在看清高越身后的人后马上变了神色。他努努嘴让高越转身。"

    $ gc_face = "wuyu"
    gc "高越，后面。"
    $ gy_face = "surprise"
    gy "什么啊…？"

    "高越疑惑地转身，发现教导主任在往这边走。两人立刻手忙脚乱起来。"
    jump houxu

label houxu: 
    gy "啊啊啊啊啊怎么办。" 
    gc "魔法呢！你的魔法呢。" 
    gy "隐形斗篷？哈利波特那个。不知道能不能行得通但姑且先试试吧。" 
    gc "能吗。能吗？？" 
    gy "不知道啊！" 
    gc "。我真无语" 

    "高越尝试转动魔法棒。可教导主任还是注意到他们。即使并不咄咄逼人，但被他扫了一眼，高超高越都吓得站直了。"

    $ gc_face = "smile"
    $ gy_face = "smile"
    zhuren "在这里干嘛？" 
    gc "罚站。" 
    gy "我出来上厕所。" 
    zhuren "行。"
    $ gc_face = "normal"
    $ gy_face = "normal"

    "教导主任并不多怀疑，巡视保安一般回到原本笔直的监察路线，静静飘走了。"

    $ gy_face = "xinxu"
    gy "吓死我了。"
    $ gy_face = "normal"
    stop music fadeout 3.0

    $ clear_narration()  

    $ show_narrator("他一紧张就管不住手脚。反应过来时，高越已经紧紧握着哥的手心。高超盯着两人牵紧的手看。自从进入中学，他俩很少再牵过手了。") 
    pause


    $ show_narrator("…高越看着有点紧张。") 
    pause

    play music aimei fadein 2.0

    $ gy_face = "normal"
    $ gc_face = "normal"
    gy "…不可以吗？"

    hide screen narration_screen

    # 分支5选项 
    menu: 
        "随你吧": 
            $ resonance += 2 
            $ control -= 1.5
            
            gy "…嗯。" 
            "高超难得坦率，他都有点不习惯了。不对！是谁攻略谁啊！？"
            "反正高超/高越没说不喜欢。两人心照不宣地牵着手。"

        "不可以。很恶心": 
            $ resonance -= 2 
            $ control += 2.5 
            gy "哼。我还没嫌你恶心呢。"

            $ gc_face = "wuyu"
            gc "既然都恶心那还牵着干嘛？"
            $ gc_face = "normal"

            "两人心怀鬼胎地甩开对方的手。"
            stop music fadeout 3.0

    gy "不多走走吗？反正都被教导主任发现了。"

    $ gc_face = "wuyu"
    gc "什么逻辑。"
    $ gc_face = "normal"

    gy "反正我俩也不走远，就在学校里转转呗。"
    stop music fadeout 4.0

    $ show_narrator("高超脸上没有拒绝的意思。话音刚落，高超慢悠悠地向楼梯方向走去。高越紧随其后。") 
    pause

    $ clear_narration()
    scene bg staircase:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(3)

    $ show_narrator("楼梯间很安静。楼上隐约传来断断续续的钢琴声，以及并不和谐的伴唱。温和，悠扬，却也惹人心烦；楼下则是高年级学长在打篮球，青春激扬，但也许暗藏危机。") 
    pause 
    
    $ show_narrator("接下来，要去哪里？{b}选项将会影响整体数值变化和场景，乃至结局走向。请慎重选择。{/b}") 
    pause 

    $ clear_narration()  
    hide screen narration_screen

    # 场景选择 
    menu: 
        "上楼梯（音乐教室）":
            $ current_route = "music"
            jump music
        "下楼梯（篮球场）":
            $ current_route = "basket"
            jump basket

label music:

    $ show_narrator("走到楼梯前，两人牵着的手忽然松了。螺旋状的楼梯垂直上升，高越脚步快，两步跨过一个大阶梯，高超跟在他后面，看他弟弟跳过石灰砌成的红色台阶。被蹭掉的油漆粉末粘在鞋底上，但很快被高越轻巧的步子震落。") 
    pause

    scene bg staircase2:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(3)

    play music beichuang

    $ show_narrator("断断续续的琴声越来越清晰。那是一首高超以前就听过的曲子，轻缓、宁静，混杂一点儿无伤大雅的悲伤。") 
    pause 

    $ show_narrator("上数学课（枯燥、无聊！）和物理化学（比数学好点儿。但没好到哪里去）的时候，高超常常装作认真听讲的样子，心神却随着空气里的乐声扶摇直上。他后来去查了，那是一首贝多芬的曲子。") 
    pause

    $ clear_narration()

    $ show_narrator("他常常听着那首钢琴曲发呆。想着想着，却是高越的脸，从记忆里蹦出来。听到这个曲调，就想到高越；和高越在一起的时候，却什么都忘记了。") 
    pause 

    $ show_narrator("高越看他若有所思的样子，停下脚步等他。他正逃学逃得起劲呢。现在开始才是最好玩的地方吧？但高超又怎么了。") 
    pause 

    $ gy_face = "smile"
    gy "你快点吧老鳖高超。龟兔赛跑的故事听说没？" 
    gy "小兔子都领先你一层了。高超，你这个年纪怎么发得了呆呀。我都替你着急！" 
    $ gy_face = "normal"

    $ show_narrator("他就不能不嘴贱？高超有点恨铁不成钢了。明明刚刚气氛很好……") 
    pause

    hide screen narration_screen

    # 分支6选项 
    menu: 
        "不说话。盯着高越看": 
            $ resonance -= 1.5
            $ control += 1.5
            gy "…干嘛呀。" 
            "被高超直直盯着，立刻老实下来了。甚至往下走了两阶台阶。要不要我背你上来啊？他试探着问。而高超仍然置若罔闻。"
            gy "不会是因为我没牵着你手生气吧。"
            $ gc_face = "wuyu"
            gc "你要死啊高越。"
            $ gc_face = "normal"
            $ gy_face = "smile"
            gy "嘻嘻～"
            $ gy_face = "normal"

        "狠狠吐槽之。加快脚步走上去": 
            $ resonance += 1.5 
            $ control -= 1
            gc "我看你是阳亢。还小兔子。"
            $ gc_face = "wuyu"
            gc "很吵，高越，非常吵。"
            $ gc_face = "normal"
            gy "略略略。" 
        "不理他。": 
            $ resonance -= 2 
            $ control += 2
            gy "…没劲。"

    scene bg musicroom:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(3)

    $ clear_narration()

    $ show_narrator("两人最终走到音乐教室的后门处。门上有小块玻璃，两个脑袋挤在一起，看里面的人叽叽喳喳。") 
    pause

    $ show_narrator("音乐教室的座位是阶梯形，一层层学生的脸依次铺开。高超看他们挤挤挨挨地站在一起，专心地唱同一首歌。诶，高越拿手肘捅他，正击中他最痛的肋骨处。想死？高超用手环过高越脖子，而高越气息微弱地说，其实我觉得你唱歌挺好听的。") 
    pause 

    gc "！" 
    $ show_narrator("高超几乎是立刻就松手了。") 
    pause 

    $ show_narrator("自从在音乐课上被点名唱歌以后，他就对当众唱歌这件事相当抗拒。") 
    pause 

    $ show_narrator("其实是很小的事，高超想，我知道，这都是很小的事。")
    pause 

    $ clear_narration()  

    $ show_narrator("但只要路过音乐教室，那段回忆就会立刻带着新鲜的气味蜂拥而上。那是羞耻和尴尬的味道。") 
    pause 

    $ show_narrator("他在全班面前跑调了。全班同学都哈哈大笑，而音乐老师没有制止，只是微笑地谢谢他的参与。") 
    pause 

    $ show_narrator("他根本不想参与。也不想被谢谢。他讨厌唱歌。") 
    pause 

    gy "高超，你听见他们在唱什么了吗？" 
    gc "校歌。"
    stop music fadeout(3.0)
    pause 3.0
    play music hechang

    $ clear_narration()  

    $ show_narrator("无非就是一些采撷阳光，播种雨露，勤读精思，守纪健身之类的套话。每个人都站在平铺的人群里，伴着平直的曲调，像失掉所有个性一样，唱着一些根本不相信的事。") 
    pause 

    $ show_narrator("高越笑眯眯的。只消一眼，高超就明白他想干什么了。") 
    pause 

    $ show_narrator("…高越根本不在乎合群不合群。那小子什么都不放在眼里。只有自己会在乎。高超低下头，扯进校服下摆，试图抚平上面的几缕褶皱。") 
    pause 

    hide screen narration_screen
    # 分支7选项 
    menu: 
        "阻止": 
            $ resonance -= 2 
            $ control += 3 
            gc "停手。" 
            gy "不会怎么样的。这么多人，我都不一定成功。" 
            menu: 
                "好吧": 
                    $ resonance += 1 
                    $ control -= 1
                    jump music_continue 
                "不可以": 
                    $ resonance -= 1 
                    $ control += 1 
                    jump cannotstop
        "放任": 
            $ resonance += 3 
            $ control -= 2 
            gc "嗯。"
            $ gy_face = "surprise"
            gy "我还以为你会阻止我。"
            $ gy_face = "normal"
            gc "你希望我阻止你？" 
            gy "废话，当然不想。" 
            gc "那不就行了。"
            jump music_continue 
        "默许": 
            $ resonance += 1 
            $ control -= 1.5
            gy "行。你就瞧好吧。"
            jump music_continue 

label cannotstop: 
    gy "嗯。"
    gy "嗯………………………………"

    # 回到主线 
    jump music_continue 

label music_continue :
    $ clear_narration()
    stop music
    play sound magic
    pause 3.0
    play music huajigangqin fadein(1.5)
    $ show_narrator("高越举起魔法棒，教室里的三十多个人忽然失声一般，徒劳地张嘴，却发不出声音。钢琴的声音也从无趣的大调伴奏，逐渐转为轻快的琴声。音乐老师惊慌地松开手，而钢琴键自发地弹奏乐声，清晰悠扬，再不复以前的断断续续。")
    pause 

    $ gy_face = "smile"
    $ gc_face = "smile"
    gy "喜欢吗？" 
    gc "嗯。" 

    $ show_narrator("仿佛被人按住后脑勺，高超鬼使神差地点头了。他竟逐渐不能分辨那是他真实的心声，还是高越的魔力。") 
    pause 

    $ show_narrator("高超心底生出一种隐秘的恐惧，而这恐惧指向一个不能说的猜想。如果他完全放任高越胡来，他，还有高越。他们最终会闹到什么地步？") 
    pause 

    $ gy_face = "normal"
    $ gc_face = "normal"
    gy "再上去走走？"

    "高越说着，双手插进校服口袋里，自顾自离开后门，转身往楼梯处走去。"
    $ clear_narration()
    hide screen narration_screen with Dissolve(3.0)

    stop music fadeout(3.0)

    # 进入天台场景 
    jump rooftop

label basket:
    scene bg basketball:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(3)


    $ show_narrator("还没打下课铃，学校里没几个人。高超高越牵着手在学校操场附近闲逛，走到篮球场时，高越忽然起了兴致，问高超要不要打一局。") 
    pause

    play music classroom fadein(2.0)

    $ gc_face = "wuyu"
    $ gy_face = "smile"
    gc "那你变个篮球出来？" 
    gy "篮球有什么难的。"

    $ show_narrator("两人偷偷溜进操场旁的器材室。倒不需要什么魔法，器材室没锁门，高越试探着拧开把手，就成功打开了门。这期间高超在门口替他把风。") 
    pause 

    $ show_narrator("他以前就常和高越一起做坏事。狼狈为奸有两种解法，一是狈趴在狼背上指挥打这打那，一是狼司令指挥自己的得意助手狈将军为非作歹。") 
    pause 

    $ show_narrator("高超高越的坏孩子往事里两者皆有，但高超只承认第一种。才不是什么狼司令呢，只是弟弟想干，他作为哥哥，有监督的义务。") 
    pause
    $ clear_narration()  
    
    "拿到篮球后，高越拍了几下球。"

    gy "现在可以来一局了吗？"
    gc "行。" 
    $ gc_face = "normal"
    $ gy_face = "normal"

    $ show_narrator("他们都不是特别热衷篮球的那种男学生。比起体育竞技，更喜欢电子竞技，但男孩儿们的社交无非就那几种，高超偶尔也跟着打几回。高越参与的理由更不纯粹一些：篮球打得好容易出风头，更容易被女同学喜欢。") 
    pause

    $ show_narrator("在高超还在支支吾吾读名著里的爱情桥段里时，高越已经坦诚地面对青春期赠予的一切。不管是身高拔高，四肢抽节，还是忽然冒头的对情爱的好奇，他都照单全收。可惜高越篮球打得也一般，勉强能在班级对抗赛里上场的水平，谈不上冒尖，通过打篮球惹女孩注意的计划很快泡汤。") 
    pause

    $ clear_narration()  

    $ show_narrator("和别人打球还要注意些礼节，和高越则完全不用在乎那些。高越的身体发展节律和他几乎完全一致，力量也相当，两个人打得有来有回，并没有明确的输赢。好几次用胳膊圈住高越，让他不得动弹时，高超都在这身体对抗中得到发泄般的快感。") 
    pause 

    $ show_narrator("两人打得大汗淋漓。虽然没有裁判，但高超默默在心里记分，拿下关键球的前一秒钟，高越柔弱倒地，哼哼唧唧地赖在地上。") 
    pause 

    stop music fadeout 4.0
    hide screen narration_screen

    # 分支8选项 
    menu: 
        "关心高越是不是受伤了": 
            $ resonance += 2 
            $ control -= 1.5

            $ gc_face = "smile"
            gc "怎么了，是不是摔哪了？" 
            gy "嗯，胳膊肘和膝盖都火辣辣滴疼。" 
            gc "真疼假疼，我上手检查了啊。"
            $ gy_face = "xinxu"
            gy "假的假的。"
            $ gc_face = "normal"
            $ gy_face = "normal"
            "高越赶紧起身了。"

        "揣着手看他。": 
            $ resonance += 0.5 
            $ control += 1.5
            $ gy_face = "surprise"
            gy "来人啊——犯规啦——篮球场上谋杀亲弟了。"
            $ gc_face = "wuyu"
            gc "你又耍赖。高越，你总是耍赖。没意思。我不玩了。"
            gy "干嘛呀！还不让人耍赖了。高超，你就不能不让让你弟弟？" 
            gc "起来。我不会说第二遍。"
            $ gc_face = "normal"
            $ gy_face = "normal"
            "高越灰溜溜地爬起来。"

        "不理他。直接投三分": 
            $ resonance -= 2 
            $ control += 2 
            gy "没劲。"
            gc "耍赖就有劲？我不和爱耍赖的人玩儿。"

            $ gy_face = "smile"
            $ gc_face = "wuyu"
            gy "你选不了，高超。我是你弟弟。"
            gc "……"
            $ gc_face = "normal"
            $ gy_face = "normal"
            "三分球直直射进篮筐。"

    play music chongtu
    $ clear_narration()  
    $ show_narrator("高越从小就这样。高越从小就这样…他俩幼儿园的时候玩弹珠，高越偷偷把哥的弹珠扔进下水道，高超蹲在路边一直哭。他没忍住动手揍了高越，打得高越破皮了，爸妈一边一个上来劝，而高超心里只有一句话，反复地响起：没意思。我不玩了。高越，我不想玩了。") 
    pause 

    gy "玩儿呢，高超，只是玩儿。你会不会太认真了？" 
    gc "如果不认真，输赢就没有意义了。" 

    $ show_narrator("最后还是赢了高越。高越的三分射偏，很不高兴地哼哼起来，坐在一旁喘气。高超又觉得没意思起来。") 
    pause 

    $ show_narrator("这节课会不会太长了？高超感觉他俩都打了快三十分钟") 
    pause

    gc "你不口渴吗？咱俩上哪喝口水去吧。"
    gy "…行啊"

    $ clear_narration()  
    $ show_narrator("高超还以为他又会从哪偷（是借。借用！会还的）来两瓶矿泉水，可高越打个响指，不知从哪冒出来两个女生，都是高超见过的脸。一个是他的同班同学，一个是高越他们班的。两个女孩儿掏出两瓶矿泉水，说喝这个吧。") 
    pause 

    $ gc_face = "wuyu"
    gc "…你们不该在上课吗！"
    $ gc_face = "normal"

    $ show_narrator("高超有点无力吐槽了。百分百是高越在搞鬼。用这种形式受欢迎，他觉得很滑稽，但女孩儿们的手还伸着，他不好拒绝。") 
    pause 

    hide screen narration_screen
    # 分支9选项 
    menu: 
        "你们是来找高越的？": 
            $ resonance -= 1.5 
            $ control += 2 
            "女生们：对…啊啊啊，不对。也对，或者说…"
            "她们说话颠三倒四，动作并不自然，提线木偶一般语无伦次。"
            gc "高越。"
            $ gy_face = "smile"
            gy "行了水放这就好。谢谢你们啦～"
            $ gy_face = "normal"

        "…你们是来找我的？": 
            $ resonance += 2 
            $ control -= 1.5 
            "她们说话颠三倒四，动作并不自然，提线木偶一般语无伦次。"
            "高超一面觉得诡异，但仍然掩不住高兴。高越在后面起哄地吹口哨，而高超接过水，按着高越的背，一起道谢。女孩们把水递给高超，害羞地逃走了。"
            $ gy_face = "smile"
            $ gc_face = "smile"
            gy "好有人气呀～高超～我都有点嫉妒了。" 
            gc "你嫉妒的是谁？我，还是她们。"
            $ gc_face = "normal"
            $ gy_face = "normal"
            gy "……" 
        "找高越算账": 
            $ resonance -= 2 
            $ control += 3 
            "她们说话颠三倒四，动作并不自然，提线木偶一般语无伦次。高超脸色冷淡地道谢，接过其中一瓶水扔给高越。"
            gc "你想干嘛？" 
            gy "没想干嘛。不就是哄你高兴吗。"
            $ gc_face = "wuyu"
            $ gy_face = "smile"
            gc "特别蠢，高越。你做的这些都特别蠢。只有你想受欢迎。"
            gy "你对我也说谎呀？哪有中学生不想受欢迎。"
            $ gy_face = "normal"
            gy "你只是不想因为魔法受欢迎。" 
            gc "随你怎么说。"
            $ gc_face = "normal"
            gc "我不想再待在这里了。" 

    $ clear_narration()  
    $ show_narrator("高越叹口气，打了个响指。那两个女孩立刻回过神来，对自己出现在篮球场的事实感到困惑，转头看见高超高越的背影。") 
    pause 

    $ show_narrator("两瓶瓶装水消失在空气里，像从没出现过一样。") 
    pause 

    $ show_narrator("高越跟在高超后面，两人两手空空地离开了篮球场。") 
    pause

    stop music fadeout(2.5)
    hide screen narration_screen
    $ clear_narration()

    # 进入游泳馆场景 
    jump swimming

label rooftop:
    scene bg rooftop1:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(3)
    

    $ show_narrator("高越略施了个小法术，天台的铁门锁应声落地，像拧开一个饮料瓶一般，高越轻松推开了厚重的铁门。高超跟在他后面，逐步踏上台阶，进入天台。") 
    pause

    play music soft fadein(0.5)

    $ show_narrator("高处有习习夏风。站在天台上，能清楚看到下面的一切：对面教学楼里正在摇头晃脑读书的三年级，楼下运动场里三三两两散步的学生。天台栏杆上还刻了字，隐约能看出，是一些\"不想再学了！！\"\"备战高考！\"之类零碎的句子。") 
    pause 

    $ show_narrator("高越也不顾裤子会不会脏，一屁股坐在地上。高超吐槽他两句，很快从善如流，跟着坐在地板上。水泥地凉凉的，高超的心也跟着宁静下来，甚至有点昏昏欲睡。") 
    pause 

    gy "你看，那儿有人在打篮球呢。" 
    gc "我看看...打得挺菜的。"
    $ gy_face = "smile"
    gy "哈哈哈。难道我们就打得很好"
    $ gy_face = "normal"
    $ gc_face = "wuyu"
    gc "啧"
    $ gc_face = "normal"

    $ clear_narration()  
    $ show_narrator("无意义的闲聊。虚度的时光。好奢侈的幸福…高超索性躺在水泥地上，看天上云卷云舒。他好久没有这么放松的时候了，什么也不想，只是和高越一起，呆在一个空旷的地方，享受着时间缝隙的休憩。像偷来的一点松弛甜蜜。而高越还撑着上半身，在那儿看人打篮球。") 
    pause 

    $ show_narrator("楼下那几个男生他见过。二年级的学长，都是很受欢迎的风云人物，其中不乏在星期一升旗时频繁见过的年级、班级代表。他忽然想起了什么，转头问高超。") 
    pause 

    gy "高超，你小学的时候也当过大队长" 
    gc "你也当过。当过一天"

    $ gy_face = "smile"
    gy "我就是觉得新鲜。觉得这官高超当得我当不得？"
    $ gy_face = "normal"

    gy "不过，那都是过去的事了…" 
    gc "嗯。" 
    gy "你又装成熟。还是真成熟了？有时候我觉得，你长大得太快了。我受不了"

    $ gc_face = "wuyu"
    gc "……"
    $ gc_face = "normal"

    $ clear_narration()  

    $ show_narrator("他说不出口。") 
    pause 

    $ show_narrator("说不出口我也接受不了。既接受不了长大，也接受不了和高越不再时时刻刻黏在一起。长大就意味着分开吗？真无聊，这个推断式子。他感到一切都无聊透顶，却不知道是不是因为高越缺席。") 
    pause 

    $ show_narrator("高越看他那么伤心，忽然也躺下来。水泥地太硬，他痛得直叫唤。吵死了，高超翻过身去捂住他的嘴。捂得太紧了，高越呼吸都困难，恶作剧一般，他伸出舌头舔了一下哥的手心。") 
    pause

    play music aimei fadein 2.0

    $ show_narrator("高超甩开手，吓得立刻坐了起来。") 
    pause

    hide screen narration_screen

    # 分支10选项 
    menu: 
        "慌不择路地吐槽": 
            $ resonance -= 0.5
            $ control += 2
            $ gc_face = "wuyu"
            gc "你有病吧，高越。为了恶心我，你现在真是无所不用其极了"
            $ gc_face = "normal"
            $ gy_face = "surprise"
            gy "你觉得是恶心？"
            $ gy_face = "normal"
            gc "…我不是那个意思" 
            gy "这才哪到哪呢。"

        "假装无事发生": 
            $ resonance -= 2 
            $ control += 3 
            "两相沉默。直到高超不自然地把手心在地板上蹭了又蹭。"
            "蹭破皮了。高越翻开他手心，小心地吹气。"

        "这是你自己送上门来的": 
            $ resonance += 3 
            $ control += 2
            $ gc_face = "smile"
            $ gy_face = "xinxu"
            gc "这是你自己送上门来的" 
            gy "什么意思啊高超。我听不懂" 
            gc "装傻是吧。"
            $ gc_face = "normal"
            $ gc_face = "normal"
    $ clear_narration()
    $ show_narrator("高超把他拽起来。捧着高越的脸，拼命地揉搓，越揉搓越觉得牙痒痒，手上不自觉地下了狠力气。高越脸都给捏红了，吱哇乱叫着，鱼一般挣扎扑腾。") 
    pause 

    $ show_narrator("高超忽然松开手，大笑起来。高越揉着脸颊看他笑，刚想吐槽，竟也不自觉地跟着笑了起来。而高越反过来捧着他的脸，轻轻印了一吻。") 
    pause

    $ gy_face = "smile"
    gy "我早就想这样干了。" 
    $ gy_face = "normal"

    $ show_narrator("时间凝滞在此刻。") 
    pause

    $ clear_narration()

    $ show_narrator("这吻如此轻柔…鬼使神差般，高超捧回高越的脸，还回去一个深重得多的吻。他把舌头探进高越口腔，扫尽里面一切气味。高越的津液顺着交缠的舌头，落到他舌尖。并没有什么深刻的味道。可高超有点晕眩了。") 
    pause

    stop music
    stop sound

    $ show_narrator("{b}一个羽毛球飞到高超眼前。直直插进高越衣领。{/b}") 
    pause 

    $ gy_face = "surprise"
    gy "谁啊！"
    $ gy_face = "normal"

    play sound laugh fadeout 2.0
    $ show_narrator("高越不耐烦地叫出了声。两人低头看去，才发现教学楼下面挤满了人。人们脸上挂着绝不能称之为善意的笑容。其中一个男孩儿扛着羽毛球拍，做着手掏来掏去的动作，笑嘻嘻地让高超帮他好弟弟把球拿出来。还要打球呢。") 
    pause

    $ clear_narration()
    play music horror

    scene bg rooftop2:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 

    $ show_narrator("高超背又濡湿了，耳边轰鸣如雷，随着同学的嗤笑一声声落地。他感到自己被撕裂的不仅是免疫系统，还有整个轮廓。像平白被撕去一页纸，高超整个人惨白而空无。怎么办、怎么办、怎么办……") 
    pause 

    $ show_narrator("高越紧紧握着他冰凉的手。力道大到高超手心都痛。痛觉给他安心。")
    gy "哥，你想怎么办？"
    pause

    hide screen narration_screen
    # 分支11选项 
    menu: 
        "消除他们的记忆": 
            $ resonance += 1.5 
            $ control -= 2
        "消除他们": 
            $ resonance += 2 
            $ control -= 3
        "我不知道…": 
            $ resonance -= 2 
            $ control += 2 

    $ show_narrator("高越又拿起他的玉桂狗魔法棒。他紧张得出一头汗，这样比划，那样比划，楼底的人仍在嗤笑，三层楼的高度，也不能完全阻隔这笑声。") 
    pause 

    $ show_narrator("高越狠下心，把声音屏蔽了。那些学生嘴巴闭紧，眼睛仍是笑着的。原来笑可以是这样不怀好意的表情。") 
    pause 

    $ gy_face = "xinxu"

    gy "没用。魔法没用。人还是太多了…"

    $ gc_face = "fear"
    gc "……………………………………"
    $ gc_face = "normal"
    $ gy_face = "normal"

    $ clear_narration()  
    $ show_narrator("他已经完全听不见声音了。情急之下，高越拉着他往外跑。曾经轻如纸片的大门，现在却花了他很大力气才能推开。高超神情恍惚，被高越拉着，缓缓离开天台。夏风习习，凉丝丝的风钻进他的衣领，而他陷入一种巨大的错愕…") 
    pause 

    $ show_narrator("他们逃得太狼狈。没人发现楼下嗤笑的学生很快离开了。落进衣领的羽毛球顺着衬衫下摆滑向地面，因恶意而聚拢的人群也四散分开，在回到原本应有位置的路程中，他们身体透明，表情淡去，直至完全消失。") 
    pause
    
    hide screen narration_screen
    menu: 
        "躲进天文台": 
            $ clear_fullscreen_narration()
            $ clear_narration()     
            stop music fadeout(2.0)
            jump observatory

label swimming: 
    scene bg swimming1:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(3)
    play sound pool_shower
    play music swimpool fadein(2.0)

    $ show_narrator("高超上学期的同桌是个外地来的男孩儿。那学期就有游泳课，他问高超，你会游泳吗。高超说咱们这里是青岛。他说，所以你们都会游泳？高超说嗯对。") 
    pause 

    $ show_narrator("他忽然想起小时候和高越一起爬长城，公交上的大爷逗他们，两个大胖小子哪儿来的呀。高越抢在他前面回答，用家乡话说青岛的。那你们都可会吃海鲜了，可会游泳了，对吧？高越重重点头，说对，不会游泳的话，会死掉的。") 
    pause 

    $ show_narrator("游泳馆里的水不像海水，是那种死物的蓝绿色，冒着消毒水味。海是生机勃勃的。白色的浪，胡乱的风，还有规律的潮汐。而游泳池只是一大块凝固的蓝绿色透明水彩颜料。") 
    pause 

    $ clear_narration()

    $ show_narrator("高超坐在泳池边发呆。外地同学问他你们都会游泳吗？他那时学着高越的语气，说，不然就会死掉。那人的脸很古怪地抽动一下，扑哧一下笑了。他说高超，你真挺幽默的，幽默得都有点不像你了。") 
    pause

    play sound pool_swim

    $ show_narrator("高越在游泳池里游了两个来回，忽然从水里钻出来，小海豹似地挺直上身，拱到忧郁的高超前头。") 
    pause

    $ gy_face = "xinxu"
    gy "高超，你消气了吗？"
    $ gy_face = "normal"

    $ clear_narration()  
    # 分支12选项 
    menu: 
        "我不和狗生气": 
            $ resonance += 2 
            $ control += 0.5
            $ gy_face = "surprise"
            $ gc_face = "smile"
            gy "？说谁狗呢" 
            gc "狗装傻。" 
            gy "我靠！高超！！" 
            gc "狗破防。"
            $ gy_face = "normal"
            $ gc_face = "normal"

            "欣赏完高越气急败坏的模样，高超满意地跳下水来，试图游开，却被高越追上拉住。高越牵着他，不让他两脚落地，只能浮在水中。两人逐渐往泳池中心走去。"
        "你知道我不喜欢那样…": 
            $ resonance += 3 
            $ control -= 1.5
            $ gy_face = "xinxu"
            $ gc_face = "smile"
            gy "对不起嘛。我就是想试试看。也有逗你开心的意思" 
            gc "你是想逗我开心，还是试探？"
            $ gy_face = "normal"
            $ gc_face = "normal"
            gy "...你知道答案。" 
            "高越趁高超出神，忽然把高超拉下泳池。水花四溅，高超下意识在水里寻找浮板，无奈之下只能握住高越的双手。而高越牵着他，不让他两脚落地，只能浮在水中。两人逐渐往泳池中心走去。"
        "不理会": 
            $ resonance -= 2 
            $ control += 2 
            gy "行。我们就这样不看彼此的眼睛吗！"
            $ gc_face = "wuyu"
            gc "别说恶心话。" 
            gy "不再说你爱我吗。"
            $ gc_face = "fear"
            gc "我说了别说恶心话！！！"
            $ gc_face = "normal"
            "高越趁高超出神，忽然把高超拉下泳池。水花四溅，高超下意识在水里寻找浮板，无奈之下只能握住高越的双手。而高越牵着他，不让他两脚落地，只能浮在水中。两人逐渐往泳池中心走去。"
    play sound jumpwater
    scene bg swimming2:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(0.5)

    $ show_narrator("进门前，高越施法让他俩都干爽而精神百倍地走进游泳馆。他说想游泳，要让高超陪——其实高超知道，这是高越哄他的一种比较曲折的方式。") 
    pause 

    $ show_narrator("他们两个里高越是水性更好的那个，但高超喜欢游泳。高越总说他浑身肉都蓬松，一进水里就像救生圈一样浮起来，回回都被哥哥扇巴掌。") 
    pause 

    $ show_narrator("两人手牵手，浮在游泳池中间。高越在水中挥动他的魔法棒，小小的泳池面积忽然扩大无数倍，从一小块蓝绿色玻璃，变成一个真正的死去的海。") 
    pause

    $ clear_narration()

    stop music fadeout 4.0

    $ show_narrator("没有潮汐，没有海风，只有纹丝不动的水面，和水中央两个手牵手的小小人儿。") 
    pause 

    $ show_narrator("交换过眼神后，两人吸了很大一口气，高越拉着高超的手一路下潜。游泳池深不见底，越往下光线越暗。高超忽然害怕起来。") 
    pause

    scene bg swimming3:
        zoom 1.5
        xalign 0.5 
        yalign 0.5

    play music swim_horror

    $ show_narrator("他有种可怕的预感。在这池无风无浪的水里，他和高越之间的边界正在逐渐消失。高超低下头，恍惚间看见自己的皮肤正在逐渐融化，高越的也是。") 
    pause

    $ clear_narration()  

    $ show_narrator("他们的皮肉缓慢相连，神经也像电路一样搭在一起，最终变成一滩共有的器官。") 
    pause

    $ show_narrator("高超和高越不再是分别的两个人，而是真正的1.5个人。他们会变成连体婴，然后永不分离。如果能就这样手脚相连地活下去…") 
    pause 

    gy "哥，你感觉到了吗？"

    hide screen narration_screen

    # 分支13选项 
    menu: 
        "停下！": 
            $ resonance -= 2 
            $ control += 3
        "……嗯": 
            $ resonance += 1.5 
            $ control -= 2.5 
        "……继续。": 
            $ resonance += 3
            $ control -= 2

    stop music
    play sound jumpwater

    "高超忽然惊醒。"

    "高越还是像小海豹一样游到他面前。这次他头上没有顶着皮球，却献宝一般游到高超前头，眼睛亮晶晶的，雀跃地等候高超的夸奖。"

    $ gc_face = "fear"
    gc "刚刚是梦吗？"
    $ gy_face = "smile"
    gy "不全是。我尝试了一点新东西。不过我看你快吓死了，就提前结束了。"
    $ gc_face = "normal"
    $ gy_face = "normal"
    gc "……" 
    gy "你觉得它是个梦吗？" 
    gc "我希望它只是个梦。"

    $ clear_narration()  

    $ show_narrator("高越脸上总是挂着的盈盈笑意消失了。他的发丝还滴着水，黑色的眼珠直直盯着高超，脸上没有任何表情。") 
    pause 

    $ show_narrator("这是高超最害怕的那一面：完全诚实，没有修饰的高越。") 
    pause 

    $ show_narrator("高超抵不过他的直视，主动跳下来，拉着高越贴近泳池底。白色瓷砖映照在两人脸上，如真正的波光一般，而高超在水底和高越交换了一口氧气。他睁开眼，在水里望着高越无知无觉的脸。") 
    pause 

    $ show_narrator("那眼睛里如实地写满了渴望。") 
    pause

    $ clear_narration()

    "熟悉的恐惧席卷而来。他们的嘴唇不顾水的阻挠，紧密相连，唇舌混着消毒水味的池水，在对方口腔里搅拌。太恐怖了，高超打了个寒战，而高越笑着把他拉上岸。"

    gy "擦干净身体再换衣服吧，晚上我还想带你看点新东西呢。"
    $ gc_face = "wuyu"
    gc "嗯…"
    $ gc_face = "normal"

    play sound pool_swim
    "他惊魂未定，在岸边喘着气，而高越不知疲倦一般，又跳进水里，欢快地游了起来…"

    menu: 
        "进入天文台": 
            $ clear_fullscreen_narration()
            jump observatory

label observatory:

    scene bg observatory:
        zoom 1.5
        xalign 0.5 
        yalign 0.5 
    with Dissolve(0.5)
    play music universe

    $ show_narrator("学校的天文台于十年前修建完成。说是天文台，也只是有一个投影室，和一架放在投影室顶上小天台的天文望远镜。") 
    pause 

    $ show_narrator("十年前陆续有飞船上天的新闻。人们对宇宙充满憧憬，连带着天文学也热门起来。学校领了经费，要建设省里的天文教授示范校。") 
    pause 

    $ show_narrator("五六年后，天文学的热度很快过去，天文台里的设施也年久失修，只能看到一些疑似星星的发光物体。也许是飞机，也许是星星。没有指导教师的帮忙，学生们无法鉴定看到的究竟是什么。") 
    pause 

    $ show_narrator("仿照世界上最著名的天文台格里菲斯，本校的天文台也建了投影室，圆形穹顶，可容纳一百人以上。") 
    pause

    $ clear_narration()  

    $ show_narrator("高超偶尔逃课来这里睡觉。撬开生锈的门锁，随意找一个舒服的位置，坐下，让背在柔软椅背支撑下逐渐倾倒。") 
    pause

    scene bg starsky: 
        zoom 1.5 
        xalign 0.5 
        yalign 0.5 
    with fade

    $ show_narrator("穹顶上是漆黑一片——投影已经坏了很久。")
    pause 

    $ show_narrator("此时此刻，高超出神地望着眼前的圆形投影。听不懂的英文台词讲述着宇宙大爆炸的故事：从混沌的星团，逐渐演变为广袤的宇宙。古代人如何靠星座辨别方位，又是怎么在星空下讲故事…") 
    pause 

    $ show_narrator("高超的眼睛直直盯着一片黑暗里闪耀的星空演出。他听不明白，只感到一种混沌的感动，转头看高越，睡得四仰八叉，口水在投影映射下闪闪发亮。他无奈地推醒高越。") 
    pause

    $ clear_narration()

    $ gc_face = "wuyu"
    gc "醒醒，醒醒。"
    $ gc_face = "normal"
    gc "你不看吗？" 
    gy "…嗯？你喜欢星星呀。" 
    gc "一般喜欢。" 
    gy "不喜欢我就关掉了。" 
    gc "别啊。"
    $ gy_face = "smile"
    gy "嘿嘿。"


    $ show_narrator("他的魔法仍在小小地运作。让十年未曾打开的投影重新工作，也不是什么困难的事。他盘算着更大的计划。被高超推醒后，他就一直盯着高超的眼睛。顺着那道并不明显，却很炙热的视线望去，是双子座的位置。") 
    pause 

    gy "哦～" 
    $ gy_face = "normal"

    $ show_narrator("然后高超反复看了五遍双子座的故事。播到第六遍时，高超叹口气，有些无奈地开口。") 
    pause 

    gc "你想说什么，高越" 
    gy "不看了吗？" 
    gc "……" 

    $ show_narrator("高越挥挥手，穹顶忽然消失。两人像坐在真实的星空里，周围群星璀璨，而高超高越坐在投影室顶楼的小天台。") 
    pause 

    gc "你的魔法是不是强了不少？白天还只能做一些小型恶作剧什么的。现在就能制造这种程度的幻术了…" 
    $ gy_face = "smile"
    gy "不一定是幻术啊。也可能真的进入宇宙了呢。你想象力还是匮乏。" 
    $ gy_face = "normal"
    $ clear_narration()

    # 根据不同路线显示不同文本

    if current_route == "basket":
        "如果只是幻术就好了。想到游泳池里逐渐模糊的肌肤边界，高超忍不住打了个寒战。"
    if current_route == "music":
        "…可惜再强也有做不到的事。想到方才天台里发生的一切，高超忍不住打了个寒战。"

    gy "但你说得没错，我的魔力确实变强了。现在我可以做更多事了。而这好像和你有关。"
    $ gy_face = "smile"
    gy "我有一种感觉。这个魔力是用来帮助你的。只要你想，我就能帮你实现。" 
    gy "而你的感受越是深刻，你的愿望越是强烈，魔法的效力就越强。" 

    # 根据不同路线显示不同文本
    if current_route == "basket":
        "…所以那也是我的愿望吗。两个人融合成一个，不再分开。高超觉得自己越来越不明白这个所谓的魔法，还有自己之间的关联。"
    if current_route == "music":
        "那为什么消除记忆的法术会失败？高超觉得自己越来越不明白这个所谓的魔法，究竟是什么运行机制。"
    gy "既然如此，我有个模糊的愿望…也可以看成一个选项。反正都选了那么多个分支，这个也一样吧？" 
    $ gy_face = "normal"
    gy "请听题：高中生高超更想要实现的是哪一种呢？"

    stop music fadeout 2.0
    play music horror fadein 2.0
    jump branch_14

# 分支14
label branch_14:
    $ option1_text = "让学校消失"
    $ option2_text = "让高超高越融合"
    
    # 如果真结局未通关，生成乱码文本
    if not persistent.true_ending_unlocked:
        $ option1_text = generate_corrupted_text("让学校彻底消失")
        $ option2_text = generate_corrupted_text("让高超高越彻底融合")
        
        # 检查乱码选项是否已达10次
        if branch_14_loop_count >= 10:
            gc "已经10次了。还是放弃吧……"
            menu:
                "不可以！":
                    $ gc_face = "fear"
                    gc "都太极端了吧！绝对不行"
                    gy "哦哦…我就知道你会这么说。"
                    jump branch_14_after
    
    menu:
        # 选项1
        "[option1_text]":
            if persistent.true_ending_unlocked:
                gy "明白了。那就如你所愿。"
                $ branch_choice = "destroy_school"
                jump ending_b
            else:
                # 未解锁时的反馈
                $ gc_face = "wuyu"
                gc "...看不懂在说什么。"
                $ gc_face = "normal"
                jump branch_14_return
        
        # 选项2
        "[option2_text]":
            if persistent.true_ending_unlocked:
                gy "明白了。那就如你所愿。"
                $ branch_choice = "merge_twins"
                jump ending_b
            else:
                $ gc_face = "wuyu"
                gc "...无法理解含义。"
                $ gc_face = "normal"
                jump branch_14_return
        
        # 选项3（始终可用）
        "不可以！":
            $ gc_face = "fear"
            gc "都太极端了吧！绝对不行"
            gy "哦哦…我就知道你会这么说。"
            jump branch_14_after
    
label branch_14_return:
    $ branch_14_loop_count += 1
    jump branch_14

label branch_14_after:
    gy "那不如，把这两个选项也融合一下吧。比如说…" 
    gy "把你在的3班和我在的7班，彻底融合成同一个班级。" 
    gc "…什么意思" 
    gy "很简单啊。就是你以外的同学，和我以外的同学，两两合并，最终变成一个人。" 
    gc "…" 

    $ show_narrator("高越怕他听不懂似的，挥挥手，出现两个陌生的同学。一个是高超的同学，另一个不怎么眼熟，只依稀有点印象，想必就是高越的同学了。") 
    pause 

    $ show_narrator("那两个人距离逐渐靠近，直到彼此都失去一半的自己。几道巨大的、发光的虚线针脚，将两个影子缝在了一起，变成诡异的一个整体。") 
    pause

    $ gy_face = "smile"
    gy "像这样。大家就都变成双胞胎了。" 
    gy "别人也能理解我们了。" 
    gy "…我们也能一直在一起。一直一直，黏在一起。"
    $ gy_face = "normal"
    gy "只要大家都是连体婴，就不会有人觉得双胞胎是异类了吧。" 
    gc "………………" 
    gy "而且我们又能一起上学了。一起交朋友，被人认错，被一起叫到办公室。你干坏事时，我也陪着你。高超，你再也不会孤独了。我们也不会被别人误解了。"
    gy "很奇怪吧，明明百分之零点三不是那么低的概率，人们为什么都把双胞胎当动物园里的猴子呢。" 
    gy "社会真的有那么重要吗?为了这个理由，就要拆散我们吗。" 
    gy "…………我一直都很想高越。很想很想…" 
    gc "真正的高越哪里去了?" 
    gy "那不重要。重要的是，你觉得我的提议怎么样?"

    scene bg starsky2: 
        zoom 1.5 
        xalign 0.5 
        yalign 0.5 
    with fade

    $ clear_narration()
    $ show_narrator("像蛋花汤一样，流体的星空飞速旋转起来。") 
    pause 

    $ show_narrator("某处的两个明亮的光点融合，变成更亮的光点；又或者是某个星团分裂成了两半。") 
    pause 

    $ show_narrator("高超觉得不妙，拼命挥手，想让星空的幻术消失。") 
    pause 

    $ show_narrator("撕裂一般的光亮后，目之所及的是真实的学校：路灯照耀下，夜晚的学校教学楼正如有生命的怪物。其中一栋，高超认得就是他们的高一教学楼。") 
    pause

    play sound destroy

    $ show_narrator("像被撕裂一般，和另一半拼凑在一起。中间的部分陡然消失，教学楼变成细窄的长条，摇摇欲坠地立在学校一侧，像踩着高跷的小丑。") 
    pause 

    hide screen narration_screen
    $ clear_narration()
    # 分支15选项 
    menu: 
        "快停下！！！": 
            $ resonance -= 1
            $ control += 1
        "……不要这样……": 
            $ resonance += 1
            $ control -= 1

    gc "高越在哪里？把高越还给我。" 
    gy "这重要吗？"
    gc "非常重要。" 
    gy "好吧……高越，或者说完整的高越，就在结局等着你。做好准备，迎接被囚禁的公主了吗？" 
    gy "真实并不一定就是美好。即使丑恶，恶劣到自己都无法接受，你也要走入真实吗。" 
    gc "…我要见到高越。我得找到高越。" 
    gc "高越…………………………………………"
    $ gc_face = "normal"

    hide screen narration_screen
    pause 1.5

    # 关掉数值体现的底图
    $ show_value_ui = False

    # 结局判断逻辑 
    $ total = resonance + control 
    $ diff = resonance - control 
    $ ratio = abs(diff / total) if total > 0 else 0

    $ gc_face = "normal"
    $ gy_face = "normal"

    # 为a线补偿1数值
    if current_route == "music":
        $ total += 1.0

    if total < 13: 
        jump ending_d 
    elif total >= 17 and abs(diff) <= 3.5: 
        jump true_ending 
    elif diff > 7: 
        jump ending_b 
    elif diff < -7: 
        jump ending_c 
    else: 
        jump ending_a

label ending_a:
    $ persistent.ending_A = True
    stop music fadeout(2.0)
    scene black with None
    
    $ show_fullscreen_narrator("漆黑的走廊。什么也看不见。") 
    with Dissolve(2.0)
    pause

    $ show_fullscreen_narrator("高超只能在黑暗里独自行走。黑暗尽头，有一个穿着蓝色校服的人，落寞地蹲在原地。") 
    with Dissolve(2.0)
    pause

    $ show_fullscreen_narrator("高越抬起头，慢慢站起来，平静地看着他。") 
    with Dissolve(2.0)
    pause

    play music soft fadein 2.0
    gy "…你不说些什么吗？" 
    gc "你是谁。" 
    gy "我是高越啊，我还能是谁。"

    $ gc_face = "wuyu"
    gc "那刚刚那些是谁。魔法，恶作剧，混乱的人群，还有学校和融合的同学…"
    $ gc_face = "normal"

    gy "那是你，也是高越。我们本来就是同一个人嘛。" 
    gc "我不明白。" 
    gy "这有什么不明白呀！你的感觉就是我的感觉。大部分时候。绝大部分时候？" 
    gy "就像我们小学门口卖的那种三色冰淇淋。融化又冻上，三个颜色就会混在一起。你，我，你的愿望…欲望。混在一起，组成了那个有魔法的高越。" 
    $ gy_face = "smile"
    gy "没关系。我一直看着你呢，就像你总是看着我一样。看着我不让我干坏事。我也看着你。毕竟你这么不让人省心！" 
    $ gy_face = "normal"
    $ gc_face = "wuyu"
    gc "......一切都结束了吗？"
    $ gc_face = "normal"
    gy "这要问你自己了。" 

    $ clear_fullscreen_narration()
    $ show_fullscreen_narrator("想要毁坏学校的欲望。想要和弟弟永远在一起的欲望。想要在人群里安全生活下去的欲望…想要和弟弟永远不分开的妄想…在这些愿望彻底满足之前，魔法永远不会消失。") 
    with Dissolve(2.0)
    pause

    $ show_fullscreen_narrator("高超叹口气，轻轻搂着高越。像不太熟悉他迟来的坦率，高越挣扎了两下。力气太小，没挣扎成功，高越轻轻回抱高超，让他把脑袋搁在自己颈窝。") 
    with Dissolve(2.0)
    pause

    $ show_fullscreen_narrator("高超轻轻地抽噎。高越安抚地拍着他的背，再说不出揶揄的话了。") 
    with Dissolve(2.0)
    pause

    $ gc_face = "wuyu"
    gc "你都知道了。"
    $ gc_face = "normal"

    gy "毕竟我们是双胞胎嘛。" 
    gy "没关系。因为我也不习惯。虽然没你那么痛苦。" 
    gc "？"

    $ gy_face = "smile"
    gy "哈哈哈哈哈哈"
    $ gy_face = "normal"

    gy "没关系。长大以后的世界我也害怕。" 
    gy "我也…我也不想和你分开。" 

    $ clear_fullscreen_narration()
    $ show_fullscreen_narrator("太肉麻了。两个人的鸡皮疙瘩都掉了一地。而高超紧紧搂着弟弟，再恶心也顾不上了。反正也没有人在看，不是吗。") 
    with Dissolve(2.0)

    gy "没关系。没关系。不管怎么选，我都会陪着你的。" 
    gy "从梦里醒来吧，高超。" 

    $ show_fullscreen_narrator("外面的现实仍然混沌，但也坚不可摧。") 
    with Dissolve(2.0)
    pause

    $ show_fullscreen_narrator("或许这才是真正的真实。夹在现实和虚幻之间。用现实验证虚幻，同时也用虚幻遮盖无法接受的那部分现实。闭上眼睛，深吸一口气，然后再睁开吧。毕竟无论如何，身边都有高越。那就没有什么好怕的了。") 
    with Dissolve(2.0)
    pause

    $ show_fullscreen_narrator("高超在高越怀里沉沉睡去，从整个噩梦里缓缓醒来…\n\n") 
    with Dissolve(2.0)

    stop music fadeout 4.0
    pause 2.0

    $ clear_fullscreen_narration()
    play sound bonus

    $ show_fullscreen_narrator(
    "{size=+5}{b}{cps=8}{color=#eeddcc}恭喜您解锁【结局A：平稳的收场】{/color}{/b}{/size}"
    "{cps=6}{color=#ddccbb}（一般结局，数值相对平衡）{/color}")
    with Dissolve(2.0)
    pause

    call check_all_endings from _call_check_all_endings # 检查是否集齐

    return

label ending_b:
    $ persistent.ending_B = True
    $ show_value_ui = None
    scene black
    with None
    stop music fadeout(2.0)

    $ show_fullscreen_narrator("漆黑的走廊。什么也看不见。高超只能在黑暗里独自行走。走到快要哭出声的时候，他终于到了尽头。") 
    pause 2.0

    $ show_fullscreen_narrator("高越站在那里，跃跃欲试地看着他。") 
    pause 2.0

    $ show_fullscreen_narrator("高超狠狠把高越抱进怀里。眼泪落到嘴角。咸咸的，是最伤心、最害怕的味道，而高超为此感到安心。高越挥挥手，他们离开漆黑的走廊，又回到天文台楼顶。") 
    pause 2.0

    play music endingb

    if branch_choice == "destroy_school":
        $ show_fullscreen_narrator("学校顷刻间毁灭。大楼被摧毁，栏杆被折断，像龙卷风席卷过后，一切化为乌有。")
        pause 2.0
        
    elif branch_choice == "merge_twins":
        $ show_fullscreen_narrator("人们开始融合...像橙汁海一样。学生的身体融化成的海洋之上，高超高越身体相连，安然无恙地漂浮其中。")
        pause 2.0
    
    else:
        # branch_choice 为 None 时走这里
        $ show_fullscreen_narrator("教学楼恢复原样。校园一片漆黑，没人发现有一对兄弟在楼顶接吻。")
        pause 2.0

    # 后面接共有的结局演出或黑屏

    $ show_fullscreen_narrator("高越的吻令人目眩神迷，而高超无力地坠入其中，顾不上学校，更顾不上自己了。高越微微抬手，所有的路灯和教学楼的灯都打开。整个校园忽然间灯火通明。在万千人造星体见证下，高超和高越跨越兄弟关系，要完成关系融合真正的最后一步。") 
    pause

    gy "你不好奇吗。高超。咱俩这双胞胎兄弟的关系，再往前走，会是什么？"
    $ gc_face = "wuyu"
    gc "……"
    $ gc_face = "normal"
    gy "这是你亲手选择的未来呀。可你甚至说不出口…" 

    $ clear_fullscreen_narration()
    $ show_fullscreen_narrator("恋人。情人。爱人。\n\n") 
    pause 1.0
    $ show_fullscreen_narrator("献出我自己…这就是我能给出的一切。\n")
    pause 1.0

    gy "我不要上学了。你也不要上学了。"
    $ gy_face = "smile"
    gy "我们想做什么做什么吧。高超。"
    $ gy_face = "normal"
    gy "谁也不能再把我们分开。包括你自己。" 

    $ show_fullscreen_narrator("狂风骤雨的吻里，高超献出了一切，包括身为兄长的教习、束缚，还有道德伦理。") 
    $ renpy.with_statement(Dissolve(3.0))
    pause

    $ show_fullscreen_narrator("短暂的光明后，所有的灯都黯淡下去，整座校园恢复为沉默的漆黑。") 
    $ renpy.with_statement(Dissolve(3.0))
    pause

    $ show_fullscreen_narrator("不再需要什么魔法了。在终止一般的绝对寂静里，只有两人纠缠的呼吸与体温。") 
    $ renpy.with_statement(Dissolve(3.0))
    pause

    $ show_fullscreen_narrator("时间在这里失去意义。高超和高越，最终成为这座废弃乐园里最后的孩童。\n\n") 
    $ renpy.with_statement(Dissolve(3.0))
    pause

    stop music fadeout 4.0
    pause 2.0

    $ clear_fullscreen_narration()
    play sound bonus

    $ show_fullscreen_narrator(
        "{cps=8}{color=#ff5555}恭喜您解锁【结局B：溺爱的深渊】{/color}\n")

    $ show_fullscreen_narrator(
        "{cps=6}{color=#ff8888}（高共鸣，低掌控结局）{/color}")
    $ renpy.with_statement(Dissolve(3.0))
    pause

    stop music fadeout(3.0)

    call check_all_endings from _call_check_all_endings_1 # 检查是否集齐

    return

label ending_c:
    $ persistent.ending_C = True
    stop music fadeout(2.0)
    scene black
    with None
    $ show_fullscreen_narrator("漆黑的走廊。什么也看不见。高超在黑暗里静静地独自行走。\n") 
    pause 

    $ show_fullscreen_narrator("高越站在走廊尽头，有些警惕而疏离地远远盯着他。冷白光打在他脸上，显得很幽怨。\n") 
    pause 

    $ gy_face = "surprise"
    gy "你满意了吗？" 
    gc "关于什么。" 
    gy "是你把我推开了。" 
    gc "…高越，你得明白一件事。那就是我们不可能永远做小孩子。"
    $ gc_face = "wuyu"
    gc "牺牲无法避免。重要的不是什么关系，而是我们得一直在一起。"
    $ gc_face = "normal"
    $ gy_face = "xinxu"
    gy "那和单胞胎有什么区别。" 
    gc "单胞胎是不会一直一直在一起的。" 
    gy "我不想这样…"
    $ gy_face = "normal"
    gy "但我没有选择，对吗？" 

    play music sad fadein(2.0)

    $ show_fullscreen_narrator("回答不言自明了。高越叹口气，把那根孩子气的魔法棒从口袋里掏出来，放在高超手心。狂热的作乱的欲望被压抑，魔法失去动机，魔法棒很快变回了廉价幼稚的塑料文具。") 
    pause 

    $ show_fullscreen_narrator("高超盯着摁动笔上玉桂狗纯洁的笑脸，珍惜又遗憾地用手指抚摸那一刻小痣。") 
    pause

    $ clear_fullscreen_narration()  

    $ show_fullscreen_narrator("没过多久，两人身上穿着的校服逐渐淡去，变作衬衫和卫衣。时光飞逝，在他们接受自己已经长大的现实之前，学校就从生活里彻底消失了。") 
    with Dissolve(3.0)
    pause 

    $ show_fullscreen_narrator("曾经最让人痛恨的，封闭、压抑的儿童乐园，很快被更为严苛冷酷的工作单位取代。高超在本地找了一份高薪工作，朝九晚五，常需要应酬。") 
    with Dissolve(3.0)
    pause 

    $ show_fullscreen_narrator("爸妈对这份工作很满意。亲戚朋友也都羡慕高超的生活。某个周五晚上，高越去接喝得烂醉的高超。高超在回家的出租车上吐得昏天黑地。高越扶着他下车，昏黄路灯映照下，两人慢慢走在小区里。") 
    with Dissolve(3.0)
    pause 

    gy "这样不对，高超。你不能把自己折腾成这样。"
    $ gc_face = "wuyu"
    gc "魔法早就消失了。"
    $ gc_face = "normal"
    gy "就没存在过。高超，重要的不是你怎么想，而是怎么做。"

    $ clear_fullscreen_narration()  

    $ show_fullscreen_narrator("后来说了什么，高超也不记得了。大约就是一些辞掉工作去北京做喜剧之类的事。他心里隐隐松动，却还没有足够的勇气跳出现在的一切。") 
    pause 

    $ show_fullscreen_narrator("欲望从未消失，叛逆也并未真正清除。那种狂热的毁坏一切的青春欲望，逐渐被更为精细微妙的掌控取代。") 
    pause 

    $ show_fullscreen_narrator("他对高越的一切了如指掌，却又假装大度地看着他漫无目的地游荡。高越连续不回家的第三晚，高超梦见自己掐着高越的脖子，听胸口的呼吸声逐渐变得微弱。") 
    pause 

    $ gc_face = "fear"
    gc "不要离开。不要离开。不要离开…"
    $ gc_face = "normal"

    $ gy_face = "xinxu"
    gy "嗯…………………………"
    $ gy_face = "normal"

    $ show_fullscreen_narrator("高越的承诺声细弱地传来，却听不真切。") 
    pause 

    $ show_fullscreen_narrator("他对一切无计可施，只能装作满不在意，陪高超一同等待——等待一个或许永不会来的，所谓时机。") 
    pause 

    $ show_fullscreen_narrator("他知道高超心里仍有一团躁动的火焰，在低氧的空间里静静燃烧着，却不知道什么时候才能等到解脱的那一天…") 
    pause

    # 音乐淡出
    stop music fadeout 4.0
    pause 2.0

    $ clear_fullscreen_narration()
    play sound bonus

    $ show_fullscreen_narrator(
    "{cps=8}{color=#4488ff}恭喜您解锁【结局C：缓慢的窒息】{/color}\n"
    "{cps=6}{color=#88aaff}（高掌控，低共鸣结局）{/color}")
    pause

    stop music fadeout(3.0)

    call check_all_endings from _call_check_all_endings_2 # 检查是否集齐

    return 

label ending_d:
    $ persistent.ending_D = True
    scene black with None

    $ show_fullscreen_narrator("高超在黑暗里摸索，最终走到一处走廊的尽头，那里空无一人。没有高越，也没有狂气的魔法师。") 
    pause 

    $ show_fullscreen_narrator("只有一只玉桂狗圆珠笔，眼角含着泪一般，脸颊上还有一颗痣，孤零零地落在地板上。") 
    pause 

    $ show_fullscreen_narrator("魔法棒变回了五块钱一支的塑料文具，玉桂狗眼下的那颗痣则被高超颤抖的指尖蹭花了——本就只是高越随手点的水笔印，而不是胎记。") 
    pause 

    $ show_fullscreen_narrator("被囚禁的公主呢？高越呢？高超胡乱地寻找，却一无所获…") 
    pause

    $ clear_fullscreen_narration()
    play sound bonus
    $ show_fullscreen_narrator(
        "{cps=8}{color=#aaaaaa}恭喜您解锁【结局D：无力的黑暗】{/color}\n"
        "{cps=6}{color=#888888}（低共鸣，低掌控结局）{/color}")
    $ renpy.with_statement(Dissolve(3.0))

    stop music fadeout 4.0
    pause 2.0
    return 

label true_ending:
    # $ narrator = None
    # $ renpy.store.narrator = None
    # $ config.narrator = None

    # 解锁真结局
    $ persistent.true_ending_unlocked = True
    stop music fadeout 3.0
    scene black with None
    play music mirror

    $ show_narrator("漆黑的走廊。什么也看不见。")
    with Dissolve(3.0)
    pause 

    $ show_narrator("高超只能在黑暗里独自行走。黑暗尽头，有一个穿着蓝色校服的人，落寞地蹲在原地。") 
    with Dissolve(3.0)
    pause 

    $ show_narrator("高越抬起头，慢慢站起来，平静地看着他。")
    with Dissolve(3.0)
    pause 

    gc "一切都结束了吗？" 
    gy "这要问你自己了。" 
    gy "不管怎么选，我都会陪着你的。"
    $ gy_face = "smile"
    gy "从梦里醒来吧，高超。" 

    $ clear_narration()  
    $ show_narrator("外面的现实仍然混沌，但也坚不可摧。")
    with Dissolve(3.0)
    pause 

    $ show_narrator("或许这才是真正的真实。夹在现实和虚幻之间。用现实验证虚幻，同时也用虚幻遮盖无法接受的那部分现实。闭上眼睛，深吸一口气，然后再睁开吧。毕竟无论如何，身边都有高越。那就没有什么好怕的了。")
    with Dissolve(3.0)
    pause 

    $ show_narrator("高超在高越怀里沉沉睡去，从整个噩梦里缓缓醒来…")
    with Dissolve(3.0)
    pause

    $ clear_narration()

    scene bg true: 
        zoom 1.5 
        xalign 0.5 
        yalign 0.5 
    with Dissolve(2.0)

    $ show_narrator("…宛若溺水一般挣扎的清醒并未到来。在漆黑的意识走廊和清晰的现实之间，还有一片白色的夹层，宽广而扁平地存在着。") 
    with Dissolve(3.0)
    pause 

    $ show_narrator("高超席地而坐（这能称之为地吗？只是白色的底面），静静存在于这广袤无垠的纯白之地。高越蹲在他对面。他微微低下头，像不满于这个空间的狭窄。") 
    pause 

    gc "高越…？" 
    gy "你终于来了！等得我急死了。" 
    gc "…你都看到了？"
    $ gy_face = "normal"
    gy "嗯。" 

    $ clear_narration()
    $ show_narrator("这也没什么稀奇的。小时候他们就常常做同一个梦，前头高超刚梦见在南极洲找企鹅玩，后半程高越就加入其中，要高超和他一起骑在北极熊背上玩。科学家说，杏仁核往往在幼年高度发达，随着时间推移，它的活跃性下降。脑电波幅度也逐步减弱。大人就不那么容易沉溺于幻想。") 
    with Dissolve(1.0)
    pause  

    $ show_narrator("可是长大以后，高超高越再鲜少进入同一个梦。")
    with Dissolve(1.0)
    pause 

    gc "…你都看到了。你在哪里呢？"
    $ gy_face = "surprise"
    gy "不知道，感觉在看电影。一开始我在我自己兜里，后来我在楼梯上，一会儿变成天台的鸟，一会儿变成游泳池的瓷砖。高超，你真的做了个很长很复杂的梦啊！我都看累了。" 
    $ gc_face = "wuyu"
    gc "我没听懂。你能听懂自己说的话吗？组织好语言再说。" 
    gy "哎呀！"
    $ gy_face = "normal"
    gy "我是这个呀。"
    $ gc_face = "normal"

    $ clear_narration()
    $ show_narrator("他从校服口袋里掏出一根圆珠笔。塑料制的玉桂狗在中性笔顶上恬静地微笑着。魔法！麦吉克。高越说。要不是我，你能做那么多乱七八糟的坏事儿？") 
    with Dissolve(1.0)
    pause 

    $ show_narrator("…原来是这样。") 
    with Dissolve(1.0)
    pause 

    $ show_narrator("并没有预想中复杂广袤的真相。也和天体、世界、青春、校园、精神分析、哲学无关。拉康和大他者。结构性空位和淫秽性团结。自我和边界，他者和欲望。通通无关。") 
    with Dissolve(1.0)
    pause 

    $ clear_narration()
    $ show_narrator("参宿四只是一颗客观存在的星星而已，人类没有发现伴星的存在，也不影响那颗小行星静静围绕着主星千万年；魔法也只是梦境。事实上，捉弄老师需要亲力亲为，毁灭学校则需要进一步的规划。一般来说，学校是不会因为一个中学生的愿望毁灭的。") 
    with Dissolve(1.0)
    pause 

    $ show_narrator("一直以来的魔力来源，都只是高越本人而已。") 
    with Dissolve(1.0)
    pause 

    gc "…为什么？" 
    gy "因为这是你的愿望啊！你高兴，我也会高兴；你不高兴，我也受影响。所以说双胞胎这事儿邪乎。太麻烦。" 
    gy "也有我自己的心愿。当然了。谁喜欢上学？我巴不得天天出去玩。逃课，打篮球。不然我们直接去上网去也行…" 
    gc "高越！"
    $ gy_face = "xinxu"
    gy "行行行，知道了。不逃课。不上网。"
    $ gy_face = "normal" 

    $ clear_narration()
    $ show_narrator("高超叹口气，很挫败地低下头。这不是他想象中的那种结局。当然，它很安全，但也乏善可陈。不新鲜，不好玩，也没有现实面的许可。没有坏孩子的刺激，也没有好孩子的奖励。讨不到任何好处。一切都很乏味。") 
    with Dissolve(1.0)
    pause 

    $ show_narrator("高越看他不高兴，只好跟着叹口气。他不再蹲下，而是学着高超的样子坐下。他坐在地上缓慢地挪动，直到挪到高超身边。他从后面环住高超的背，手臂在高超胸前交汇。两人的心跳声逐渐重叠。这种回响让高超安心。") 
    with Dissolve(1.0)
    pause 

    gy "未来的事谁说得准呢！不如享受现在。" 
    gc "你是享乐主义分子。" 
    gy "听不懂。我只是觉得，和你在一起，我就很幸福。" 
    gy "…我想和你在一起。我们不是生下来就应该在一起的吗？一直一直在一起。"
    $ gy_face = "smile"
    gy "我不管别人的幸福是什么。我的幸福就是和你在一起。如果不是，幸福这个词也没意义了。那样的话，我不要幸福也可以。" 
    gy "你不看着我，会出很大问题的。"
    $ gy_face = "normal"
    gy "我想和你在一起…我得和你在一起。" 

    $ clear_narration()
    $ show_narrator("高超转过头来和他接吻。没人注视，没有隐喻。没有气息和味道，吻就只是吻而已。像贴在纯白页面上的拼贴画，没有意义，没有价值。没有原因，没有未来。吻让他们的食道相连，顺着食物的路径，消化，吸收，进入血液，回流到心脏。吻让连接穿透前胸后背的骨骼和肌肤，在流通中融为一体。") 
    with Dissolve(1.0)
    pause 

    $ show_narrator("嘴唇相触，纯白色的地面顷刻间被巨大的镜面取代。空间崩塌，镜子出现裂痕，高超和高越像一叶扁舟，在翻涌的世界里漂流。一道道裂痕泡沫一样堆积，像海上的泡沫，清透闪亮。") 
    with Dissolve(1.0)
    pause 

    $ show_narrator("高超心里知道，这是梦要醒的征兆。从睡眠和水面里冒头的感觉类似，都是从溺水里惊醒。") 
    with Dissolve(1.0)
    pause

    $ clear_narration()
    # $ hide screen narration_screen

    # 创建一个纯白色图像
    image pure_white = Solid("#ffffff")

    call flash_effect from _call_flash_effect

    scene pure_white
    with Dissolve(1.0)

    stop music fadeout(1.0)

    # 真结局现实部分 - 使用默认字体和黑色
    $ show_fullscreen_narrator("{font=AlibabaPuHuiTi-2-75-SemiBold.ttf}{color=#000000}高超猛地睁开眼睛。阳光顺着窗帘缝隙射进来，高越还在上铺沉沉睡着。高超挣扎着爬起身，换衣服，穿校服。见高越还没醒，他坐在下铺踢上铺的木板。高越被他踢醒，烦躁地哼哼两声。起床了起床了！妈妈穿着围裙进门来喊他俩起床。门撕开一道小缝，透过缝隙，能看到爸爸坐在餐桌前看报纸。{/color}{/font}")
    with Dissolve(1.0)
    pause

    $ show_fullscreen_narrator("{font=AlibabaPuHuiTi-2-75-SemiBold.ttf}{color=#000000}两人洗漱穿戴好，一起去卫生间刷牙。小小的卫生间容纳两个人就是极限，高超忙着刷牙，而高越挤在他旁边。烦躁，实在是烦躁。他俩已经长到一米八了，不再是小小的两个孩童。对方的身体已经构成足够的威胁，可空间还是这么小。高超怕他把高越吃掉，又怕被高越吃掉，只能在这狭小的空间里，勉力维持平衡。{/color}{/font}")
    with Dissolve(1.0)
    pause

    $ show_fullscreen_narrator("{font=AlibabaPuHuiTi-2-75-SemiBold.ttf}{color=#000000}吐掉牙膏后，嘴里仍有淡淡薄荷味。市面上牙膏味道都差不多，但高越说其实有差别。这一款的比较辣，那一款比较凉。他俩用一管牙膏，味道没有任何差别。漱口以后，高越忽然亲了他一下。亲在额头上，高超下意识用手去摸那一小块区域，只有一点甜蜜的凉。{/color}{/font}")
    with Dissolve(1.0)
    pause

    $ clear_fullscreen_narration()

    $ show_fullscreen_narrator("{font=AlibabaPuHuiTi-2-75-SemiBold.ttf}{color=#000000}高越：你想要的不就是这个吗？{/color}{/font}")
    with Dissolve(1.0)
    pause

    $ show_fullscreen_narrator("{font=AlibabaPuHuiTi-2-75-SemiBold.ttf}{color=#000000}高越轻轻地说。狡黠的笑转瞬即逝，他用胳膊肘推高超，说快出去快出去。挤死了，咱家这小卫生间。待会儿去学校给我抄下英语作业。你们应该也学到第八节了吧？我赶不及了。{/color}{/font}")
    with Dissolve(1.0)
    pause

    $ show_fullscreen_narrator("{font=AlibabaPuHuiTi-2-75-SemiBold.ttf}{color=#000000}高超：嗯。{/color}{/font}")
    with Dissolve(1.0)
    pause

    $ show_fullscreen_narrator("{font=AlibabaPuHuiTi-2-75-SemiBold.ttf}{color=#000000}高超轻轻应允。今天天气很好，天光大亮。\n\n\n{/color}{/font}")
    with Dissolve(1.0)
    pause

    $ show_fullscreen_narrator("{font=AlibabaPuHuiTi-2-75-SemiBold.ttf}{color=#000000}全文完。{/color}{/font}")
    with Dissolve(1.0)
    pause

    scene black

    play sound bonus

    $ show_fullscreen_narrator("{cps=8}{color=#cccccc}恭{/color}{color=#dddddd}喜{/color}{color=#eeeeee}您{/color}{color=#ffffff}解{/color}{color=#eeeeee}锁{/color}{color=#dddddd}真{/color}{color=#cccccc}结{/color}{color=#bbbbbb}局{/color}{color=#aaaaaa}！{/color}{/cps}")
    with Dissolve(1.0)
    pause

    return

label hidden_ending_1:
    $ persistent.hidden_ending = True
    $ show_value_ui = None
    scene black
    gc "我不相信。"

    $ show_fullscreen_narrator("{cps=50}鍟婂jm3憖鍛€鍟婂彂q8x鍔涚鎶€abcd鍝堝搱鍝堝搱鏈哄3pqz鏈哄櫒濂藉儚鍗￠晙锛熺┖璁捐w5r鍦版柟12345涓嶅鐢╋紒v9k杩樿鍐嶆潵鐐规柟渚匡紵鍟婂憖鍛€鍜嬩簡鍟婂摝鍝﹀摕鍠傚摝鍜﹀彂鍔涚鎶€鏄痜2h繖鏍风殑鍚楋紵opuyt涓嶇煡閬撲簡鍛€绱浜嗗搱鍝堝搱鎶よ偆鍝佸拰娉曞叞鍏媐ghjkl鏈夊叧b4t绯诲悧锛熷畬鍏nmsx娌℃湁鍟婂搱鍝堝搱鎴戞噿寰楁兂浜嗗彂鍔涚鎶€灏卞彂鍔涚鎶€鍚э紝鏈哄櫒浜哄彲浠ョ殑锛丳OIUTY鍟婂搱鍝堝搱鍛冨憙鍛冨憙鍛冨憙鍙戯紱鍟暘鍟暘鍟暘jj闀滃ご鎬庝箞鎼炵殑鐪嬩簡d6s灏辩湅浜嗗憖鍟婂憖鍛€鍟婂憖鎶よ偆鏈哄櫒鎶ヨzxcvbnm鎶ヨ鎶ヨ杩欎釜鏈哄櫒鎬庝箞鍥炰簨鏄痥9p璇锛熼晜绌鸿璁″湴寮€鏈烘敹鍒板洖澶嶅崱鏄痬7c鍒嗛挓濂戒簡鏈哄櫒浜哄ソ鍍忚鎴戝紕鍧忎簡鍝堝搱鍝堝搱鎶变笉璧峰暒鍟婂憖鍟婂憖鍟婂晩鍟婂晩鍟婂晩鍟婂晩鍟婂晩{/cps}")
    $ gc_face = "fear"
    # 乱码
    gc "{cps=50}??!??!???!!??????????????????????{/cps}"
    extend "{cps=70}@@妗堜緥锛佸挭鍛冨懙锛佸挭鍛冨彂锛佸挭鍛冮樋鑾卞厠鏂倢鑲や綇鍛滃搯鍝嗗挭@@{/cps}"
    extend "{cps=90}##asdkjfhasdlkj###qwyu###zxmvnb###lkjpoihfgdsa###{/cps}"
    extend "{cps=110}鎴栬浣犺繕涓嶅お鏄庣櫧鎴戜滑p4j6t8k1s9鎴栬浣犺繕涓嶅お鏄庣櫧鎴戜滑w2n5q0r3m7{/cps}"
    pause 2.8

    $ gc_face = "smile"
    # 乱码渐弱，文字浮现
    gc "{cps=30}@@～或＊许＃你￥还＆不＾太＿明＋白＝我＝们［］｛｝〈〉《》？…—·～＠＃＄＆＊＋＝｛｝{/cps}"
    pause
    
    gc "{cps=20}我..{w=0.3}还有高越..{w=0.5}＠高＠＃越＃＄＾＆＊＊（（高越））{/cps}"
    extend "{cps=15}绝不可能不信任对方。{/cps}"
    pause

    gc "{cps=18}高越会骗我..{w=0.4}但我绝不会..{w=0.6}＠不＠＃会＃＄＾＆＊＊的啊{/cps}"
    extend "{cps=12}不信任他。{/cps}"
    pause

    $ clear_fullscreen_narration()
    $ gc_face = "normal"
    gc "{cps=8}重来吧...{w=1.0}更努力倾听我们的心...{/cps}"
    pause

    $ clear_fullscreen_narration()
    play sound bonus
    $ show_fullscreen_narrator("{cps=6}{color=#777777}恭喜您解锁【隐藏结局：轻率的否认】🎉{/color}{/cps}\n\n\n\n")
    pause 2.0

    stop music fadeout 4.0
    pause 2.0
    
    $ show_fullscreen_narrator("{cps=4}{color=#555555}系统重启初始化中......{/color}{/cps}")
    pause
    
    return
