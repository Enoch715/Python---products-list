#建立商品清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q' or name == 'Q':
		break
	price = int(input('請輸入商品價格: '))
	products.append([name, price]) 
	print('')
with open('products.csv', 'w', encoding='utf-8') as file:
	file.write('商品,價格\n')
	for p in products:
		file.write(p[0] + ',' + str(p[1]) + '\n')
search = input('是否需要查詢商品(y/n): ')
#查詢商品價格
if search == 'y':
	while True:
		productname = input('請輸入要查詢的商品: ')
		print('')
		if productname == 'q' or productname == 'Q':
			break
		with open('products.csv', 'r', encoding='utf-8') as pdlist:
			for product in pdlist:
				if productname in product: 
					print('所查詢的商品: ', product)
					print('')