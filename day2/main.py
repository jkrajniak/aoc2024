import numpy as np


def verify_row(row):
    row_diff = np.diff(row)
    return (np.all(np.sign(row_diff) == -1) or np.all(np.sign(row_diff) == 1)) and np.all(np.abs(row_diff) <= 3)


def can_row_be_fixed(row):
    # row_diff = np.diff(row)
    # row_diff_sign = np.sign(row_diff)
    
    # # Count how many times each sign value appears
    # unique, counts = np.unique(row_diff_sign, return_counts=True)
    # if len(unique) > 2:
    #     return False
    # if min(counts) > 1:
    #     return False
    # print(row, row_diff_sign, unique, counts)
    for i in range(len(row)):
        # Create a new row with the i-th element removed
        new_row = np.delete(row, i)
        if verify_row(new_row):
            return True
    return False


def part_one():
    safe_count = 0
    with open("input.txt") as f:
        for line in f:
            data = np.array(line.split(), dtype=int)
            if verify_row(data):
                safe_count += 1
    print(f"Part one: {safe_count}")
    

def part_two():
    safe_count = 0
    with open("input.txt") as f:
        for line in f:
            data = np.array(line.split(), dtype=int)
            if verify_row(data):
                safe_count += 1
            else:
                if can_row_be_fixed(data):
                    safe_count += 1
                
    print(f"Part two: {safe_count}")

if __name__ == "__main__":
    part_one()
    part_two()
