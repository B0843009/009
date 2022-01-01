import random #函式庫

def a(b): #排序
    c=[] #排序完後的整理
    max=0 #最大值
    for i in range(0,13): #跑1到13的回圈
        max=0
        x=""
        for j in b: #比大小
            if(int(j[1:3])>max):
                max=int(j[1:3])
                x=j
        c.append(x)
        b.remove(x)
    print(c) #輸出i
        

S=['A','B','C','D'] #建立花色
s=[] #52張卡片

for i in S: #產生52張卡片
    for j in range(1,14):
        s.append(i+str(j))

player=[] #隨機發牌
for i in range(0,4): #分成4份
    player.append(([]))
    for j in range(0,13): #分成13張
        val=random.choice(s)
        player[i].append(val)
        s.remove(val)

for i in player:
    a(i) #