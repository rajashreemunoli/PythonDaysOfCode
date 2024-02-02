#Write a program that checks if a key exists in a dictionary
cars = {'Ford':'Mustang',
		'Dodge':'Charger',
    	'Chevrolet': 'Corvette',
    	'Toyota': 'Camry',
    	'Volkswagen':'Beetle',
    	'Fiat':'500',
    	'BMW':'Mini Cooper'}


def check_key(key):
	if cars.get(key.title())!=None:
		print("We do have "+key.title()+" cars!")
	else:
		print("Sorry,we currently do have any "+key.title()+" cars.")


brand=input("Enter the car brand: ")
check_key(brand)