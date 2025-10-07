# Function to identify empty cells = 0
def find_empty_location(arr, l):
    size = len(arr)
    for i in range(size):
        for j in range(size):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

# Function to propose a number in the empty cell
def used_in_row(arr, row, num):
    size = len(arr)
    for i in range(size):
        if arr[row][i] == num:
            return True
    return False

# Function to check if proposed number is valid in the specific cell
def used_in_col(arr, col, num):
    size = len(arr)
    for i in range(size):
        if arr[i][col] == num:
            return True
    return False

def used_in_box(arr, row, col, num):
    size = len(arr)
    box_size = int(size**0.5)
    start_row = row - row % box_size
    start_col = col - col % box_size
    for i in range(box_size):
        for j in range(box_size):
            if arr[i + start_row][j + start_col] == num:
                return True
    return False

def check_location_is_safe(arr, row, col, num):
    size = len(arr)
    box_size = int(size**0.5)
    return (not used_in_row(arr, row, num) and 
            not used_in_col(arr, col, num) and 
            not used_in_box(arr, row, col, num))

# Recursive function to solve the sudoku
def solve_sudoku(arr):
    l = [0, 0]
    if not find_empty_location(arr, l):
        return True
    row = l[0]
    col = l[1]
    size = len(arr)
    for num in range(1, size + 1):
        if check_location_is_safe(arr, row, col, num):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True
            arr[row][col] = 0
    return False

def print_board(arr):
    """Helper function to print the board in a nice format"""
    size = len(arr)
    box_size = int(size**0.5)
    for i in range(size):
        if i % box_size == 0 and i != 0:
            print("-" * (size * 2 + box_size))
        for j in range(size):
            if j % box_size == 0 and j != 0:
                print("|", end=" ")
            print(arr[i][j], end=" ")
        print()

# Driver code
def main():
    print("Enter the size of the Sudoku (e.g., 4 for 4x4, 9 for 9x9): ")
    size = int(input())
    
    # Validate size is a perfect square
    box_size = size**0.5
    if box_size != int(box_size):
        print("Size must be a perfect square (4, 9, 16, etc.)")
        return
    
    print(f"Enter the Sudoku puzzle row by row, using 0 for empty cells (each row should have {size} numbers separated by spaces):")
    matrix = []
    for i in range(size):
        while True:
            try:
                row_input = input(f"Row {i+1}: ").strip()
                row = list(map(int, row_input.split()))
                if len(row) != size:
                    print(f"Each row must have exactly {size} numbers. You entered {len(row)}.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Please enter only numbers separated by spaces.")
    
    print("\nUnsolved Sudoku:")
    print_board(matrix)
    
    if solve_sudoku(matrix):
        print("\nSolved Sudoku:")
        print_board(matrix)
    else:
        print("\nNo solution exists")

if __name__ == "__main__":
    main()