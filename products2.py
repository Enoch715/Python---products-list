#建立商品清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q' or name == 'Q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price]) 
	print('')
with open('products.csv', 'w') as file:
	for p in products:
		file.write(p[0] + ',' + p[1] + '\n')

#查詢商品價格
while True:
	productname = input('請輸入要查詢的商品: ')
	print('')
	if productname == 'q' or productname == 'Q':
		break
	with open('products.csv', 'r') as pdlist:
		for product in pdlist:
			if productname in product: 
				print('所查詢的商品: ', product)
				print('')