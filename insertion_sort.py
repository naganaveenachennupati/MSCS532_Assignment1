"""
MSCS 532 - Assignment 1
Naga Naveena Chennupati

Insertion Sort in decreasing order.
"""


def insertion_sort_descending(values):
    """
    Sorts the list in monotonically decreasing order
    using the Insertion Sort algorithm.
    """

    for i in range(1, len(values)):
        current_value = values[i]
        j = i - 1

        # Move smaller values one position to the right.
        while j >= 0 and values[j] < current_value:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = current_value

    return values


def main():
    sample_values = [12, 7, 19, 3, 15, 8]

    print("Original values:")
    print(sample_values)

    insertion_sort_descending(sample_values)

    print("\nValues after Insertion Sort in decreasing order:")
    print(sample_values)


if __name__ == "__main__":
    main()