import tkinter as tk
from tkinter import messagebox

# プレイヤーの記号を交互に切り替える
current_player = "○"

# 勝敗判定のための盤面（3×3）
board = [["" for _ in range(3)] for _ in range(3)]

# 勝敗を判定する関数
def check_winner():
    # 横・縦・斜めをすべてチェック：3回確認する
    for i in range(3):
        # 横
        # if board[i][0] != ""左端のセルが空じゃない（つまり、○か×が入っている）ことを確認。
        # board[i][0] == board[i][1] == board[i][2]横一列がすべて同じ記号であることを確認。つまり勝利かどうか
        # まとめ：「行 i にある3つのマスが、すべて同じ記号（○か×）で埋まっていて、かつ空ではない」ことをチェックしている、という意味です。
        # board = [
        # ["○", "○", "○"],  # i=0 ← この行をチェック
        # ["×", "",  "×"],  # i=1
        # ["",  "×", "" ]   # i=2 ]
        # 横の場合には必ず左に"i"が入る
        # つまり、iは空欄をきいている 0行目にi（空欄はいくつか）　1行目にi（空欄はいくつか） 2行目にi（空欄はいくつか）
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        # 縦の場合には必ず左に数字がはいる⇒は絶対i
        # 方法は横と同じ
        #i=1,  i=2  i=0  
        # ["", "×", "〇"],  [0 1 2]
        # ["×", "",  "〇"],  [0 1 2]
        # ["×",  "", "〇" ]  [0 1 2]
        # 0列目にiはいくつか、1列目にiはいくつか、2列目にiはいくつか
        if board[0][i] != "" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    # 斜め　二つとも数字のみ
    # {}"" and} (board[0][0] == board[1][1] == board[2][2]:)"には〇か×が入るけど、[0][0]入ってない+1、"
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

# 引き分けのチェック
def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

# ボタンが押されたときの処理
def on_click(row, col):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        winner = check_winner()
        if winner:
            messagebox.showinfo("ゲーム終了", f"{winner} の勝ち！")
            reset_game()
        elif check_draw():
            messagebox.showinfo("ゲーム終了", "引き分けです。")
            reset_game()
        else:
            current_player = "×" if current_player == "○" else "○"

# ゲームをリセット
def reset_game():
    global current_player, board
    current_player = "○"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")
          

# ウィンドウ作成
root = tk.Tk()
root.title("○×ゲーム!!")

# ボタン作成（3×3）
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", width=4, height=2,
                        font=("Arial", 40),
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn

root.mainloop()

