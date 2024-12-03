import numpy as np


def part_one():
    data = np.loadtxt("input.txt")

    # Sort and combine columns in a single step
    data = np.column_stack((np.sort(data[:, 0]), np.sort(data[:, 1])))

    # Calculate the row-wise absolute differences
    diff = np.abs(data[:, 0] - data[:, 1])

    # print(diff)
    print(f"Part one: {sum(diff)}")


def part_two():
    data = np.loadtxt("input.txt")
    
    # Split into left and right columns
    left = data[:, 0]
    right = data[:, 1]
    
    # Calculate similarity score
    total_score = sum(num * np.count_nonzero(right == num) for num in left)
    
    print(f"Part two: {total_score}")


if __name__ == "__main__":
    part_one()
    part_two()
