print("welcome to pattern generator and number analyzer\n")

while True: 
    print("select an option:")
    print("1. generate a pattern")
    print("2. analyze a range of numbers")
    print("3. exit")

    user = int(input("Enter the choice number: "))

    if user == 1:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        i = 1
        while i <= rows:
            j = 1
            while j <= i and j <= cols:
                print("*", end="")
                j += 1
            print()
            i += 1

    elif user == 2:
        a = int(input("enter the start number :- "))
        b = int(input("enter the end number :- "))

        total = 0
        for number in range(a, b + 1):
            if number % 2 == 0:
                print(f"number {number} even")
            else:
                print(f"number {number} odd")
                total += number
        print(f"sum of all odd numbers {a} to {b} is: {total}\n")

    elif user == 3:
        print("Exiting program... Goodbye!")
        break  
    else:
        print("Invalid option! Please select 1, 2, or 3.\n")
