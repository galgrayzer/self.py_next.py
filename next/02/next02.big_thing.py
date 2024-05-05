class BigThing:
    def __init__(self, item):
        self._item = item

    def size(self):
        if isinstance(self._item, (list, str, dict)):
            return len(self._item)
        elif isinstance(self._item, int):
            return self._item


class BigCat(BigThing):
    def __init__(self, item, weight):
        super().__init__(item)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return 'Very Fat'
        elif self._weight > 15:
            return 'Fat'
        else:
            return 'OK'


def main():
    big_thing = BigThing([1, 2, 3])
    print(big_thing.size())
    big_thing = BigThing('123')
    print(big_thing.size())
    big_thing = BigThing({1: 'a', 2: 'b'})
    print(big_thing.size())
    big_thing = BigThing(123)
    print(big_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()
