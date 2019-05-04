def DecimaltoBinary(number):
    if number > 1:
        # call the function with the result of floor division 
        # of the number by 2
        DecimaltoBinary(number // 2)
    
    # print the modules which is the binary
    print(number % 2,end="")

if __name__ == "__main__":
    num = int(input("\nEnter a number : "))
    DecimaltoBinary(num)
