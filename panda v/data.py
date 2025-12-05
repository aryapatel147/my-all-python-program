import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#auto file finder use

class SalesDataAnalyzer:
    def __init__(self):
        self.data = None
        self.last_plot = None

   
    def load_data(self):
      
        possible_files = ["sales_data.csv", "sales.csv", "data.csv"]

        found_file = None
        for fname in possible_files:
            if os.path.exists(fname):
                found_file = fname
                break

        if found_file:
            print(f"Found CSV file: {found_file}")
            try:
                self.data = pd.read_csv(found_file)
                print("Dataset loaded successfully from", found_file)
                return
            except Exception as e:
                print("Error loading file:", e)

        
        path = input("Enter CSV path (e.g. sales_data.csv): ")
        try:
            self.data = pd.read_csv(path)
            print("Dataset loaded successfully from", path)
        except FileNotFoundError:
            print("File not found. Check path again.")
        except Exception as e:
            print("Error reading CSV:", e)

    

    def explore_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n== Explore Data ==")
            print("1. Head")
            print("2. Tail")
            print("3. Columns")
            print("4. Dtypes")
            print("5. Info")
            print("6. Back")

            choice = input("Choice: ")

            if choice == '1':
                print(self.data.head())
            elif choice == '2':
                print(self.data.tail())
            elif choice == '3':
                print(self.data.columns)
            elif choice == '4':
                print(self.data.dtypes)
            elif choice == '5':
                print(self.data.info())
            elif choice == '6':
                break
            else:
                print("Invalid choice.")

    

    def mathematical_operations(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        if "Sales" in self.data.columns and "Profit" in self.data.columns:
            self.data["Profit Margin %"] = (self.data["Profit"] / self.data["Sales"]) * 100
            print("Profit Margin % column added.")
        else:
            print("Sales or Profit column missing.")

    # ==== DESCRIPTIVE STATISTICS ====

    def descriptive_statistics(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        print("\n--- Descriptive Statistics ---")
        print(self.data.describe())

    # ==== VISUALIZATION ====

    def visualize_data(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        while True:
            print("\n== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Histogram")
            print("5. Back")

            choice = input("Choice: ")

            if choice == '1':
                x = input("X column: ")
                y = input("Y column: ")
                sns.barplot(data=self.data, x=x, y=y)

            elif choice == '2':
                x = input("X column: ")
                y = input("Y column: ")
                sns.lineplot(data=self.data, x=x, y=y)

            elif choice == '3':
                x = input("X column: ")
                y = input("Y column: ")
                sns.scatterplot(data=self.data, x=x, y=y)

            elif choice == '4':
                col = input("Column for histogram: ")
                if col in self.data.columns:
                    plt.hist(self.data[col], bins=10)
                else:
                    print("Column not found.")
                    continue

            elif choice == '5':
                break
            else:
                print("Invalid choice.")
                continue

            plt.xlabel(x if choice in ['1', '2', '3'] else col)
            if choice in ['1', '2', '3']:
                plt.ylabel(y)
            plt.show()
            self.last_plot = plt.gcf()

    # ==== SAVE PLOT ====

    def save_visualization(self):
        if self.last_plot is None:
            print("No plot created yet.")
            return

        name = input("Filename (e.g. plot.png): ")
        self.last_plot.savefig(name)
        print("Saved as", name)


# ==== MAIN PROGRAM ====

def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========= MAIN MENU =========")
        print("1. Load Data")
        print("2. Explore Data")
        print("3. Math Operations")
        print("4. Descriptive Statistics")
        print("5. Visualize")
        print("6. Save Plot")
        print("7. Exit")

        choice = input("Choice: ")

        if choice == '1':
            analyzer.load_data()
        elif choice == '2':
            analyzer.explore_data()
        elif choice == '3':
            analyzer.mathematical_operations()
        elif choice == '4':
            analyzer.descriptive_statistics()
        elif choice == '5':
            analyzer.visualize_data()
        elif choice == '6':
            analyzer.save_visualization()
        elif choice == '7':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
