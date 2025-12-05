import numpy as np

def one_array(self):
    elements = input("Enter elements separated by space: ")
    data = list(map(int, elements.split()))
    self.array = np.array(data)

def two_array(self):
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    elements = list(map(int, input(f"Enter {rows * cols} elements separated by space: ").split()))
    self.array = np.array(elements).reshape(rows, cols)

def three_array(self):
    x = int(input("Enter number of matrices: "))
    y = int(input("Enter number of rows: "))
    z = int(input("Enter number of columns: "))
    elements = list(map(int, input(f"Enter {x * y * z} elements separated by space: ").split()))
    self.array = np.array(elements).reshape(x, y, z)


def indexing_one(self):
    idx_input = input("Enter index (comma separated for multi-dim): ")
    idx = tuple(map(int, idx_input.split(",")))
    print("Element:", self.array[idx])

def slicing_two(self):
    if self.array.ndim == 1:
        s = input("Enter slice (start:end): ")
        start, end = map(int, s.split(":"))
        print("Sliced Array:", self.array[start:end])
    else:
        r = input("Enter row slice (start:end): ")
        c = input("Enter column slice (start:end): ")
        r_start, r_end = map(int, r.split(":"))
        c_start, c_end = map(int, c.split(":"))
        print("Sliced Array:\n", self.array[r_start:r_end, c_start:c_end])