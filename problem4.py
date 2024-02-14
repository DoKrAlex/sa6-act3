def find_intersection(list1, list2):
    """
    Find the intersection of two lists using a lambda function and the filter() function.

    Parameters:
        list1 (list): First list of elements.
        list2 (list): Second list of elements.

    Returns:
        list: Intersection of the two lists.
    """
    # Use filter() with a lambda function to keep only the elements in list1 that are also in list2
    intersection = list(filter(lambda x: x in list2, list1))
    return intersection

# Example usage:
if __name__ == "__main__":
    # Two lists
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]

    # Find the intersection of the two lists
    intersection = find_intersection(list1, list2)

    # Print the intersection
    print("Intersection of the two lists:", intersection)
