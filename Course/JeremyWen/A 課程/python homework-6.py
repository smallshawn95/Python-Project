# 九九乘法表矩狀圖

# 第一種寫法
print('\n'.join (" ".join("%2d" % (s*h) for s in range(1,10)) for h in range(1,10)))

print()

# 第二種寫法
for i in range(1,10) :
    for j in range(1,10) :
        if i*j < 10 :
            print('',i*j,end=' ')
        else:
            print(i*j,end=' ')
    print(end='\n')