import random

# 讀檔
f = open("words_alpha.txt",'r')

# 建立單字庫
arr = [[0] for _ in range(32)]
for w in f.readlines():
    arr[len(w) - 1].append(w)

# 定義顏色
class colors:
        green = '\033[92m' # 有字母且位置正確
        yellow = '\033[93m' # 有字母但位置不對
        gray = '\033[90m' # 無字母
        red = '\033[91m'
        blue = '\033[94m'
        cyan = '\033[96m'
        magenta = '\033[95m'
        reset = '\033[0m'

# 統計數據
played = 0 # 玩了幾場
win = 0 # 贏了幾場
lose = 0 # 輸了幾場
currentstreak = 0 # 目前連勝幾場
maxstreak = 0 # 最高連勝幾場

# 遊戲
while True:
    # 鍵盤
    key = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\n', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '\n', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '\n']
    keycolor = [0] * 29
    #  0 : 還沒猜過
    #  1 : 有字母且位置正確
    #  2 : 有字母但位置不對
    #  3 : 無字母
    
    # 決定失敗容許次數
    while True:
        time = input(colors.cyan + "失敗容許次數 : " + colors.reset)
        timenum = 1 # 判斷time是否為數字
        for tt in time:
            if tt < '0' or tt > '9':
                timenum = 0
                break
        if timenum == 1:
            time = int(time)
            break
        else:
            print(colors.red + "輸入數字啦" + colors.reset)
    # 決定單字長度
    while True:
        wordlen = input(colors.cyan + "單字長度 : " + colors.reset)
        wordlennum = 1 # 判斷worlennum是否為數字
        for ww in wordlen:
            if ww < '0' or ww > '9':
                wordlennum = 0
                break
        if wordlennum == 1:
            wordlen = int(wordlen)
            if wordlen < 1 or wordlen > 31:
                print(colors.red + "沒有這個長度的單字喔~再輸入一次" + colors.reset)
            elif wordlen == 26 or wordlen == 30:
                print(colors.red + "沒有這個長度的單字喔~再輸入一次" + colors.reset)
            else:
                break
        else:
            print(colors.red + "輸入數字啦" + colors.reset)
    # 決定題目
    while True:
        word = random.choice(arr[wordlen])
        if type(word) == int:
            continue
        else:
            word, space = word.split('\n')
            break
    # print("題目 : ", word)

    played += 1
    bingo = 0 # 記錄有沒有猜中

    # 開始猜
    print()
    print(colors.magenta + "遊戲開始!!" + colors.reset)
    t = 1 # 記錄猜到第幾次
    while t <= time:
        # 鍵盤
        print("--------------------")
        for k in range(len(key)):
            if key[k] == '\n':
                print()
            else:
                if keycolor[k] == 1:
                    print(colors.green + key[k] + colors.reset, end = ' ')
                elif keycolor[k] == 2:
                    print(colors.yellow + key[k] + colors.reset, end = ' ')
                elif keycolor[k] == 3:
                    print(colors.gray + key[k] + colors.reset, end = ' ')
                else:
                    print(key[k], end = ' ')
        print("--------------------")

        print(colors.cyan + "第", t, "次回答 : " + colors.reset, end = '')
        guess = input()

        # 開始判斷
        wordguess = [0] * wordlen # 紀錄是否被猜過
        if len(guess) == wordlen: # 單字長度符合
            if guess + '\n' in arr[wordlen]: # 單字在單字庫內
                for g in range(wordlen):
                    if guess[g] == word[g]:
                        wordguess[g] = 1

                cnt = 0 # 計算有幾個位置正確的字母
                for i in range(wordlen):
                    num = key.index(guess[i]) # 知道字母在key裡的index
                    if guess[i] == word[i]:
                        keycolor[num] = 1
                        print(colors.green + guess[i] + colors.reset, end = '')
                        cnt += 1
                    else:
                        yes = 0
                        for j in range(wordlen):
                            if guess[i] == word[j] and wordguess[j] != 1:
                                if keycolor[num] != 1:
                                    keycolor[num] = 2
                                wordguess[j] = 1
                                print(colors.yellow + guess[i] + colors.reset, end = '')
                                yes = 1
                                break
                        if yes == 0:
                            if keycolor[num] == 0:
                                keycolor[num] = 3
                            print(colors.gray + guess[i] + colors.reset, end = '')
                print()
                if cnt == wordlen:
                    print(colors.magenta + "恭喜你猜中了!!" + colors.reset)
                    win += 1
                    currentstreak += 1
                    bingo = 1
                    break

                t += 1
            else: # 單字不在單字庫內
                print(colors.red + "單字不在單字庫內，這次不算，再猜一次" + colors.reset)
        else: # 單字長度不符
            print(colors.red + "單字長度不符，這次不算，再猜一次" + colors.reset)

    # 如果沒猜中
    if bingo == 0:
        print(colors.magenta + "好可惜沒猜中" + colors.reset)
        print("正確答案為 :", colors.green + word + colors.reset) # 公布答案
        lose += 1
        currentstreak = 0 # 目前連勝場數歸零
    # 更新最高連勝場數
    if currentstreak >= maxstreak:
        maxstreak = currentstreak

    # 數據
    print()
    print("statistics :")
    print("玩了", played, "場")
    print("贏了", win, "場")
    print("輸了", lose, "場")
    print("勝率 :", 100 * win // played, "%")
    print("目前連勝", currentstreak, "場")
    print("最高連勝", maxstreak, "場")
    print()

    while True:
        ans = input(colors.cyan + "還要玩嗎(Y/N) :" + colors.reset)
        if ans == 'N' or ans == 'n':
            print(colors.magenta + "不玩那掰掰" + colors.reset)
            break
        elif ans == 'Y' or ans == 'y':
            print(colors.magenta + "好玩一直玩" + colors.reset)
            break
        else:
            print("不要亂輸入= =")
    if ans == 'N' or ans == 'n':
        break # 結束遊戲
    print()

f.close()