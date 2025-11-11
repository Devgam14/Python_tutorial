#main loop start 
while True:
    print("Welcome to my controlled multiplying program")
#User prompt input
    next = int(input("Enter any option below \nEnter 1 to start and enter 2 to exit \n1. Start \n2. Exit \n"))
#Main code block 
    if next == 1 :
        print("\nTerms and condition :\n1. Pls note that the start number must be lower than the stop number \n2. The stop number must be higher than the start number\n3. Pls follow all these rules so as not get an error\n")
#Collecting data through input
        multiplier = int(input("Pls enter multiplying number : "))
        start_num = int(input("Pls enter the start number of the multiplication : "))
        stop_num = int(input("Pls enter the limit number you want to be multiplied : "))
        if stop_num < start_num:

            print("Invalid stop number \nStop number shuld be greater than start number\n ")
            continue
        else:
#multiplying loop
            while start_num <= stop_num:
                print(f" {multiplier} * {start_num} = {multiplier * start_num}")
                start_num += 1
        print("\nRestarting program ........\n")
#The continue keyword restarts the loop 
        continue
#Main loop breaker 
    elif next == 2 :
      break
    else :
#Error handling block 
        print("Pls enter 1 or 2 below \n")
        continue