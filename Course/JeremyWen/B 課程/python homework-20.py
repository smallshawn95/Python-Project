import itertools #排列組合模組

letter = ['A','B','C','D','E']
shawn = 1 ; total = 1
print('可幫您排列出英文字母有幾種排列組合!!!')
ans = int(input('請輸入：'))
for x in range(1,ans+1) : 
    total *= x  #階乘計算
if ans < 1 or ans > 26 :
    print('英文有沒有學好，英文字母只有26個030')
elif ans < 6 :
    print('{}個英文字母有{:,}種排列OWO'.format(ans,total))
    for y in itertools.permutations(letter[:ans],ans):
        y = ''.join(y)
        print('{:0>3}.{}'.format(shawn,y))
        shawn += 1
else :
    print('{}個英文字母有{:,}種排列OWO'.format(ans,total))