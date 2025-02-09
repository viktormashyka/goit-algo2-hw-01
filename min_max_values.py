def min_max_values(arr):
    min_value = arr[0]
    max_value = arr[0]

    # Print the header of the table
    print(f"{'current':>10} {'min value':>10} {'max value':>10}")
    print("-" * 30)
    print(f"{arr[0]:>10} {min_value:>10} {max_value:>10}")

    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
        elif arr[i] > max_value:
            max_value = arr[i]
        else:
            continue

        # Print the current values in a table format
        print(f"{arr[i]:>10} {min_value:>10} {max_value:>10}")

    return min_value, max_value

arr = [3, 12, 2, -123, 56, -156, 14, 0, 8]

print("\nResult min and max values: ", min_max_values(arr))

print('\n***** Recursive version *****\n')

def min_max_values_recursive(arr, index=0, min_value=None, max_value=None):
    if index == 0:
        min_value = arr[0]
        max_value = arr[0]
        # Print the header of the table
        print(f"{'current':>10} {'min value':>10} {'max value':>10}")
        print("-" * 30)
        print(f"{arr[0]:>10} {min_value:>10} {max_value:>10}")

    if index == len(arr):
        return min_value, max_value

    current_value = arr[index]
    if current_value < min_value:
        min_value = current_value
    elif current_value > max_value:
        max_value = current_value

    # Print the current values in a table format
    print(f"{current_value:>10} {min_value:>10} {max_value:>10}")

    return min_max_values_recursive(arr, index + 1, min_value, max_value)

arr = [3, 12, 2, -123, 56, -156, 14, 0, 8]

print("\nResult min and max values: ", min_max_values_recursive(arr))

