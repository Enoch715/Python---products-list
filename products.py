#建立商品清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q' or name == 'Q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price]) 
	print('')
#查詢商品價格
while True:
	productname = input('請輸入要查詢的商品: ')
	print('')
	if productname == 'q' or productname == 'Q':
		break
	for product in products:
		if productname in product: 
			print('所查詢的商品: ', product[0], '價格為: ', product[1], '元')
			print('')