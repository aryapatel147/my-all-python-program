import math

print("Welcome to the Data Analyzer and Transformer Program")

data = []

def filter_data():
    threshold = int(input("Enter a threshold value: "))
    filtered = [x for x in data if x >= threshold]
    print(f"Filtered Data (>= {threshold}):", filtered)

def sort_data():
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Ascending:", sorted(data))
    elif choice == "2":
        print("Descending:", sorted(data, reverse=True))
    else:
        print("Invalid choice")

def display_dataset():
    print("Dataset Statistics:")
    print("Min:", min(data))
    print("Max:", max(data))
    print("Sum:", sum(data))
    print("Average:", sum(data)/len(data))

while True:
    print("\nMain Menu")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Factorial")
    print("4. Filter Data")
    print("5. Sort Data")
    print("6. Dataset Statistics")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = list(map(int, input("Enter numbers (space separated): ").split()))
        print("Data stored successfully")

    elif choice == 2:
        print("Summary:")
        print("Total:", len(data))
        print("Min:", min(data))
        print("Max:", max(data))
        print("Sum:", sum(data))
        print("Average:", sum(data)/len(data))

    elif choice == 3:
        num = int(input("Enter a number: "))
        print("Factorial of", num, "is", math.factorial(num))

    elif choice == 4:
        filter_data()

    elif choice == 5:
        sort_data()

    elif choice == 6:
        display_dataset()

    elif choice == 7:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
