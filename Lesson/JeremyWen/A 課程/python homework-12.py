# 擷取奇數位字母形成新字串
print('此程式會擷取奇數位的英文字母形成新字串OWO')
string = input('請輸入一串英文字串：')
string_amount = len(string)
print('-'*30,'\n產生出的新字串 -->',string[0:string_amount:2])