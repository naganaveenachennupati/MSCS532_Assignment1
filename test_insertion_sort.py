from insertion_sort import insertion_sort_descending


def run_tests():
    test_cases = [
        ([12, 7, 19, 3, 15, 8], [19, 15, 12, 8, 7, 3]),
        ([9, 7, 5, 3, 1], [9, 7, 5, 3, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([4, 2, 4, 1], [4, 4, 2, 1]),
        ([-3, 2, 0, -1], [2, 0, -1, -3]),
        ([], []),
        ([10], [10]),
    ]

    for values, expected in test_cases:
        result = insertion_sort_descending(values.copy())
        assert result == expected

    print("All Insertion Sort tests passed successfully.")


if __name__ == "__main__":
    run_tests()