import os # operating system
 #讀取商品清單
def read_file(filename):
	products = []
	with open (filename, 'r', encoding='utf-8') as pdlist:
		for line in pdlist:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)
	return  products
#建立商品清單
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q' or name == 'Q':
			break
		elif name in str(products):
			print('此商品已在清單中')
			print('')
		else:
			price = int(input('請輸入商品價格: '))
			products.append([name, price]) 
			print('')
	return products
#將商品清單寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as file:
		file.write('商品,價格\n')
		for p in products:
			file.write(p[0] + ',' + str(p[1]) + '\n')
#查詢商品價格
def search_price(filename):
	while True:
		choose = 0
		productname = input('請輸入要查詢的商品: ')
		print('')
		if productname == 'q' or productname == 'Q':
			break
		with open(filename, 'r', encoding='utf-8') as pdlist:
			for product in pdlist:
				name, price = product.strip().split(',')
				if productname in product: 
					print('所查詢的商品: ', name, '價格:', price, '元')
					print('')
					choose = 1
					break
			if choose == 0:
				print('查無此產品')
				print('')		
#主程式進行
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('找到商品清單內容如下:')
		products = read_file(filename)
	else:
		print('未找到商品清單')
		products = []
	choose01 = input('是否編輯商品清單(y/n): ')
	if choose01 == 'n':
		if len(products) > 0  :
			choose02 = input('是否查詢商品價錢(y/n): ')
			if choose02 == 'y':
				search_price(filename)
	else:
		products = user_input(products)
		write_file(filename, products)
		choose02 = input('是否查詢商品價錢(y/n): ')
		if choose02 == 'y':
			search_price(filename)

main()