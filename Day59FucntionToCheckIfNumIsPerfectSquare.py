#Create a function that checks if a number is a perfect square
def isperfectsquare(num):
    if num<2:
        return True
    
    left,right=2,num
    while left<=right:
        mid=(left+right)//2
        if(mid**2==num):
            return True
        elif(mid**2>num):
            right=mid-1
        else:
            left=mid+1
    return False

if __name__ == '__main__':
    try:       
        check_num=int(input("Enter an integer: "))
        if(isperfectsquare(check_num)):
            print(f'{check_num} is a perfect square')
        else:
            print(f'{check_num} is not a perfect square')
    except:
        print("Invalid Entry. Enter integers only...")