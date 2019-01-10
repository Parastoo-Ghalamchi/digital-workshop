print("hello")
#This is Collatz program that creates a Collatz series

def Collatz(number):
        if number % 2 == 0:
                return number // 2
        elif number % 2 == 1:
                return 3 * number + 1
while True:
        num = int(input("enter a number"))
        print(Collatz(num))
        

            
        
        
        
        
    
	
