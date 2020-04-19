# 先計算字的計數
# 讓使用者輸入這個字輸入過幾次

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有',len(data),'筆資料' )
print(data[0])


#文字計數
wc = {} #word_count 建立一個字典
for d in data: #讀取每一筆留言
	words = d.split() #d是一筆留言 用空格做切割
	for word in words:
		if word in wc: #如果這個字出現在字典裡我們就
			wc[word] += 1 #我們就把目前的次數加一
		else: #如果沒有的話
			wc[word] = 1 #新增新的key進wc字典
for word in wc: #每一個key(word)被字典叫出來
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Tina'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:',wc[word])
	else:
		print('這個字沒有出現過喔')
print('感謝使用本查詢功能')