products = []
while True:
	name = input('請輸入商品名稱(如果要退出請輸入q or Q): ')
	if name == 'q' or name == 'Q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price]) 
print(products)