from collections import Counter


def count_elements(iterable):
    """
    Counts the frequency of each element in an iterable.

    Args:
    iterable (iterable): An iterable object containing hashable elements.

    Returns:
    dict: A standard dictionary with elements of the iterable as keys and their frequency counts as values.

    Exceptions:
    TypeError: If the input is not an iterable or contains non-hashable elements.
    """
    try:
        # Using Counter to count elements in the iterable
        counter_result = Counter(iterable)

        # Convert Counter object to a standard dictionary
        return dict(counter_result)
    except TypeError as e:
        print(f"An error occurred: {e}")
        return {}