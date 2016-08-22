# Bicycle_Test.py
# Author: R Prasana Venkateswaran
# Unit 1 Assignment
# Code version: 1
# Description: This code contains transactions on the 
# classes defined in the Bicycle_Class.py code


# CREATE BICYCLE MODELS
import random
from Bicycle_Class import Bicycle
from Bicycle_Class import Customer
from Bicycle_Class import BikeShop

if __name__ == '__main__':
	bike1 = Bicycle("Cannondale", 28, 150)
	bike2 = Bicycle("Trek", 29, 999)
	bike3 = Bicycle("Windsor", 32, 170)
	bike4 = Bicycle("Fuji", 30, 350)
	bike5 = Bicycle("Mercier", 31, 450)
	bike6 = Bicycle("Motobecane", 33, 807)

inventoryList = [bike1, bike2, bike3, bike4, bike5, bike6]


if __name__ == '__main__':
	shop = BikeShop("Trekker Bikes",6)
	print("\n The Store is {0} with {1} bikes.\n".format(shop.shopName,shop.shopInventory))


# CREATE CUSTOMERS
if __name__ == '__main__':
	customer1 = Customer("Dave",200)
	customer2 = Customer("Chan",500)
	customer3 = Customer("Ethan",1000)

customerList = [customer1, customer2, customer3]


# PRINT CUSTOMER AND INVENTORY LIST
print("List of Customers is:")
for cust in range(len(customerList)):
	print(customerList[cust])


print("\nBicycle Inventory currently is:")
for inv in range(len(inventoryList)):
	print(inventoryList[inv])


# PRINT WHAT THE CUSTOMER CAN AFFORD
for cust in range(len(customerList)):
	print("\n" + customerList[cust].custName + "  can afford the following bike models: ")
	for bke in range(len(inventoryList)):
		if (inventoryList[bke].salePrice) <= customerList[cust].custFunds:
			print(inventoryList[bke])


# RECORD WHAT THE CUSTOMER CAN AFFORD INTO A DICTIONARY
custAfford = { }
for cust in range(len(customerList)):
	if customerList[cust].custName not in custAfford:
		custAfford[customerList[cust].custName] = []
	for bke in range(len(inventoryList)):
		if (inventoryList[bke].salePrice) <= customerList[cust].custFunds:
			custAfford[customerList[cust].custName].append(inventoryList[bke].modelName)
	
print("\nAffordability")
print(custAfford)
print()

# PRINT CUSTOMER PURCHASE
custPurch = {}
for cust in range(len(customerList)):
	if customerList[cust].custName not in custPurch:
		custPurch[customerList[cust].custName] = []

for cust in range(len(customerList)):
	custPurch[customerList[cust].custName] = random.choice(custAfford[customerList[cust].custName])	


print("\nCustomer Purchase")
print(custPurch)
print()

for cust in range(len(customerList)):
	print("Details of Sale to " + customerList[cust].custName + ": ")
	print("Model purchased :" + custPurch[customerList[cust].custName])
	for inv in range(len(inventoryList)):
		if custPurch[customerList[cust].custName] == inventoryList[inv].modelName :
			print(inventoryList[inv])
			print("Funds left = $", customerList[cust].custFunds - inventoryList[inv].salePrice)
			print("Store Profit = $", inventoryList[inv].Profit, "\n")
		else:
			continue
		
# CALCULATE REMAINING STORE INVENTORY AND TOTAL PROFIT
totalProfit = 0
for cust in range(len(customerList)):	
	for inv in range(len(inventoryList)):
		if custPurch[customerList[cust].custName] == inventoryList[inv].modelName :
			totalProfit = totalProfit + inventoryList[inv].Profit


newInventory = [bike1.modelName, bike2.modelName, bike3.modelName, bike4.modelName, bike5.modelName, bike6.modelName]
for pr in range(len(custPurch)):
	for cust in range(len(custPurch)):
		if newInventory.count(custPurch[customerList[cust].custName])==1:
			newInventory.remove(custPurch[customerList[cust].custName])

print("New store inventory is: ")
print(newInventory)
print("Total store profit is: ", round(totalProfit,2))
