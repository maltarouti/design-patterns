from iterator import Aggregate


if __name__ == "__main__":
    aggregate = Aggregate()

    iterator = iter(aggregate)

    # Case 1: iterate one by one manually
    print(next(iterator))
    print(next(iterator))

    # Case 2: Loop over the rest
    for x in iterator:
        print(x)
