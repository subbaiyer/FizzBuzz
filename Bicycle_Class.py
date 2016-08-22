# Bi-Cycle Project
# Author: R Prasana Venkateswaran
# Unit 1: Final Assignment
# Code version: 1
# Description: This code contains definitions of the classes required for this assignment

class Bicycle(object):
	def __init__(self, modelName, weight, prodCost):
		self.modelName = modelName
		self.weight = weight
		self.prodCost = prodCost
		self.salePrice = self.prodCost * 1.20
		self.Profit = self.salePrice - self.prodCost

	def __repr__(self):
		return "{0} : weights {1} lbs, costs ${2} to make, sells for ${3}.".format(self.modelName,self.weight,self.prodCost,self.salePrice)
		


class BikeShop(object):
	def __init__(self, shopName, shopInventory):
		self.shopName = shopName
		self.shopInventory = shopInventory


class Customer(object):
	def __init__(self, custName, custFunds):
		self.custName = custName
		self.custFunds = custFunds

	def __repr__(self):
		return "{0}, budget of ${1}.".format(self.custName, self.custFunds)