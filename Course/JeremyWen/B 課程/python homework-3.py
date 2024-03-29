# 九九乘法表
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))
print('')
print('\n'.join([' '.join(['{}*{}={:<2d}'.format(y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))