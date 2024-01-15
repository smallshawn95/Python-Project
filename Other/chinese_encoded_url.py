from urllib.parse import quote

chinese_url = "https://www.google.com.tw/search?q=哈囉，世界！"
encoded_url = quote(chinese_url, safe = ";/?:@&=+$,", encoding = "utf8")

print(encoded_url)
