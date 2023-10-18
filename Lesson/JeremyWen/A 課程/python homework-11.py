import math
shawn = ''                                                                          
for i in range(1,17):
    for j in range(1,17):
        ans = i*j
        while ans != 0 :
            num = ans%16
            ans = (ans-num)/16
            list_16=('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
            shawn = list_16[math.floor(num)]+shawn
        print('{:>4}'.format(shawn),end='')                                
        shawn = ''                                                                  
    print()