# 星星三角形進階版
shawn = 1 ; shung = 2
for x in range(1,13) :
    if x <= 3 or x%3 == 0 :
        for y in range(1,x+1) :
            print('*',end='')
    elif x%3 == 1:
        for y in range(1,x-shawn) :
            print('*',end='  ')
        shawn += 2
    elif x%3 == 2 :
        for y in range(1,x-shung) :
            print('**',end=' ')
        shung += 2
    print()