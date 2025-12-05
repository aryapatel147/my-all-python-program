import numpy as np
from arrcreat import one_array, two_array, three_array, indexing_one, slicing_two


class DataAnalytics:
    def __init__(self):
        self.array = None

    #  ARRAY CREATION MENU
    def create_array_menu(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            one_array(self)
        elif choice == 2:
            two_array(self)
        elif choice == 3:
            three_array(self)
        else:
            print("Invalid choice")
            return

        print("\nArray created successfully:")
        print(self.array)

        self.index_slice_menu()

    #  INDEX & SLICE MENU
    def index_slice_menu(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                indexing_one(self)
            elif choice == 2:
                slicing_two(self)
            elif choice == 3:
                return
            else:
                print("Invalid choice!")

    #  COMBINE OR SPLIT
    def combine_or_split(self):
        if self.array is None:
            print("No array available!")
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            elements = list(map(int, input("Enter elements of another array separated by space: ").split()))
            try:
                new_array = np.array(elements).reshape(self.array.shape)
                combined = np.vstack((self.array, new_array))
                print("\nCombined Array (Vertical Stack):")
                print(combined)
            except:
                print("Shape mismatch! Cannot combine arrays.")

        elif choice == 2:
            parts = int(input("Enter number of parts to split: "))
            try:
                split_arrays = np.array_split(self.array, parts)
                print("\nSplit Arrays:")
                for arr in split_arrays:
                    print(arr)
            except Exception as e:
                print("Error splitting array:", e)

    #  MATH OPERATIONS
    def mathematical_ops(self):
        if self.array is None:
            print("No array available!")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))
        elements = list(map(int, input(f"Enter {self.array.size} elements separated by space: ").split()))
        new_array = np.array(elements).reshape(self.array.shape)

        if choice == 1:
            result = self.array + new_array
        elif choice == 2:
            result = self.array - new_array
        elif choice == 3:
            result = self.array * new_array
        elif choice == 4:
            result = self.array / new_array
        else:
            print("Invalid choice!")
            return

        print("\nOriginal Array:\n", self.array)
        print("Second Array:\n", new_array)
        print("Result:\n", result)

    #  SEARCH, SORT, FILTER
    def search_sort_filter(self):
        if self.array is None:
            print("No array available!")
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to search: "))
            indices = np.where(self.array == val)
            print("Value found at:", indices)

        elif choice == 2:
            sorted_arr = np.sort(self.array, axis=None).reshape(self.array.shape)
            print("\nSorted Array:\n", sorted_arr)

        elif choice == 3:
            condition = int(input("Show values greater than: "))
            filtered = self.array[self.array > condition]
            print("\nFiltered Array:\n", filtered)

    #  AGGREGATES
    def aggregate_statistics(self):
        if self.array is None:
            print("No array available!")
            return

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Sum:", np.sum(self.array))
        elif choice == 2:
            print("Mean:", np.mean(self.array))
        elif choice == 3:
            print("Median:", np.median(self.array))
        elif choice == 4:
            print("Standard Deviation:", np.std(self.array))
        elif choice == 5:
            print("Variance:", np.var(self.array))
        else:
            print("Invalid choice!")


#  MAIN PROGRAM
def main():
    analyzer = DataAnalytics()

    while True:
        print("\nWelcome to the NumPy Analyzer!")
        print("====================================")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            analyzer.create_array_menu()
        elif choice == 2:
            analyzer.mathematical_ops()
        elif choice == 3:
            analyzer.combine_or_split()
        elif choice == 4:
            analyzer.search_sort_filter()
        elif choice == 5:
            analyzer.aggregate_statistics()
        elif choice == 6:
            print("Thank you for using NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


main()