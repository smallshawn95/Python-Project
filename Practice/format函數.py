# 原始格式：format(value, format_spec)

_ = 3.1415926
# {:.xf} 保留小數點後x位
print('{:.2f}'.format(_))
# {:+.xf} 帶符號保留小數點後x位
print('{:+.2f}'.format(_))
# {:.x%} 百分比格式取到小數點後x位
print('{:.2%}'.format(_))

__ = 5201314
# {:a>xd} a代表補多於字元的符號 x代表字元數 >代表補左邊
print('{:0>10d}'.format(__))
# {:a>xd} a代表補多於字元的符號 x代表字元數 <代表補右邊
print('{:0<10d}'.format(__))
# {:.>xd} >靠右對齊 <靠左對齊 ^置中對齊 x代表字元數
print('{:>10d}'.format(__))
print('{:<10d}'.format(__))
print('{:^10d}'.format(__))

___ = 100000000
print('{:,}'.format(___)) #逗號分隔數字
print('{:e}'.format(___)) #科學記號

____ = 10
print('{:b}'.format(____)) #二進位
print('{:d}'.format(____)) #十進位
print('{:o}'.format(____)) #八進位
print('{:x}'.format(____)) #十六進位(小寫)
print('{:X}'.format(____)) #十六進位(大寫)
