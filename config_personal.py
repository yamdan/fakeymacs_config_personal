﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

# https://stackoverflow.com/questions/2904274/globals-and-locals-in-python-exec
# https://docs.python.org/3/library/functions.html?highlight=exec%20global#exec

# 本ファイルは、config_personal.py というファイル名にすることで個人設定ファイルとして機能します。
# 本ファイルの設定には [] で括られたセクション名が定義されており、その単位で config.py の中に設定
# が取り込まれ、exec関数により実行されます。config.py ファイル内の exec関数をコールしているところ
# を検索すると、何のセクションがどこで読み込まれるかが分かると思います。

# 本ファイルはサンプルファイルです。本ファイルに記載のない設定でも、config.py から設定を取り込み、
# カスタマイズしてご利用ください。

####################################################################################################
## 初期設定
####################################################################################################
# [section-init] -----------------------------------------------------------------------------------

print(startupString())

keymap.editor = r"notepad.exe"
keymap.setFont("ＭＳ ゴシック", 12)

####################################################################################################
## 機能オプションの選択
####################################################################################################
# [section-options] --------------------------------------------------------------------------------

# IMEの設定（次の設定のいずれかを有効にする）
# fc.ime = "old_Microsoft_IME"
# fc.ime = "new_Microsoft_IME"
# fc.ime = "Google_IME"
fc.ime = None

# 日本語キーボード設定をした OS 上で英語キーボードを利用するかどうかを指定する
# （True: 使う、False: 使わない）
# （False に設定した場合でも、OS の設定が日本語キーボードになっていれば、ランチャーメニュー
#   の一番最後に表示されるメニューからキーボード種別を切り替えることができます）
fc.use_usjis_keyboard_conversion = False

# IME の状態をテキスト カーソル インジケーターの色で表現するかどうかを指定する
# （True: 表現する、False: 表現しない）
# （テキスト カーソル インジケーターを利用するには、次のページを参考とし設定を行ってください
#   https://faq.nec-lavie.jp/qasearch/1007/app/servlet/relatedqa?QID=022081）
fc.use_ime_status_cursor_color = False

# IME が ON のときのテキスト カーソル インジケーターの色を指定する
fc.ime_on_cursor_color = 0x00C800 # 濃い緑

# IME が OFF のときのテキスト カーソル インジケーターの色を指定する
fc.ime_off_cursor_color = 0x0000FF # 赤

####################################################################################################
## 基本設定
####################################################################################################
# [section-base-1] ---------------------------------------------------------------------------------

# すべてのキーマップを透過（スルー）するアプリケーションソフトを指定する
# （keymap_base、keymap_global を含むすべてのキーマップをスルーします）
fc.transparent_target  += []

# Emacs のキーバインドに“したくない”アプリケーションソフトを指定する
# （Keyhac のメニューから「内部ログ」を ON にすると processname や classname を確認することができます）
fc.not_emacs_target    += []

# IME の切り替え“のみをしたい”アプリケーションソフトを指定する
# （指定できるアプリケーションソフトは、not_emacs_target で（除外）指定したものからのみとなります）
fc.ime_target          += []

# キーマップ毎にキー設定をスキップするキーを指定する
# （リストに指定するキーは、define_key の第二引数に指定する記法のキーとしてください。"A-v" や "C-v"
#   のような指定の他に、"M-f" や "Ctl-x d" などの指定も可能です。"M-g*" のようにワイルドカードも
#   利用することができます。ワイルドカード文字をエスケープしたい場合は、[] で括ってください。）
# （ここで指定したキーに新たに別のキー設定をしたいときには、「-2」が付くセクション内で define_key2
#   関数を利用して定義してください）
fc.skip_settings_key    = {"keymap_base"      : ["*W-g"], # ベース Keymap
                           "keymap_global"    : [],       # グローバル Keymap
                           "keymap_emacs"     : [],       # Emacs キーバインド対象アプリ用 Keymap
                           "keymap_vscode"    : [],       # Emacs キーバインド VSCode 拡張用 Keymap
                           "keymap_ime"       : [],       # IME 切り替え専用アプリ用 Keymap
                           "keymap_ei"        : [],       # Emacs 日本語入力モード用 Keymap
                           "keymap_tsw"       : [],       # タスク切り替え画面用 Keymap
                           "keymap_lw"        : [],       # リストウィンドウ用 Keymap
                           }

# Emacs のキーバインドにするアプリケーションソフトで、Emacs キーバインドから除外するキーを指定する
# （リストに指定するキーは、Keyhac で指定可能なマルチストロークではないキーとしてください。
#   Fakeymacs の記法の "M-f" や "Ctl-x d" などの指定はできません。"A-v"、"C-v" などが指定可能です。）
# （ここで指定しなくとも、左右のモディファイアキーを使い分けることで入力することは可能です）
fc.emacs_exclusion_key  = {"chrome.exe"       : ["C-l", "C-t"],
                           "msedge.exe"       : ["C-l", "C-t"],
                           "firefox.exe"      : ["C-l", "C-t"],
                           "Code.exe"         : ["C-S-b", "C-S-f", "C-S-p", "C-S-n", "C-S-a", "C-S-e"],
                           }

# 左右どちらの Ctrl キーを使うかを指定する（"L": 左、"R": 右）
# fc.side_of_ctrl_key = "L"
fc.side_of_ctrl_key = "R"

# Esc キーを Meta キーとして使うかどうかを指定する（True: 使う、False: 使わない）
# （True（Meta キーとして使う）に設定されている場合、ESC の二回押下で ESC が入力されます）
fc.use_esc_as_meta = False

# Emacs 日本語入力モードを使うかどうかを指定する（True: 使う、False: 使わない）
# fc.use_emacs_ime_mode = True
fc.use_emacs_ime_mode = False

# Emacs 日本語入力モードが有効なときに表示するバルーンメッセージを指定する
# fc.emacs_ime_mode_balloon_message = None
fc.emacs_ime_mode_balloon_message = "▲"

# IME の状態を表示するバルーンメッセージを表示するかどうかを指定する（True: 表示する、False: 表示しない）
# fc.use_ime_status_balloon = True
fc.use_ime_status_balloon = False

# IME をトグルで切り替えるキーを指定する（複数指定可）
fc.toggle_input_method_key = []
# fc.toggle_input_method_key += ["C-Yen"]
# fc.toggle_input_method_key += ["C-o"]
# fc.toggle_input_method_key += ["O-LAlt"]

#---------------------------------------------------------------------------------------------------
# IME を切り替えるキーの組み合わせ（disable、enable の順）を指定する（複数指定可）
# （toggle_input_method_key のキー設定より優先します）
fc.set_input_method_key = []

## 日本語キーボードを利用している場合、<無変換> キーで英数入力、<変換> キーで日本語入力となる
# fc.set_input_method_key += [["(29)", "(28)"]]

## 日本語キーボードを利用している場合、<Ａ> キーで英数入力、<あ> キーで日本語入力となる
## （https://docs.microsoft.com/ja-jp/windows-hardware/design/component-guidelines/keyboard-japan-ime）
# fc.set_input_method_key += [["(26)", "(22)"]]

## LAlt の単押しで英数入力、RAlt の単押しで日本語入力となる
## （JetBrains 製の IDE でこの設定を利用するためには、ツールボタンをオンにする必要があるようです。
##   設定は、View -> Appearance -> Tool Window Bars を有効にしてください。）
# fc.set_input_method_key += [["O-LAlt", "O-RAlt"]]

## C-j や C-j C-j で 英数入力となる（toggle_input_method_key の設定と併せ、C-j C-o で日本語入力となる）
# fc.set_input_method_key += [["C-j", None]]

## C-j で英数入力、C-o で日本語入力となる（toggle_input_method_key の設定より優先）
# fc.set_input_method_key += [["C-j", "C-o"]]

## C-j で英数入力、C-i で日本語入力となる（C-i が Tab として利用できなくなるが、トグルキー C-o との併用可）
# fc.set_input_method_key += [["C-j", "C-i"]]
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Emacs 日本語入力モードを利用する際に、IME のショートカットを置き換えるキーの組み合わせ
# （置き換え先、置き換え元）を指定する
# （「ことえり」のキーバインドを利用するための設定例です。Google 日本語入力で「ことえり」の
#   キー設定になっている場合には不要ですが、設定を行っていても問題はありません。）
fc.emacs_ime_mode_key = []
fc.emacs_ime_mode_key += [["C-i", "S-Left"],  # 文節を縮める
                          ["C-o", "S-Right"], # 文節を伸ばす
                          ["C-j", "F6"],      # ひらがなに変換
                          ["C-k", "F7"],      # 全角カタカナに変換
                          ["C-l", "F9"],      # 全角英数に表示切替
                          ["C-;", "F8"]]      # 半角に変換

if is_japanese_keyboard:
    fc.emacs_ime_mode_key += [["C-:", "F10"]] # 半角英数に表示切替
else:
    fc.emacs_ime_mode_key += [["C-'", "F10"]] # 半角英数に表示切替
#---------------------------------------------------------------------------------------------------

# アプリケーションキーとして利用するキーを指定する
# （修飾キーに Alt は使えないようです）
fc.application_key = None
# fc.application_key = "O-RCtrl"

# 数引数の指定に Ctrl+数字キーを使うかを指定する（True: 使う、False: 使わない）
# （False に指定しても、C-u 数字キーで数引数を指定することができます）
fc.use_ctrl_digit_key_for_digit_argument = False

# アクティブウィンドウを切り替えるキーの組み合わせ（前、後 の順）を指定する（複数指定可）
# （A-Esc キーの動作とは異なり、仮想デスクトップを跨ぎ、最小化されていないウィンドウを順に切り替え
#   ます。初期設定は ["A-p", "A-n"] としていますが、Emacs の shell-mode のキーバインドなどと設定が
#   被る場合には、["A-S-p", "A-S-n"] などの異なる設定とするか、Emacs 側に次の設定を入れて、Emacs 側
#   のキーの設定を置き換えてご利用ください。
#     (define-key key-translation-map (kbd "M-S-p") (kbd "M-p"))
#     (define-key key-translation-map (kbd "M-S-n") (kbd "M-n"))
#  ）
fc.window_switching_key = []
fc.window_switching_key += [["A-p", "A-n"]]
# fc.window_switching_key += [["A-S-p", "A-S-n"]]
# fc.window_switching_key += [["A-Up", "A-Down"]]

# 仮想デスクトップを切り替えるキーの組み合わせ（前、後 の順）を指定する（複数指定可）
# （仮想デスクトップを切り替えた際にフォーカスのあるウィンドウを適切に処理するため、設定するキーは
#   Win キーとの組み合わせとしてください）
# （デフォルトキーは、["W-C-Left", "W-C-Right"]）
fc.desktop_switching_key = []
fc.desktop_switching_key += [["W-,", "W-."]]
# fc.desktop_switching_key += [["W-b", "W-f"]]

# Microsoft Excel のセル内で改行を選択可能かを指定する（True: 選択可、False: 選択不可）
# （kill_line 関数の挙動を変えるための変数です。Microsoft Excel 2019 以降では True にして
#   ください。）
fc.is_newline_selectable_in_Excel = True

# ゲームなど、キーバインドの設定を極力行いたくないアプリケーションソフトを指定する
# （keymap_global 以外のすべてのキーマップをスルーします。ゲームなど、Keyhac によるキー設定と
#   相性が悪いアプリケーションソフトを指定してください。keymap_base の設定もスルーするため、
#   英語 -> 日本語キーボード変換の機能が働かなくなることにご留意ください。）
fc.game_app_list        = ["ffxiv_dx11.exe",         # FINAL FANTASY XIV
                           ]

# [section-base-2] ---------------------------------------------------------------------------------
##################################################
## HandS (Henkan/Muhenkan and Shift)
##################################################

# 変換キーを右シフトキー、無変換キーを左シフトキーとして使えるように
# それぞれ単独で押した場合は元の役割(変換/無変換)が機能
# 方針:
# 変換->右シフト, 無変換->左シフト、カタカナひらがな->左Win への置き換えは
# レジストリで実施し、keyhacでは行わない。
# 左/右シフトの単独押しが無変換/変換キーとして動くようにする点にのみ
# keyhacを利用する。

# 右シフト単独押し -> 変換(28)
define_key(keymap_global, "O-Rshift", self_insert_command("(28)"))

# 左シフト単独押し -> 無変換(29)
define_key(keymap_global, "O-Lshift", self_insert_command("(29)"))

##################################################
## その他のマッピング
##################################################

# Win + Q でウィンドウ閉じ
define_key(keymap_global, "W-q", reset_search(reset_undo(reset_counter(reset_mark(kill_emacs)))))

# W-S-B, W-S-F, W-S-P, W-S-N でウィンドウ移動
define_key(keymap_global, "W-S-B", self_insert_command("W-Left"))
define_key(keymap_global, "W-S-F", self_insert_command("W-Right"))
define_key(keymap_global, "W-S-P", self_insert_command("W-Up"))
define_key(keymap_global, "W-S-N", self_insert_command("W-Down"))

####################################################################################################
## クリップボードリストの設定
####################################################################################################
# [section-clipboardList-1] ------------------------------------------------------------------------

# 定型文
fc.fixed_items = [
    ["---------+ x 8", "---------+" * 8],
    ["メールアドレス", "user_name@domain_name"],
    ["住所",           "〒999-9999 ＮＮＮＮＮＮＮＮＮＮ"],
    ["電話番号",       "99-999-9999"],
]
fc.fixed_items[0][0] = list_formatter.format(fc.fixed_items[0][0])

# 日時
fc.datetime_items = [
    ["YYYY/MM/DD HH:MM:SS", dateAndTime("%Y/%m/%d %H:%M:%S")],
    ["YYYY/MM/DD",          dateAndTime("%Y/%m/%d")],
    ["HH:MM:SS",            dateAndTime("%H:%M:%S")],
    ["YYYYMMDD_HHMMSS",     dateAndTime("%Y%m%d_%H%M%S")],
    ["YYYYMMDD",            dateAndTime("%Y%m%d")],
    ["HHMMSS",              dateAndTime("%H%M%S")],
]
fc.datetime_items[0][0] = list_formatter.format(fc.datetime_items[0][0])

fc.clipboardList_listers = [
    ["定型文", cblister_FixedPhrase(fc.fixed_items)],
    ["日時",   cblister_FixedPhrase(fc.datetime_items)],
]

# [section-clipboardList-2] ------------------------------------------------------------------------

####################################################################################################
## ランチャーリストの設定
####################################################################################################
# [section-lancherList-1] --------------------------------------------------------------------------

# アプリケーションソフト
fc.application_items = [
    ["Notepad",     keymap.ShellExecuteCommand(None, r"notepad.exe", "", "")],
    ["Explorer",    keymap.ShellExecuteCommand(None, r"explorer.exe", "", "")],
    ["Cmd",         keymap.ShellExecuteCommand(None, r"cmd.exe", "", "")],
    ["MSEdge",      keymap.ShellExecuteCommand(None, r"msedge.exe", "", "")],
    ["Chrome",      keymap.ShellExecuteCommand(None, r"chrome.exe", "", "")],
    ["Firefox",     keymap.ShellExecuteCommand(None, r"firefox.exe", "", "")],
    ["Thunderbird", keymap.ShellExecuteCommand(None, r"thunderbird.exe", "", "")],
]
fc.application_items[0][0] = list_formatter.format(fc.application_items[0][0])

# ウェブサイト
fc.website_items = [
    ["Google",          keymap.ShellExecuteCommand(None, r"https://www.google.co.jp/", "", "")],
    ["Facebook",        keymap.ShellExecuteCommand(None, r"https://www.facebook.com/", "", "")],
    ["Twitter",         keymap.ShellExecuteCommand(None, r"https://twitter.com/", "", "")],
    ["Keyhac",          keymap.ShellExecuteCommand(None, r"https://sites.google.com/site/craftware/keyhac-ja", "", "")],
    ["Fakeymacs",       keymap.ShellExecuteCommand(None, r"https://github.com/smzht/fakeymacs", "", "")],
    ["NTEmacs＠ウィキ", keymap.ShellExecuteCommand(None, r"https://w.atwiki.jp/ntemacs/", "", "")],
]
fc.website_items[0][0] = list_formatter.format(fc.website_items[0][0])

fc.lancherList_listers = [
    ["App",     cblister_FixedPhrase(fc.application_items)],
    ["Website", cblister_FixedPhrase(fc.website_items)],
    ["Other",   cblister_FixedPhrase(fc.other_items)],
]

# [section-lancherList-2] --------------------------------------------------------------------------

####################################################################################################
## 拡張機能の設定
####################################################################################################
# [section-extensions] -----------------------------------------------------------------------------

# https://github.com/smzht/fakeymacs/blob/master/fakeymacs_manuals/extensions.org

# --------------------------------------------------------------------------------------------------

# Chrome 系ブラウザで Ctl-x C-b を入力した際、Chrome の拡張機能 Quick Tabs を起動する
if 0:
    fc.chrome_list= ["chrome.exe",
                     "msedge.exe"]
    fc.quick_tabs_shortcut_key = "A-q"
    exec(readConfigExtension(r"chrome_quick_tabs\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# Emacs の shell-command-on-region の機能をサポートする
if 0:
    fc.unix_tool = "WSL"
    # fc.unix_tool = "MSYS2"
    # fc.unix_tool = "Cygwin"
    # fc.unix_tool = "BusyBox"
    # fc.bash_options = []
    fc.bash_options = ["-l"]
    exec(readConfigExtension(r"shell_command_on_region\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# VSCode 用のキーの設定を行う
if 1:
    fc.vscode_target  = ["Code.exe"]
    fc.vscode_target += ["chrome.exe",
                         "msedge.exe",
                         "firefox.exe",
                         ]

    # fc.vscode_prefix_key = [["C-;", "C-A-;"]]
    fc.use_ctrl_atmark_for_mark = False
    fc.use_direct_input_in_vscode_terminal = False
    fc.esc_mode_in_keyboard_quit = 1

    # VSCode Extension 用のキーの設定を行う
    fc.vscode_dired = False
    fc.vscode_recenter = False
    fc.vscode_recenter2 = False
    fc.vscode_occur = False
    fc.vscode_quick_select = True
    fc.vscode_input_sequence = True
    fc.vscode_insert_numbers = True
    fc.vscode_keyboard_macro = False
    fc.vscode_filter_text = False

    exec(readConfigExtension(r"vscode_key\config.py"), dict(globals(), **locals()))
    # vscode_extensions\config.py は、vscode_key\config.py 内部から呼ばれている

# --------------------------------------------------------------------------------------------------

# Everything を起動するキーを指定する
if 0:
    exec(readConfigExtension(r"everything\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# ブラウザをポップアップしてから C-l、C-t を入力するキーを設定する
if 0:
    fc.browser_list= ["chrome.exe",
                      "msedge.exe",
                      "firefox.exe"]
    exec(readConfigExtension(r"browser_key\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 指定したアプリケーションソフトに F2（編集モード移行）を割り当てるキーを設定する
if 0:
    exec(readConfigExtension(r"edit_mode\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# Emacs の場合、IME 切り替え用のキーを C-\ に置き換える
if 0:
    exec(readConfigExtension(r"real_emacs\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 英語キーボード設定をした OS 上で日本語キーボードを利用する場合の設定を行う
if 0:
    fc.change_keyboard_startup = "US"
    # fc.change_keyboard_startup = "JP"
    exec(readConfigExtension(r"change_keyboard\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 日本語キーボード設定をした OS 上で日本語キーボードを英語配列で利用する場合の設定を行う
if 0:
    fc.change_keyboard2_startup = "US"
    # fc.change_keyboard2_startup = "JP"
    exec(readConfigExtension(r"change_keyboard2\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# クリップボードに格納したファイルもしくはフォルダのパスを emacsclient で開く
if 0:
    fc.emacsclient_name = r"<emacsclient プログラムをインストールしている Windows のパス>\wslclient-n.exe"
    exec(readConfigExtension(r"emacsclient\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 指定したキーを押下したときに IME の状態を表示する
if 0:
    fc.pop_ime_balloon_key = ["C-;"]
    # fc.pop_ime_balloon_key = ["O-" + fc.side_of_ctrl_key + "Ctrl"] # Ctrl キーの単押し
    exec(readConfigExtension(r"pop_ime_balloon\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 60% US キーボードのキー不足（Delete キー、Backquote キー不足）の対策を行う
if 0:
    exec(readConfigExtension(r"compact_keyboard\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 半角と全角の入力を間違えた際、入力モードの切り替えと入力文字の変換を行う
if 0:
    exec(readConfigExtension(r"zenkaku_hankaku\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------
