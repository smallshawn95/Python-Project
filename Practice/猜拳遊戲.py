import random

computer = int(random.randint(0,2))
print("歡迎遊玩猜拳遊戲OUO!!!")
rock = chr(9994)
paper = chr(9995)
scissors = chr(9996)
print("{0} 剪刀「2」{1}石頭「0」{2}布「1」".format(scissors,rock,paper))
player = int(input("玩家出拳(輸入數字)："))
if player == 0 :
    print("玩家出拳{}".format(rock))
    if computer == 0 :
        print("電腦出拳{}".format(rock))
        print("此次平局，兩位並駕齊驅OWO")
    elif computer == 1 :
        print("電腦出拳{}".format(paper))
        print("電腦勝利，電腦舉世無雙OWO")
    else :
        print("電腦出拳{}".format(scissors))
        print("玩家勝利，玩家神機妙算OWO")
elif player == 1 :
    print("玩家出拳{}".format(paper))
    if computer == 0 :
        print("電腦出拳{}".format(rock))
        print("玩家勝利，玩家足智多謀OWO")
    elif computer == 1 :
        print("電腦出拳{}".format(paper))
        print("此次平局，兩位不分軒輊OWO")
    else :
        print("電腦出拳{}".format(scissors))
        print("電腦勝利，電腦登峰造極OWO")
elif player == 2 :
    print("玩家出拳{}".format(scissors))
    if computer == 0 :
        print("電腦出拳{}".format(rock))
        print("電腦勝利，電腦以一當十OWO")
    elif computer == 1 :
        print("電腦出拳{}".format(paper))
        print("玩家勝利，玩家獨孤求敗OWO")
    else :
        print("電腦出拳{}".format(scissors))
        print("此次平局，兩位平分秋色OWO")
else :
    print("別當作者不知道你的想法OWO，請輸入正確數字!!!")