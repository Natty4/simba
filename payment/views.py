from django.shortcuts import render
import requests


def  yenepay_charge(order):
	def get_all_item():
		ItemDict = {}
		Items = []
		for item in order['items']:
			
			ItemDict['itemId'] = item['product'].id
			ItemDict['itemName'] = item['product'].name
			ItemDict['unitPrice'] = item['price']
			ItemDict['quantity'] = item['quantity']

			Items.append(ItemDict)
			ItemDict = {}

		return Items

	proccessed_data = {
		"process":"Cart",
		"successUrl":"http://localhost/api/users/profile/1",

		"merchantId":"SB1405",

		"merchantOrderId":1,

		"expiresAfter":24,

		"items": get_all_item(),

		"totalItemsDeliveryFee":"1",

		"totalItemsTax1": "1"
	}

	redirect_token = requests.post('https://test.yenepay.com/', data = proccessed_data )

	print('____________Status__________________')
	print(redirect_token.status_code)
	print('____________     __________________')
	return redirect_token

	# print(proccessed_data)
	# return proccessed_data



	# try:
	# 	requests.post('https://test.yenepay.com/', data = proccessed_data )
	# 	return True
	# except Exception:
		
	# 	return False

def tellbirr_charge(order):
	pass

def chapa_charge(order):
	pass
