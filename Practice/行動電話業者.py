print('輸入行動電話號碼可查詢電信業者OWO')
cellphone_number = input('請輸入(數字十碼)：')
ans = int(cellphone_number[1:4])
if ans == 910 or ans == 911 or ans == 912 or \
   ans == 919 or ans == 921 or ans == 928 or \
   ans == 932 or ans == 933 or ans == 934 or \
   ans == 937 or ans == 963 or ans == 972 or \
   ans == 975 or ans == 978 or ans == 988 :
    print('電信業者為「中華電信」')
elif ans == 914 or ans == 918 or ans == 920 or \
     ans == 922 or ans == 923 or ans == 924 or \
     ans == 929 or ans == 935 or ans == 939 or \
     ans == 952 or ans == 953 or ans == 956 or \
     ans == 958 or ans == 961 or ans == 970 or \
     ans == 979 or ans == 983 or ans == 987 :
   print('電信業者為「台灣大哥大」')
elif ans == 913 or ans == 915 or ans == 916 or \
     ans == 917 or ans == 925 or ans == 926 or \
     ans == 927 or ans == 930 or ans == 936 or \
     ans == 938 or ans == 954 or ans == 955 or \
     ans == 976 or ans == 981 or ans == 984 or \
     ans == 989 :
   print('電信業者為「遠傳電信」')
elif ans == 973 or ans == 986 :
   print('電信業者為「威寶電信」')
elif ans == 977 or ans == 980 or ans == 982 or \
     ans == 985 :
   print('電信業者為「亞太電信」')
elif ans == 966 or ans == 968 :
   print('電信業者為「大眾電信」')
elif ans == 931 or ans == 960 :
   print('電信業者為「台灣大哥大或遠傳電信」')
elif ans == 971 :
   print('電信業者為「台灣大哥大或威寶電信」')
else :
   print('查無此電話號碼的電信業者QQ')
