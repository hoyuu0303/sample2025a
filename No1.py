import tkinter as tk
from tkinter import messagebox

#タイトル、定義
root = tk.Tk()
root.title("三目並べ")
buttons = []

#先行
current_player = ['○']

#勝ちパターン
win_patterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 横
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 縦
    [0, 4, 8], [2, 4, 6]              # 斜め
]

#勝敗
def check_winner():
    for pattern in win_patterns:
        if buttons[pattern[0]]['text'] == buttons[pattern[1]]['text'] == buttons[pattern[2]]['text'] != '':
            return True
    return False

#クリックしたら
def on_click(i):
    if buttons[i]['text'] == '':
        buttons[i]['text'] = current_player[0]
        if check_winner():
            messagebox.showinfo("ゲーム終了", f"プレイヤー {current_player[0]} の勝ちです！")
            root.quit()
        elif all(button['text'] != '' for button in buttons):
            messagebox.showinfo("ゲーム終了", "引き分けです。")
            root.quit()
        else:
            current_player[0] = '○' if current_player[0] == 'X' else 'X'

#画面上の設定
for i in range(9):
    pady=(10, 0)
    button = tk.Button(root, text='',font=50, bg = "#969696",width=10, height=5, command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)
    
# ラベル  ,注意書き
    label1 = tk.Label(text = "先に○から始まるよ！好きな場所をクリックしてはじめてね！", font=("Helvetica",15), foreground= "#cd5c5c")
    label1.place(x = 1, y = 0)

root.mainloop()
