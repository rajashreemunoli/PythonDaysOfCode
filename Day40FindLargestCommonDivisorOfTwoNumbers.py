#Write a function to find the largest common divisor of two numbers using a function
def lcd_two_numbers(num1,num2):
	if num1==0:
		return num2

	if num2==0:
		return num1

	if num1==num2:
		return num1

	if num1>num2:
		return lcd_two_numbers(num1-num2,num2)
	return lcd_two_numbers(num1,num2-num1)

try:
	x=int(input("Enter the first number: "))
	y=int(input("\nEnter the second number: "))
	print(f"\nLargest Common Divisor of {x} and {y} is: ",lcd_two_numbers(x,y))
except Exception as e:
	print('Invalid Entry. Please try again.')