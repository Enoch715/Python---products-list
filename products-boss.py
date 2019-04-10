#檢查是否有商品清單並且讀取
import os # operating system
products = []
if os.path.isfile('products.csv'): #檢查商品清單是否存在
	print('找到商品清單內容如下:')
#讀取商品清單
	with open ('products.csv', 'r', encoding='utf-8') as pdlist:	
		for line in pdlist:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	add = input('是否要建立新商品清單(y/n): ')
else: 
	print('未找到商品清單開始建立')
#建立商品清單
if add =='y':
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q' or name == 'Q':
			break
		elif name in products:
			print('此商品已在清單中')
			print('')
		else:
			price = int(input('請輸入商品價格: '))
			products.append([name, price]) 
			print('')

#將商品清單寫入檔案
	with open('products.csv', 'w', encoding='utf-8') as file:
		file.write('商品,價格\n')
		for p in products:
			file.write(p[0] + ',' + str(p[1]) + '\n')
search = input('是否需要查詢商品價格(y/n): ')

#查詢商品價格
if search == 'y':
	while True:
		productname = input('請輸入要查詢的商品: ')
		print('')
		if productname == 'q' or productname == 'Q':
			break
		with open('products.csv', 'r', encoding='utf-8') as pdlist:
			for product in pdlist:
				name, price = product.strip().split(',')
				if productname in product: 
					print('所查詢的商品: ', name, '價格:', price, '元')
					print('')