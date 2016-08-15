# Author: R Prasana Venkateswaran
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


# Function to get customer preference
# Responses are recorded in the custPref dictionary
def drinkStyle ():
 custPref = {}
 print('Answer only y or Y (for Yes) to the following questions')

 strong1 = input(questions['strong'] + ": ")
 if (strong1[0] == 'y' or strong1[0] == 'Y'):
    custPref['strong'] = True
 else:
    custPref['strong'] = False
        
 salt1 = input(questions['salty'] + ": ")
 if salt1[0] =='y' or salt1[0] == 'Y':
    custPref['salty'] = True
 else:
    custPref['salty'] = False

 bitter1 = input(questions['bitter'] + ": ")
 if bitter1[0] == 'y' or bitter1[0] == 'Y':
    custPref['bitter'] = True
 else:
    custPref['bitter'] = False

 sweet1 = input(questions['sweet'] + ": ") 
 if sweet1[0] == 'y' or sweet1[0] == 'Y':
    custPref['sweet'] = True
 else:
    custPref['sweet'] = False

 fruity1 = input(questions['fruity'] + ": ")
 if fruity1[0] == 'y' or fruity1[0] == 'Y':
    custPref['fruity'] = True
 else:
    custPref['fruity'] = False
    print('Your choices are:')
    print()
    print(custPref)
    return custPref


# For the customer preference as input, make a drink
def makeDrink(custPref):
    drink = {}
    if custPref['strong'] == True:
        drink['strong']= random.choice(ingredients['strong'])
        
    if custPref['salty'] == True:
        drink['salty'] = random.choice(ingredients['salty'])
        
    if custPref['bitter'] == True:
        drink['bitter'] = random.choice(ingredients['bitter'])
        
    if custPref['sweet'] == True:
        drink['sweet'] = random.choice(ingredients['sweet'])
        
    if custPref['fruity'] == True:
        drink['fruity'] = random.choice(ingredients['fruity'])
        
    return drink
    
def main():
    custResponse = drinkStyle()
    drink = makeDrink(custResponse)
    print()
    print('The contents of the drink are:')
    for i in drink:
        print(drink[i])
        
if __name__ == '__main__':
    main()
