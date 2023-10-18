#十進位制轉換成二進位制、八進位制、十六進位制
print('輸入一個數字將轉換成二進位制、八進位制、十六進位制OWO')
ans_number = int(input('請輸入 --> '))
Binary = format(ans_number,'b')          # "b"是format( )函數中將數值轉換為二進位制的代號
Octal = format(ans_number,'o')           # "o"是format( )函數中將數值轉換為八進位制的代號
Hexadecimal = format(ans_number,'x')     # "x"是format( )函數中將數值轉換為十六進位制的代號
print('-'*30,'\n二進位制 --> {0}\n八進位制 --> {1}\n十六進位制 --> {2}'.format(Binary,Octal,Hexadecimal))