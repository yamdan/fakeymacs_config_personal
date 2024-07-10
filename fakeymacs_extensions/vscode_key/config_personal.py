# -*- mode: python; coding: utf-8-with-signature-dos -*-

# 本ファイルは、config_personal.py というファイル名にすることで vscode_key Extension の
# 機能拡張ファイルとして機能します。以下はサンプルコードです。

# # --------------------------------------------------------------------------------------------------

# def toggle_panel():
#     # VSCode Command : View: Tggole Panel
#     self_insert_command("C-j")()
#     # vscodeExecuteCommand("workbench.action.togglePanel")()

# # 本設定を行わなくとも、C-q C-j を利用することで対応は可能
# define_key_v("Ctl-x C-j", toggle_panel)

# # --------------------------------------------------------------------------------------------------

# 前に戻る
define_key(keymap_vscode, "C-A-h", self_insert_command("A-Left"))

# 次に進む
define_key(keymap_vscode, "C-A-l", self_insert_command("A-Right"))

# ドキュメントのフォーマット
define_key(keymap_vscode, "C-S-i", self_insert_command("A-S-f"))
