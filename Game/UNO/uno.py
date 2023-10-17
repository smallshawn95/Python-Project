import random

def start_game():
    '''遊戲開始'''
    global deck, hand, uno_color, reverse
    print(f"{'-' * 30}\n|| Game Start ||\n{'-' * 30}")
    deck = []
    hand = []
    reverse = 1
    uno_color = {"r": "🟥", "y": "🟨", "g": "🟩", "b": "🟦", "any": "⬛"}
    input_player_number()
    init_deck()
    first_down_card()
    decide_order()
    run_game()

def run_game():
    '''遊戲運行'''
    show_down_card()
    show_player_hand()
    play_player_card()

def end_game():
    '''遊戲結束'''
    for i in range(player_num):
        if len(hand[i]) == 0:
            print(f"{i + 1} 號玩家獲得 UNO 遊戲勝利")
            quit()

def init_deck():
    '''初始化'''
    for color in ["r", "y", "g", "b"]:
        deck.append((color, "0"))
        for i in range(2):
            for number in range(1, 10):
                deck.append((color, str(number)))
            deck.append((color, "skip"))
            deck.append((color, "reverse"))
            deck.append((color, "draw_two"))
    for i in range(4):
        deck.append(("any", "wild"))
        deck.append(("any", "wild_draw_four"))
    shuffle_deck()
    deal_deck()

def shuffle_deck():
    '''洗牌'''
    for i in range(random.randint(1, 5)):
        random.shuffle(deck)

def deal_deck():
    '''發牌'''
    for i in range(player_num):
        hand.append([])
    for i in range(7):
        for player in range(player_num):
            hand[player].append(deck.pop())

def first_down_card():
    '''放置首張底牌'''
    global down_card
    while True:
        down_card = deck.pop()
        if not down_card[0] == "any":
            break

def add_player_card(num: int):
    '''增加玩家手牌'''
    for i in range(num):
        hand[order].append(deck.pop())

def decide_order():
    '''決定玩家順序'''
    global order
    order = random.randint(0, player_num - 1)

def input_player_number():
    '''輸入遊戲遊玩人數'''
    global player_num
    while True:
        player_num = int(input("Input Player Number: "))
        if player_num >= 2:
            break
        print("UNO 遊戲遊玩人數至少 2 人")
    print('-' * 30)

def reverse_order(reverse: int):
    '''迴轉玩家順序'''
    if player_num == 2:
        reverse = 2 * reverse
    else:
        reverse = -1 if reverse == 1 else 1
    return reverse

def next_order(next: int):
    '''更新下一位玩家順序'''
    global order
    order += next
    if order >= player_num:
        order -= player_num
    elif order < 0:
        order += player_num

def play_player_card():
    '''玩家出牌'''
    global reverse, down_card
    add_num = 0
    next = reverse
    while True:
        card_num = input("Input Card Number or Pass: ")
        if card_num == "pass" or card_num == "Pass":
            hand[order].append(deck.pop())
            break
        play_card = hand[order][int(card_num) - 1]
        if int(card_num) < 1 or int(card_num) > len(hand[order]):
            print("輸入不存在的卡片編號")
        else:
            print(f"出牌: {uno_color[play_card[0]]} {play_card[1]}")
            if play_card[0] == "any":
                color = int(input("Input Number(1 Red/2 Yellow/3 Green/4 Blue): "))
                if play_card[1] == "wild_draw_four":
                    add_num = 4
                down_card = (['r', 'y', 'g', 'b'][color - 1], "any")
                del hand[order][int(card_num) - 1]
                break
            elif play_card[0] == down_card[0] or play_card[1] == down_card[1]:
                down_card = play_card
                del hand[order][int(card_num) - 1]
                if play_card[1] == "skip":
                    next = 2 * reverse
                elif play_card[1] == "reverse":
                    next = reverse_order(reverse)
                elif play_card[1] == "draw_two":
                    add_num = 2
                break
            else:
                print("與底牌顏色、點數、種類不同")
    next_order(next)
    add_player_card(add_num)
    print('-' * 30)
    end_game()
    run_game()

def sort_player_hand():
    '''排序玩家手牌'''
    sort_hand = sorted(hand[order])
    return sort_hand

def show_down_card():
    '''查看底牌'''
    print(f"牌堆還剩 {len(deck)} 張，底牌 {uno_color[down_card[0]]} {down_card[1]}")

def show_player_hand():
    '''查看玩家手牌內容'''
    print(f"輪到遊戲 {order + 1} 號玩家，手牌還剩 {len(hand[order])} 張")
    hand[order] = sort_player_hand()
    for i in range(len(hand[order])):
        if i == len(hand[order]) - 1:
            print(f"{str(i + 1).zfill(2)}: {uno_color[hand[order][i][0]]} {hand[order][i][1]}")
        else:
            print(f"{str(i + 1).zfill(2)}: {uno_color[hand[order][i][0]]} {hand[order][i][1]}", end = " || ")

if __name__ == "__main__":
    start_game()