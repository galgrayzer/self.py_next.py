def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])


def main():
    prices = [("item1", 50.20), ("item2", 15.10), ("item3", 24.5)]
    print(sort_prices(prices))


if __name__ == '__main__':
    main()
