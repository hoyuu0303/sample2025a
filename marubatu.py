import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

##############################################
# 座標を指定してつくってみよう（課題）
##############################################

#class Application(tk.Frame):
    #def __init__(self, master = None):
        #super().__init__(master)

        #root.title("○×ゲーム")     # ウィンドウタイトル
       # self.master.geometry("450x500")       # ウィンドウサイズ(幅x高さ)

         

# 勝敗を判定する関数
def check_winner():
    for pattern in win_patterns:
        if buttons[pattern[0]]['text'] == buttons[pattern[1]]['text'] == buttons[pattern[2]]['text'] != '':
            return True
    return False

# ####ボタンが押されたときの処理
  # 画像のパス（同じフォルダに image1.png と image2.png を置く）
    image_paths = [ "C:/Users/hetar/Desktop/金4/image1.png",
                "C:/Users/hetar/Desktop/金4/image2.png"]
    images = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]
    current_index = 0

# ラベルに最初の画像を表示
    label = tk.Label(root, image=images[current_index])
    label.pack()

# 画像クリックで切り替える関数
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
            current_player[0] = 'O' if current_player[0] == 'X' else 'X'

    #def switch_image(event=None):
     #   global current_index
      #  current_index = (current_index + 1) % len(images)
    #label.config(image=images[current_index])

# ラベルをクリックしたら切り替え
   # label.bind("<Button-1>", switch_image)

# ラベル  ,注意書き
    label1 = tk.Label(text = "先に○から始まるよ！好きな場所をクリックしてはじめてね！", font=("Helvetica",11), foreground= "#cd5c5c")
    label1.place(x = 1, y = 1)

# ○からはじまる
    current_player = "○"

    buttons = []
    #current_player = ['X']

win_patterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 横
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 縦
    [0, 4, 8], [2, 4, 6]              # 斜め
]
# ボタンの作成

for i in range(9):
        button1 = tk.Button(root, text = "", bg = "#969696")
        button1.place(x = 1, y = 40, width = 150, height = 150) 

        button2 = tk.Button(self.master, text = "", bg = "#969696")
        button2.place(x = 150, y = 40, width = 150, height = 150) 

        button3 = tk.Button(self.master, text = "", bg = "#969696")
        button3.place(x = 300, y = 40, width = 150, height = 150)

        button4 = tk.Button(self.master, text = "", bg = "#969696")
        button4.place(x = 1, y = 190, width = 150, height = 150) 

        button5 = tk.Button(self.master, text = "", bg = "#969696")
        button5.place(x = 150, y = 190, width = 150, height = 150) 

        button6 = tk.Button(self.master, text = "", bg = "#969696")
        button6.place(x = 300, y = 190, width = 150, height = 150) 

        button7 = tk.Button(self.master, text = "", bg = "#969696")
        button7.place(x = 1, y = 340, width = 150, height = 150) 

        button8 = tk.Button(self.master, text = "", bg = "#969696")
        button8.place(x = 150, y = 340, width = 150, height = 150) 

        button9 = tk.Button(self.master, text = "", bg = "#969696")
        button9.place(x = 300, y = 340, width = 150, height = 150)  


root = tk.Tk()
root.mainloop()

#############################################################################
import tkinter as tk
from tkinter import messagebox

def check_winner():
    for pattern in win_patterns:
        if buttons[pattern[0]]['text'] == buttons[pattern[1]]['text'] == buttons[pattern[2]]['text'] != '':
            return True
    return False

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
            current_player[0] = 'O' if current_player[0] == 'X' else 'X'

root = tk.Tk()
root.title("三目並べ")

buttons = []
current_player = ['X']
win_patterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 横
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 縦
    [0, 4, 8], [2, 4, 6]              # 斜め
]

for i in range(9):
    button = tk.Button(root, text='', width=10, height=5, command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()
