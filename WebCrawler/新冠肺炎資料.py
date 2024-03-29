import requests

response = requests.get("https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CVS.json", verify = False)

num = 0
for data in response.json():
    if num == 20:
        break
    print(f"編號 {num + 1:0>2}")
    print(f"病名: {data['確定病名']}")
    print(f"個案研判日: {data['個案研判日']}")
    print(f"縣市: {data['縣市']}")
    print(f"鄉鎮: {data['鄉鎮']}")
    print(f"性別: {data['性別']}")
    print(f"是否為境外移入: {data['是否為境外移入']}")
    print(f"年齡層: {data['年齡層']}")
    print(f"確定病例數: {data['確定病例數']}")
    print('-' * 30)
    num += 1
