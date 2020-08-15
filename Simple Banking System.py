# BANKING SYSYTEM


print("=====================================")

customerNames = ['Sachin Tendulkar', 'Sourav Ganguli', 'Virat Kohli', 'MS DHONI']
customerPins = ['7002', '8876', '0342', '9063']
customerBalances = [9000000, 8000000,6440000, 9440000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 4
i = 0

while True:
    print("=====================================")
    print(" ----Welcome to Times Bank----       ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")
    choiceNumber = input("Select your choice number from menu given above : ")
    if choiceNumber == "1":
        print("Choice number 1 is selected by the customer")
        c = eval(input("Number of Customers : "))
 
        i = i + c
        if i > 5:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i = i - c
        else:
            while counter_1 <= i:
                name = input("Input Fullname : ")
                customerNames.append(name)
                pin = str(input("Please input a pin of your choice : "))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("Please input a value to deposit to start an account : "))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("Pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(customerBalances[counter_2], end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(customerNames)
                print("\n")
                print("Please remember the Name and Pin")
                print("========================================")

        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "2":
        j = 0
        print("Choice number 2 is selected by the customer")
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        withdrawal = eval(input("Input value to Withdraw : "))
                        if withdrawal > balance:
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n")
                            balance = balance - withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            balance = balance - withdrawal
                            print("\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "3":
        print("Choice number 3 is selected by the customer")
        n = 0
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        print("Your Current Balance: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
