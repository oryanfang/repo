#!/usr/bin/env python3
# 生成每个包的详情页：depictions/<包名>/depiction.json（Sileo 原生）和 index.html（Zebra 等用的网页版）。
# Sileo 不会按手机语言切换，所以默认英文，另加一个「中文」标签页；更新日志中英双语。
# 改详情页 / 加更新日志就改这个文件，然后运行：python3 depictions/make_depictions.py
import json, html, os

BASE = "https://oryanfang.github.io/repo/depictions/"
HERE = os.path.dirname(os.path.abspath(__file__))

PACKAGES = {
"com.xyrith.xrkit": {
    "name": "xrkit", "tint": "#6FB596", "icon": True, "screenshots": [],
    "source": "https://github.com/oryanfang/xrkit",
    "en": {
        "intro": "All‑in‑one tweak for jailbroken iOS 17: Home Screen, Lock Screen, Control Center and the App Switcher, each change behind its own switch.",
        "note": "> **Only tested on iOS 17.3.1**; some features may not work on other versions. Requires a **roothide** jailbreak. The settings are in English and Chinese (About › Language).",
        "features": """**Home Screen**
- Hide the home bar, Today view, App Library, page dots, Search button, icon labels, notification badges
- Folders: hide the background, or show the folder as its first app's icon
- Layout: up to 6 columns and 8 rows per page; hide "+" and "Done" while editing
- Dock: hide it, background style, icon count (3–6)
- Icon menu: Copy Bundle ID, Force Quit, Relaunch
- Icons: badges in the app's own color, download percentage, fade when idle, haptic on tap
- Screenshots: skip the corner thumbnail

**Lock Screen**
- Hide the flashlight / camera buttons, "Swipe up to open" and the Control Center hint
- Disable the camera swipe and pull‑down search
- Go straight to the Home Screen after Face ID
- Battery percentage while charging, Now Playing options

**Control Center**
- Background / module transparency, corner radius, hide the status bar, slider percentages
- Module loader (a CCSupport replacement): third‑party modules, and fixed modules can be moved and removed
- Built‑in modules: respring, lock, screenshot, auto‑brightness, clear apps, xrkit settings, VPN (long‑press to switch), dark mode, Night Shift, True Tone, keep awake, hotspot, location, network speed, battery info

**App Switcher**
- Layout: system / grid / iPad
- Hide titles and icons, long‑press to lock apps, pull down to clear all, memory usage on each card
- Card size, corners, spacing, position

Settings live in Settings › xrkit; some options need a respring.""",
        "rows": [("Version", "0.2.3"), ("Supported iOS", "iOS 17 (tested on 17.3.1)"), ("Jailbreak", "roothide"), ("Author", "xyrith")],
        "buttons": [("Source Code", ""), ("Report an Issue", "/issues")],
    },
    "zh": {
        "intro": "iOS 17 越狱综合优化插件：主屏幕、锁屏、控制中心、多任务，一个插件里按需开关。",
        "note": "> **只在 iOS 17.3.1 上测试过**，其他版本可能部分功能不生效。需要 **roothide** 越狱环境。设置页有中文和英文（关于 › 语言）。",
        "features": """**主屏幕**
- 隐藏：底部横条、负一屏、App 资源库、页面圆点、底部搜索按钮、图标名称、通知角标
- 文件夹：隐藏背景、文件夹图标显示第一个 App 的图标
- 布局：每页最多 6 列、8 行；编辑时隐藏「+」和「完成」
- Dock：隐藏、背景样式、图标数量（3～6 个）
- 长按图标菜单：复制 Bundle ID、强制退出、重新打开
- 图标：角标跟随 App 主色调、下载时显示百分比、静止时半透明、点按时震动
- 截图：不显示左下角预览

**锁屏**
- 隐藏手电筒 / 相机按钮、「上滑打开」、右上角控制中心提示条
- 禁止左滑打开相机、禁止下滑搜索
- 面容识别后直接进主屏幕
- 充电时显示电量、音乐播放器显示方式

**控制中心**
- 背景 / 模块透明度、模块圆角、隐藏状态栏、亮度和音量显示百分比
- 模块加载器（可替代 CCSupport）：加载第三方模块，原本固定的模块也能移动、删除
- 自带模块：注销、锁屏、截屏、自动亮度、清除后台、xrkit 设置、VPN（长按切换）、深色模式、夜览、原彩、常亮、个人热点、定位、实时网速、电池信息

**多任务**
- 排列样式：系统 / 网格 / iPad
- 隐藏卡片名称和图标、长按锁定 App、下拉清除全部、卡片上显示内存占用
- 卡片大小、圆角、间距、上下位置

设置在「设置 › xrkit」，部分选项需要注销才生效。""",
        "rows": [("版本", "0.2.3"), ("适用系统", "iOS 17（只在 17.3.1 测过）"), ("越狱环境", "roothide"), ("作者", "xyrith")],
        "buttons": [("源代码", ""), ("反馈问题", "/issues")],
    },
    "changelog": [
        ("0.2.3", "- Fixed: after enabling More Controls, the new controls could be missing from Settings › Control Center because Settings kept running from before. The Respring button now also closes Settings\n- The More Controls description now says where to add them (Settings › Control Center › More Controls, tap +)",
                  "- 修复：打开「启用更多控件」后，「设置 › 控制中心」里可能看不到新控件（「设置」还是之前打开的那个）。现在「注销」按钮会顺便关掉「设置」\n- 「更多控件」的说明写清楚了添加位置（设置 › 控制中心 › 更多控制，点 ＋）"),
        ("0.2.2", "- New icon\n- Home Screen layout: up to 6 columns and 8 rows per page\n- Hide \"+\" and \"Done\" while editing the Home Screen\n- Icon menu: Copy Bundle ID, Force Quit, Relaunch\n- Haptic on tap\n- Memory usage on App Switcher cards",
                  "- 新图标\n- 主屏幕布局：每页最多 6 列、8 行\n- 编辑主屏幕时隐藏「+」和「完成」\n- 长按图标菜单：复制 Bundle ID、强制退出、重新打开\n- 点按图标时震动\n- 多任务卡片显示内存占用"),
        ("0.2.1", "- English settings, following the system language\n- About › Language: System / 中文 / English, no respring needed\n- \"Copy Debug Info\" is now always in English",
                  "- 设置页、弹窗和「需注销」标签有了英文，跟随系统语言\n- 关于页加「语言」：跟随系统 / 中文 / English，马上生效，不用注销\n- 「复制问题信息」统一用英文，方便贴进 GitHub Issue"),
        ("0.2.0", "First public release.", "第一个公开版本。"),
    ],
},
"com.xyrith.xrhea": {
    "name": "xrhea", "tint": "#14B8A6", "icon": True,
    "screenshots": [("en-battery", "Battery"), ("en-log", "Log"), ("en-alerts", "Alerts")],
    "screenshots_zh": [("zh-battery", "电池信息"), ("zh-log", "日志"), ("zh-alerts", "提示")],
    "source": "https://github.com/oryanfang/xrhea",
    "en": {
        "intro": "Battery and charging tweak for jailbroken iOS 17: detailed battery info, a real charge limit with scheduled full charge, heat protection, a battery log that shows where the charge goes, Low Power Mode automation, and short, readable alerts from the Dynamic Island.",
        "note": "> **Pre-release.** **Only tested on iOS 17.3.1**; some features may not work on other versions. Requires a **roothide** jailbreak. The settings are in English and Chinese (About › Language).",
        "features": """**Battery details**
- Maximum capacity, live power / voltage / current / temperature, time to full or to your limit
- While charging, power is what the charger delivers (matches a USB power meter)
- Charger info, capacity and cycle count
- ⚠️ on readings that need attention, with what to do about it

**Charge limit**
- Stop charging at 60–90%; the charger then powers the phone directly
- When you plug in: keep the limit, or charge to 100% this time
- Scheduled full charge: hold at the limit overnight, full by the time you set
- Monthly reminder to charge fully once

**Optimization**
- Heat protection while charging: stop charging or switch to intermittent charging at the set temperature (40 °C wired, 37 °C wireless recommended)
- Bypass while gaming: under heavy load, stop charging the battery and run on the charger to stay cooler
- Background drain alert: tells you when one app drains too much while locked

**Log**
- 24-hour battery level chart and 30 days of charging history, each with its own chart
- Measured speed for each charger, renamable
- Battery drain: standby drain, usage by app (all / while locked), push reconnects and network wakes
- Export everything as one Markdown file to save or hand to an AI

**Low Power Mode**
- Turn it on below a set level, off once charged to a set level, on while locked, and on while charging
- Keep 120 Hz in Low Power Mode on ProMotion models; other power savings stay on

**Alerts**
- From the Dynamic Island (a long pill like the one iOS shows when you plug in, or a shorter one), or a banner on other phones
- Charging: plugged in, target level, limit reached, bypass started, fully charged, charging summary
- Issues: slow charging, slowed by heat, loose cable, plugged in but not charging, hot, charging in the cold
- Usage: standby drain, bedtime, high power draw, background drain, weekly summary
- Each alert has its own switch and a Preview button; quiet during Focus with your own exceptions; tap to open the related page

Settings live in Settings › xrhea.""",
        "rows": [("Version", "0.3.1 (pre-release)"), ("Supported iOS", "iOS 17 (tested on 17.3.1)"), ("Jailbreak", "roothide"), ("Author", "xyrith")],
        "buttons": [("Source Code", ""), ("Report an Issue", "/issues"), ("Donate (WeChat)", "/blob/main/docs/wechat-reward.jpg")],
    },
    "zh": {
        "intro": "iOS 17 越狱电池与充电插件：详细的电池信息、真正能停充的充电上限和定时充满、高温保护、看得清电去哪了的电池日志、低电量模式自动开关，还有从灵动岛弹出的、一眼看得懂的提醒。",
        "note": "> **预览版。** **只在 iOS 17.3.1 上测试过**，其他版本可能部分功能不生效。需要 **roothide** 越狱环境。设置页有中文和英文（关于 › 语言）。",
        "features": """**电池信息**
- 最大容量，实时功率 / 电压 / 电流 / 温度，多久充满或充到上限
- 充电时的功率是充电头送进手机的功率（和 USB 数显线对得上）
- 充电器信息、容量和循环次数
- 需要注意的读数标 ⚠️，并给出处理办法

**充电上限**
- 充到 60%～90% 就停，之后电源直接给手机供电
- 插电时可以选「按上限停」或「这次充满」
- 定时充满：夜里先停在上限，在你设的时间前充满
- 每月提醒充满一次

**优化**
- 充电时的高温保护：达到设定温度（推荐有线 40℃、无线 37℃）就停充或改为间歇充电
- 边充边玩直充：负载高时停止给电池充电，由电源直接供电，温度更低
- 后台耗电提醒：某个 App 锁屏时耗电过多时提醒

**日志**
- 24 小时电量曲线、最近 30 天充电记录，每次都有曲线
- 每个充电器的实测速度，可以改名
- 耗电排查：锁屏待机速度、App 耗电排行（全部 / 锁屏时）、推送重连和网络唤醒次数
- 全部导出成一份 Markdown，可以保存或交给 AI 分析

**低电量模式**
- 低于设定电量自动开启、充到设定电量自动关闭、锁屏时开启、充电时开启
- ProMotion 机型在低电量模式下保持 120Hz，其他省电措施不变

**提醒**
- 从灵动岛弹出（和系统插电那条一样的长条，或者短条），没有灵动岛的机型用横幅
- 充电：插电、到点、到上限停充、开始直充、充满、拔线总结
- 异常：慢充、过热降速、接触不良、插着却不充、过热、低温充电
- 用电：锁屏掉电、睡前、高耗电、后台耗电、每周小结
- 每条单独开关，有「预览」；专注模式时静默，可以自选照常提醒的几条；点提醒打开相关页面

设置在「设置 › xrhea」。""",
        "rows": [("版本", "0.3.1（预览版）"), ("适用系统", "iOS 17（只在 17.3.1 测过）"), ("越狱环境", "roothide"), ("作者", "xyrith")],
        "buttons": [("源代码", ""), ("反馈问题", "/issues"), ("赞赏作者（微信）", "/blob/main/docs/wechat-reward.jpg")],
    },
    "changelog": [
        ("0.3.1 (pre-release)", "Fixed the weekly summary popping up again a few minutes after Monday 9:00, and Background Drain Alert repeating for the same app on the same day.",
                                "修复每周小结在周一 9:00 之后隔几分钟又弹一次，以及后台耗电提醒同一个 App 同一天重复弹。"),
        ("0.3.0 (pre-release)", "New Log: 24-hour battery chart, 30 days of charging history and measured charger speeds; Battery Drain: usage by app, standby drain and push reconnects; Markdown export; Bypass While Gaming and Background Drain Alert; separate wireless heat-protection temperature; Low Power Mode while charging; weekly summary and Bypass alerts; tap an alert to open the related page; Try It is now Preview.",
                                "新增日志：24 小时电量曲线、最近 30 天充电记录和充电器实测速度；耗电排查：App 耗电排行、锁屏待机速度和推送重连；Markdown 导出；边充边玩直充和后台耗电提醒；高温保护可单独设无线温度；充电时开启低电量模式；每周小结和直充提醒；点提醒打开相关页面；「试试看」改名「预览」。"),
        ("0.2.0 (pre-release)", "Scheduled full charge; heat protection (stop or intermittent charging); Low Power Mode automation and keeping 120 Hz in Low Power Mode; cleaner settings with sliders and new icons; the update check also finds pre-releases.",
                                "定时充满；高温保护（停充或间歇充电）；低电量模式自动开关，以及低电量模式下保持 120Hz；设置页精简排版，改用滑块和新图标；检查更新也能查到预览版。"),
        ("0.1.0 (pre-release)", "First release (pre-release): battery details, charge limit, Dynamic Island and banner alerts.",
                                "第一个版本（预览版）：电池信息、充电上限、灵动岛和横幅提醒。"),
    ],
},
"com.xyrith.xrsh": {
    "name": "xrsh", "tint": "#3B82F6", "icon": True,
    "screenshots": [("en-devices", "Devices"), ("terminal", "Terminal"), ("en-settings", "Settings")],
    "screenshots_zh": [("zh-devices", "设备页"), ("terminal", "终端"), ("zh-settings", "设置页")],
    "source": "https://github.com/oryanfang/xrsh-ios",
    "en": {
        "intro": "A lightweight SSH client and LAN scanner for iOS: scan your Wi‑Fi, tap a device, and you're in a terminal. On jailbroken devices the local terminal is a real shell.",
        "note": """- Only tested on a roothide‑jailbroken iPhone. The rootless package is the same app in a different location and hasn't been tested on a device
- If you installed xrsh with TrollStore before, uninstall it there first (it's the same app; both at once will conflict)
- Allow the Local Network permission on first launch, or no devices can be found
- License: PolyForm Noncommercial 1.0.0 (free for personal, noncommercial use)""",
        "features": """**Devices**
- Scans the current subnet for SSH devices, with device names and guessed types (Mac, Windows, Raspberry Pi, router…)
- Remembers the last scan; long‑press to name a device, copy its IP or connect
- Devices with passwordless login go straight to the terminal

**Terminal**
- SSH terminal with password or key login; host keys are remembered
- One‑tap passwordless login (ed25519; the private key stays in the Keychain)
- Local terminal: a real shell on jailbroken devices
- Command panel and SFTP file transfer

**AI assistant (optional, off by default)**
- Type `/xr` in a terminal to talk to an AI using your own OpenAI‑compatible API
- Read‑only commands run on their own, changes ask first, destructive commands are blocked

The UI is in English, Chinese, Japanese and Russian.""",
        "rows": [("Version", "1.1"), ("Supported iOS", "iOS 17 or later"), ("Jailbreak", "roothide (rootless untested)"), ("Author", "xyrith")],
        "buttons": [("Source Code", ""), ("Report an Issue", "/issues")],
    },
    "zh": {
        "intro": "iOS 上轻量的 SSH 终端与局域网设备扫描工具：扫描 Wi‑Fi，点一下设备就进终端。越狱环境下本机终端是真 shell。",
        "note": """- 只在 roothide 越狱的 iPhone 上测过；rootless 版是同一个 App，装的位置不同，没有在真机上测过
- 如果之前用 TrollStore 装过 xrsh，请先在 TrollStore 里卸载，再从这里安装（两个是同一个 App，同时装会冲突）
- 首次打开要允许「本地网络」权限，否则扫描不到设备
- 许可：PolyForm Noncommercial 1.0.0（可以个人非商业使用）""",
        "features": """**设备页**
- 扫描当前 Wi‑Fi 网段，找出 SSH 设备，显示设备名和推测的类型（Mac、Windows、树莓派、路由器等）
- 记住上次扫描结果；长按设备可以起名、复制 IP、SSH 连接
- 设置过免密登录的设备点一下直接进终端

**终端页**
- SSH 终端，支持密码和密钥登录，记住主机密钥
- 一键设置免密登录（ed25519 密钥，私钥存在系统钥匙串）
- 本机终端：越狱环境下是真 shell
- 常用命令面板、SFTP 传文件

**AI 助手（可选，默认关闭）**
- 在终端输入 `/xr` 和 AI 对话，用你自己的 OpenAI 兼容接口
- 只读命令自动运行，会改动设备的命令先问你，危险命令直接禁止

界面有中文、英文、日语和俄语。""",
        "rows": [("版本", "1.1"), ("适用系统", "iOS 17 或更高"), ("越狱环境", "roothide（rootless 未测）"), ("作者", "xyrith")],
        "buttons": [("源代码", ""), ("反馈问题", "/issues")],
    },
    "changelog": [
        ("1.1", "- AI assistant (optional, off by default): type `/xr` in a terminal\n- Japanese and Russian\n- Optional extras: tmux after SSH connects, device tools, saved connections\n- Fixes: Chinese input in the real shell, terminal text squeezed into two columns, Local Network prompt language",
                "- AI 助手（可选，默认关闭）：终端里输入 `/xr` 对话\n- 新增日语和俄语\n- 可选功能：SSH 连上后进入 tmux、设备小工具、常用连接\n- 修复：本机真 shell 中文输入、终端文字被挤成两列、「本地网络」权限提示的语言"),
        ("1.0", "First release.", "第一个版本。"),
    ],
},
}


def stack(pkg, lang, shots):
    t = pkg[lang]
    views = [{"class": "DepictionMarkdownView", "markdown": t["intro"]}]
    if shots:
        views.append({"class": "DepictionScreenshotsView", "itemCornerRadius": 12, "itemSize": "{160, 347}",
                      "screenshots": [{"url": BASE + pid + "/" + n + ".png", "accessibilityText": a} for n, a in shots]})
    views += [{"class": "DepictionMarkdownView", "markdown": t["features"]},
              {"class": "DepictionSeparatorView"},
              {"class": "DepictionMarkdownView", "markdown": t["note"]},
              {"class": "DepictionSeparatorView"}]
    views += [{"class": "DepictionTableTextView", "title": k, "text": v} for k, v in t["rows"]]
    views += [{"class": "DepictionTableButtonView", "title": k, "action": pkg["source"] + suffix} for k, suffix in t["buttons"]]
    return views


def md_html(text):
    out, inlist = [], False
    for line in text.split("\n"):
        line_html = html.escape(line.lstrip("> ")).replace("`", "")
        while "**" in line_html:
            line_html = line_html.replace("**", "<b>", 1).replace("**", "</b>", 1)
        if line.startswith("- "):
            if not inlist: out.append("<ul>"); inlist = True
            out.append("<li>" + line_html[2:] + "</li>"); continue
        if inlist: out.append("</ul>"); inlist = False
        if line.startswith("**") and line.endswith("**"): out.append("<h3>" + html.escape(line.strip("*")) + "</h3>")
        elif line.strip(): out.append("<p>" + line_html + "</p>")
    if inlist: out.append("</ul>")
    return "\n".join(out)


for pid, pkg in PACKAGES.items():
    d = os.path.join(HERE, pid)
    changelog = []
    for ver, en, zh in pkg["changelog"]:
        changelog += [{"class": "DepictionSubheaderView", "title": ver, "useBoldText": True},
                      {"class": "DepictionMarkdownView", "markdown": en + "\n\n" + zh}]
    depiction = {"minVersion": "0.1", "class": "DepictionTabView", "tintColor": pkg["tint"], "tabs": [
        {"tabname": "Details", "class": "DepictionStackView", "views": stack(pkg, "en", pkg["screenshots"])},
        {"tabname": "中文", "class": "DepictionStackView", "views": stack(pkg, "zh", pkg.get("screenshots_zh", pkg["screenshots"]))},
        {"tabname": "Changelog", "class": "DepictionStackView", "views": changelog},
    ]}
    with open(os.path.join(d, "depiction.json"), "w") as f:
        json.dump(depiction, f, ensure_ascii=False, indent=1)

    shots_html = "".join(f'<img src="{n}.png" alt="{html.escape(a)}">' for n, a in pkg["screenshots"])
    log_html = "".join(f"<h3>{ver}</h3>{md_html(en)}{md_html(zh)}" for ver, en, zh in pkg["changelog"])
    links = f'<a href="{pkg["source"]}">Source Code · 源代码</a> · <a href="{pkg["source"]}/issues">Report an Issue · 反馈问题</a>'
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{pkg["name"]}</title><style>
body{{font:16px -apple-system,sans-serif;margin:0;padding:16px;background:#f2f2f7;color:#111}}
@media(prefers-color-scheme:dark){{body{{background:#000;color:#eee}}.card{{background:#1c1c1e!important}}}}
.card{{background:#fff;border-radius:12px;padding:12px 16px;margin-bottom:12px}}h3{{margin:12px 0 4px}}ul{{padding-left:20px;margin:4px 0}}
.head{{display:flex;align-items:center;gap:12px}}.head img{{width:60px;height:60px;border-radius:13px}}a{{color:{pkg["tint"]}}}
.shots{{display:flex;gap:8px;overflow-x:auto}}.shots img{{width:30%;min-width:120px;border-radius:10px}}</style></head><body>
<div class="card head"><img src="icon.png" alt=""><div><b>{pkg["name"]}</b> {pkg["en"]["rows"][0][1]}<br><small>{html.escape(pkg["en"]["intro"].split(":")[0])}</small></div></div>
{f'<div class="card shots">{shots_html}</div>' if shots_html else ""}
<div class="card">{md_html(pkg["en"]["intro"])}{md_html(pkg["en"]["features"])}</div>
<div class="card">{md_html(pkg["en"]["note"])}</div>
<div class="card"><h3>中文</h3>{md_html(pkg["zh"]["intro"])}{md_html(pkg["zh"]["features"])}{md_html(pkg["zh"]["note"])}</div>
<div class="card"><h3>Changelog · 更新日志</h3>{log_html}</div>
<div class="card">{links}</div>
</body></html>'''
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(page)
    print("写好", pid)
